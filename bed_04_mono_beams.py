import cadquery as cq
import sys
import copy
import beam

from beam import *

def post(i):
    old = i[0]
    i[0] += 1
    return old

# Regular grid beam but with hard-edged holes:
#hard_edge_args = copy.copy(default_beam_args)
#hard_edge_args.bolt_contersink_diameter = 0.01
# 1 x 10
#result  = build_grid_beam(default_beam_args, 10,1)
spacing = default_beam_args.half_unit / 4
stride  = spacing + default_beam_args.unit
base = stride #spacing /+ default_beam_args.unit
step = [int(0)]
result  = build_grid_beam_only_vertical(default_beam_args, 40,1, 1)
result += build_grid_beam_only_vertical(default_beam_args, 38,1, 1).translate([0, base + stride * post(step), 0])
"""result += build_grid_beam_only_vertical(default_beam_args, 35,1, 1).translate([0, base + stride * post(step), 0])
result += build_grid_beam_only_vertical(default_beam_args, 33,1, 1).translate([0, base + stride * post(step), 0])
result += build_grid_beam_only_vertical(default_beam_args, 30,1, 1).translate([0, base + stride * post(step), 0])
result += build_grid_beam_only_vertical(default_beam_args, 28,1, 1).translate([0, base + stride * post(step), 0])
result += build_grid_beam_only_vertical(default_beam_args, 26,1, 1).translate([0, base + stride * post(step), 0])
result += build_grid_beam_only_vertical(default_beam_args, 24,1, 1).translate([0, base + stride * post(step), 0])
result += build_grid_beam_only_vertical(default_beam_args, 22,1, 1).translate([0, base + stride * post(step), 0])
result += build_grid_beam_only_vertical(default_beam_args, 20,1, 1).translate([0, base + stride * post(step), 0])
result += build_grid_beam_only_vertical(default_beam_args, 18,1, 1).translate([0, base + stride * post(step), 0])
result += build_grid_beam_only_vertical(default_beam_args, 15,1, 1).translate([0, base + stride * post(step), 0])
result += build_grid_beam_only_vertical(default_beam_args, 13,1, 1).translate([0, base + stride * post(step), 0])
result += build_grid_beam_only_vertical(default_beam_args, 11,1, 1).translate([0, base + stride * post(step), 0])
result += build_grid_beam_only_vertical(default_beam_args,  9,1, 1).translate([0, base + stride * post(step), 0])
result += build_grid_beam_only_vertical(default_beam_args,  6,1, 1).translate([0, base + stride * post(step), 0])
result += build_grid_beam_only_vertical(default_beam_args,  4,1, 1).translate([0, base + stride * post(step), 0])
result += build_grid_beam_only_vertical(default_beam_args,  2,1, 1).translate([0, base + stride * post(step), 0])
"""
result = result.rotate([0,0,0], [0,0,1],45)
# Duplicate a mirror image on other side of the bed:
result += result.rotate([0,0,0], [0,0,1], 180)
result = result.clean()

cq.exporters.export(result, "gridbeam_bed_04.3mf")

# Visualise with the bed attached:
bed = cq.Workplane("XY" ).box(300, 300, 1).translate([0, 0, -default_beam_args.half_unit - spacing])
result += bed
cq.exporters.export(result, "gridbeam_bed_04.svg")