#!/usr/bin/env python3
"""Generate parametric Savonius rotor assets using FreeCAD Python API.

Outputs (under output_dir):
- top_plate.stl
- bottom_plate.stl
- top_plate.step
- bottom_plate.step
- assembly_preview.step
- blade_template.dxf
"""

from __future__ import annotations

import json
import math
import os
import sys
from pathlib import Path

try:
    import FreeCAD as App
    import Part
    import Mesh
    import importDXF
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "FreeCAD Python modules were not found. Run with FreeCAD's Python interpreter."
    ) from exc


def load_config(config_path: Path) -> dict:
    with config_path.open("r", encoding="utf-8") as f:
        cfg = json.load(f)
    return cfg


def mm(val: float) -> float:
    return float(val)


def make_end_plate(cfg: dict, z: float, name: str) -> Part.Shape:
    radius = mm(cfg["diameter_mm"]) / 2.0 + mm(cfg["plate_margin_mm"])
    thickness = mm(cfg["plate_thickness_mm"])
    shaft_radius = mm(cfg["shaft_hole_diameter_mm"]) / 2.0

    disk = Part.makeCylinder(radius, thickness, App.Vector(0, 0, z))
    shaft_hole = Part.makeCylinder(shaft_radius, thickness + 2.0, App.Vector(0, 0, z - 1.0))
    plate = disk.cut(shaft_hole)

    slot_depth = mm(cfg["slot_depth_mm"])
    blade_thickness = mm(cfg["blade_thickness_mm"])
    slot_width = blade_thickness + mm(cfg["slot_clearance_mm"])
    rotor_radius = mm(cfg["diameter_mm"]) / 2.0
    overlap = rotor_radius * float(cfg["center_overlap_ratio"])

    half_cyl_r = rotor_radius / 2.0
    centers = [
        App.Vector(-half_cyl_r + overlap / 2.0, 0, z),
        App.Vector(half_cyl_r - overlap / 2.0, 0, z),
    ]

    base_slot = Part.makeBox(slot_depth, slot_width, thickness + 2.0)
    base_slot.translate(App.Vector(0, -slot_width / 2.0, z - 1.0))

    blade_count = int(cfg["blade_count"])
    for i in range(blade_count):
        angle = (360.0 / blade_count) * i
        for c in centers:
            slot = base_slot.copy()
            slot.rotate(App.Vector(0, 0, z), App.Vector(0, 0, 1), angle)
            slot.translate(c)
            plate = plate.cut(slot)

    plate = plate.removeSplitter()
    return plate


def make_blade_surface(cfg: dict, phase_deg: float) -> Part.Shape:
    h = mm(cfg["height_mm"])
    rotor_radius = mm(cfg["diameter_mm"]) / 2.0
    twist = float(cfg["twist_deg"])
    overlap = rotor_radius * float(cfg["center_overlap_ratio"])

    half_cyl_r = rotor_radius / 2.0
    center = App.Vector(-half_cyl_r + overlap / 2.0, 0, 0)

    c1 = Part.makeCircle(half_cyl_r, center, App.Vector(0, 0, 1), -90, 90)
    arc_bottom = Part.Wire([Part.Edge(c1)])
    arc_bottom.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), phase_deg)

    arc_top = arc_bottom.copy()
    arc_top.translate(App.Vector(0, 0, h))
    arc_top.rotate(App.Vector(0, 0, h), App.Vector(0, 0, 1), twist)

    blade_face = Part.makeLoft([arc_bottom, arc_top], ruled=False, solid=False)
    return blade_face


def make_blade_template_dxf(cfg: dict, out_path: Path) -> None:
    h = mm(cfg["height_mm"])
    rotor_radius = mm(cfg["diameter_mm"]) / 2.0
    half_cyl_r = rotor_radius / 2.0
    arc_len = math.pi * half_cyl_r

    doc = App.newDocument("BladeTemplate")
    p1 = App.Vector(0, 0, 0)
    p2 = App.Vector(arc_len, 0, 0)
    p3 = App.Vector(arc_len, h, 0)
    p4 = App.Vector(0, h, 0)

    wire = Part.makePolygon([p1, p2, p3, p4, p1])
    obj = doc.addObject("Part::Feature", "BladeTemplate")
    obj.Shape = wire

    App.ActiveDocument.recompute()
    importDXF.export([obj], str(out_path))
    App.closeDocument(doc.Name)


def export_shape(shape: Part.Shape, stl_path: Path, step_path: Path) -> None:
    Mesh.export([shape], str(stl_path))
    shape.exportStep(str(step_path))


def main() -> int:
    cfg_path = Path("config.json")
    if not cfg_path.exists():
        raise SystemExit("config.json not found in current directory.")

    cfg = load_config(cfg_path)
    out_dir = Path(cfg.get("output_dir", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)

    h = mm(cfg["height_mm"])
    top = make_end_plate(cfg, h, "top")
    bottom = make_end_plate(cfg, 0.0, "bottom")

    export_shape(top, out_dir / "top_plate.stl", out_dir / "top_plate.step")
    export_shape(bottom, out_dir / "bottom_plate.stl", out_dir / "bottom_plate.step")

    blade_count = int(cfg["blade_count"])
    blades = []
    for i in range(blade_count):
        phase = (360.0 / blade_count) * i
        blades.append(make_blade_surface(cfg, phase))

    assembly = top.fuse(bottom)
    for b in blades:
        assembly = assembly.fuse(b)
    assembly.exportStep(str(out_dir / "assembly_preview.step"))

    make_blade_template_dxf(cfg, out_dir / "blade_template.dxf")

    print(f"Generated outputs in: {out_dir.resolve()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
