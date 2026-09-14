#!/usr/bin/env python3
"""Materialize website-only derivatives from one immutable evaluations registry."""
from __future__ import annotations

import copy
import hashlib
import json
import re
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path, PurePosixPath

REPO = "WumboLabs/evaluations"
PIN = Path("data/evaluations-source.json")
SHA = re.compile(r"[0-9a-f]{40}")


def safe_path(value):
    if not isinstance(value, str) or not value or PurePosixPath(value).is_absolute() \
            or any(p in ("", ".", "..") for p in value.split("/")) \
            or re.search(r"[\\%?#\x00-\x20]", value):
        raise ValueError(f"unsafe evaluations source path: {value!r}")
    return value


def fetch(commit, path, expected=None):
    if not isinstance(commit, str) or not SHA.fullmatch(commit):
        raise ValueError("evaluations source requires an exact full commit SHA")
    url = f"https://raw.githubusercontent.com/{REPO}/{commit}/{safe_path(path)}"
    with urllib.request.urlopen(url, timeout=30) as response:
        raw = response.read()
    if expected is not None and hashlib.sha256(raw).hexdigest() != expected:
        raise ValueError(f"evaluations source hash mismatch: {path}")
    return raw


def migrate_links(text, targets, commit):
    """Migrate current navigation, retaining quoted historical provenance verbatim."""
    pattern = re.compile(r"https://github\.com/(WumboLabs/(?:eval-[A-Za-z0-9._-]+|labs))(?:/(?:tree|blob)/[^\s/)>\"`]+(?:/[^\s)>\"`]*)?)?")

    def replace(match):
        path = targets.get(match.group(1))
        if path is None:
            raise ValueError(f"unmapped legacy evidence link: {match.group(0)}")
        return f"https://github.com/{REPO}/tree/{commit}/{path}"

    lines = []
    for line in text.splitlines(keepends=True):
        # Quoted historical notes describe their original publication topology.
        # Their source links must continue identifying that history, not its replacement.
        if line.lstrip().startswith(">"):
            lines.append(line)
            continue
        migrated = pattern.sub(replace, line)
        migrated = re.sub(
            r"\[(?:WumboLabs/)?eval-[^\]]+\](\(https://github\.com/WumboLabs/evaluations/[^)]+\))",
            r"[Central evidence]\1", migrated)
        lines.append(migrated)
    return "".join(lines)


def project(registry, pin, payloads):
    if registry.get("schema") != "wumbolabs-evaluations/1":
        raise ValueError("unsupported central evaluations registry")
    models = copy.deepcopy(registry["models"])
    profiles = {p["profile_id"]: p for p in registry["profiles"]}
    targets = {source["repo"]: source["landing_path"] for source in registry["legacy_sources"]}
    outputs = {}
    records = []
    for original in registry["records"] + registry["shared_events"]:
        entry = copy.deepcopy(original)
        if entry.get("shared_event_id"):
            attribution = entry["website_attribution"]
            entry.update(attribution)
            entry["related_model_ids"] = [mid for mid in entry["related_model_ids"] if mid != entry["model_id"]]
            # Preserve the prior website's related-profile display, not a new owner.
            entry["related_profile_ids"] = [pid for pid in entry["related_profile_ids"] if pid != entry["profile_id"]]
        evidence = entry["canonical_evidence"]
        if evidence.get("repo") != REPO or not SHA.fullmatch(evidence.get("commit", "")):
            raise ValueError(f"invalid canonical evidence pin: {entry['event_id']}")
        evidence["url"] = f"https://github.com/{REPO}/blob/{evidence['commit']}/{safe_path(evidence['path'])}"
        entry["profile_metadata_urls"] = {
            pid: f"https://github.com/{REPO}/blob/{pin['commit']}/{profiles[pid]['profile_path']}/profile.json"
            for pid in [entry["profile_id"], *entry.get("related_profile_ids", [])]
        }
        entry["model_evidence_url"] = f"https://github.com/{REPO}/tree/{pin['commit']}/models/{entry['model_id']}"
        if original.get("source"):
            source = original["source"]
            raw = payloads[(source["commit"], source["path"])]
            rel = f"data/generated/evaluations-exports/{entry['event_id']}.json"
            outputs[rel] = raw
            entry["source"] = {"kind": "repository-cache", "repo": REPO, "ref": source["commit"],
                               "path": source["path"], "sha256": source["sha256"], "file": rel}
        if original.get("body_source"):
            source = original["body_source"]
            raw = payloads[(source["commit"], source["path"])]
            rel = f"labs-events/{entry['event_id']}.md"
            outputs["data/" + rel] = migrate_links(raw.decode("utf-8"), targets, pin["commit"]).encode("utf-8")
            entry["event_body"] = rel
        records.append(entry)
    # Preserve existing registry order as an explicit presentation property.
    order = {eid: i for i, eid in enumerate(registry["website_event_order"])}
    records.sort(key=lambda entry: order[entry["event_id"]])
    projected = {"version": 3, "generated_by": "scripts/evaluations_source.py — do not hand-edit",
                 "source_pin": pin, "description": "Deterministic derivative of the canonical WumboLabs/evaluations registry; edit that source, not this file.",
                 "models": models, "profiles": registry["profiles"], "records": records}
    outputs["data/labs-registry.json"] = (json.dumps(projected, indent=2, ensure_ascii=False) + "\n").encode()
    return outputs


def synchronize(base, check_only=False):
    pin = json.loads((base / PIN).read_text(encoding="utf-8"))
    if pin.get("repo") != REPO or pin.get("path") != "registry.json" \
            or not re.fullmatch(r"[0-9a-f]{64}", pin.get("sha256", "")):
        raise ValueError("invalid central evaluations source pin")
    registry = json.loads(fetch(pin["commit"], pin["path"], pin["sha256"]))
    sources = {}
    for event in registry["records"] + registry["shared_events"]:
        for field in ("source", "body_source"):
            source = event.get(field)
            if source:
                key = (source["commit"], source["path"])
                if key in sources and sources[key] != source["sha256"]:
                    raise ValueError(f"conflicting central source hashes: {key}")
                sources[key] = source["sha256"]

    def get(item):
        key, expected = item
        return key, fetch(*key, expected)

    with ThreadPoolExecutor(max_workers=8) as pool:
        payloads = dict(pool.map(get, sources.items()))
    outputs = project(registry, pin, payloads)
    changed = []
    for rel, raw in outputs.items():
        path = base / safe_path(rel)
        if not path.is_file() or path.read_bytes() != raw:
            changed.append(rel)
            if not check_only:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(raw)
    print(f"Evaluations source {'CHECK' if check_only else 'sync'}: {len(changed)} changes; {REPO}@{pin['commit']}")
    if check_only and changed:
        raise ValueError(f"central source derivatives are stale: {changed}")
    return changed
