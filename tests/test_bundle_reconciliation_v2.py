"""Protect canonical source ownership and reproducible checked-in bundle output."""
import json

import pytest

from build.builder import DEFAULT_BUNDLE_PATH, build_bundle
from engine.graph import build_graph
from engine.loader import load_entities


@pytest.mark.parametrize("core_id,platform_id,name", [
    ("core.mame", "platform.arcade", "MAME"),
    ("core.mupen64plus.next", "platform.nintendo.n64", "Mupen64Plus-Next"),
])
def test_previously_bundle_only_knowledge_has_canonical_source(core_id, platform_id, name):
    entities = {entity.id: entity.data for entity in load_entities()}
    assert entities[core_id] == {"id": core_id, "type": "core", "name": name}
    assert entities[platform_id]["relationships"]["supports_core"] == [core_id]
    assert core_id in entities["frontend.retroarch"]["relationships"]["launches_core"]
    claim = entities[f"compatibility.{core_id}.{platform_id}"]
    assert claim["type"] == "compatibility"
    assert claim["subject"] == core_id
    assert claim["platform"] == platform_id
    assert claim["playability"] == "playable"
    assert len(claim["evidence"]) == 3
    for evidence in claim["evidence"]:
        # Promotion preserves historical provenance, not a new runtime qualification.
        assert evidence["checked_at"] == "2026-09-23"
        assert evidence["source"]
        assert evidence["url"].startswith("https://")
        assert evidence["notes"]


def test_checked_in_bundle_matches_validated_source_and_deterministic_build(monkeypatch, tmp_path):
    import commands.build as command

    first = tmp_path / "first.json"
    monkeypatch.setattr(command, "build_bundle", lambda graph: build_bundle(graph, first))
    assert command.cmd_build() == first
    # Comparing bytes detects both stale knowledge and non-canonical serialization.
    assert first.read_bytes() == DEFAULT_BUNDLE_PATH.read_bytes()
    second = tmp_path / "second.json"
    build_bundle(build_graph(list(reversed(load_entities()))), second)
    assert second.read_bytes() == first.read_bytes()

    data = json.loads(first.read_text())
    assert len(data["nodes"]) == len(data["edges"]) == 57
    assert set(data["nodes"]) == set(data["edges"])
    for identity, node in data["nodes"].items():
        assert data["edges"][identity] == node.get("relationships", {})
