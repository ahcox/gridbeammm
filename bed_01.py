import cadquery as cq
import sys
import copy
import beam

from beam import *


# Lay out a few parts:
"""result =  build_beam(default_beam_args, 1,1)
result += build_beam(default_beam_args, 2,1).translate([default_beam_args.half_unit, default_beam_args.half_unit * 3, 0])
result += build_grid_beam(default_beam_args, 1,1).translate([default_beam_args.half_unit * 0, default_beam_args.half_unit * 6, 0])
result += build_grid_beam(default_beam_args, 2,1).translate([default_beam_args.half_unit * 1, default_beam_args.half_unit * 9, 0])
result += build_grid_beam_bored(default_beam_args, 1,1).translate([default_beam_args.half_unit * 0, default_beam_args.half_unit * 12, 0])
result += build_grid_beam_bored(default_beam_args, 2,1).translate([default_beam_args.half_unit * 1, default_beam_args.half_unit * 15, 0])
# Regular grid beam but with hard-edged holes:
hard_edge_args = default_beam_args.copy()
hard_edge_args.bolt_contersink_diameter = 0.01
result += build_grid_beam(default_beam_args, 1,1).translate([default_beam_args.half_unit * 0, default_beam_args.half_unit * 18, 0])
result += build_grid_beam(default_beam_args, 2,1).translate([default_beam_args.half_unit * 1, default_beam_args.half_unit * 21, 0])
"""
# Regular grid beam but with hard-edged holes:
#hard_edge_args = copy.copy(default_beam_args)
#hard_edge_args.bolt_contersink_diameter = 0.01
# 1 x 10
#result  = build_grid_beam(default_beam_args, 10,1)
spacing = default_beam_args.half_unit / 4
stride  = spacing + default_beam_args.unit
base = spacing / 2 + default_beam_args.half_unit
result  = build_grid_beam_capped_x(default_beam_args, 30,1, 1).translate([0, base, 0])
result += build_grid_beam_capped_x(default_beam_args, 30,1, 1).translate([0, base + stride * 1, 0])
result += build_grid_beam_capped_x(default_beam_args, 25,1, 1).translate([0, base + stride * 2, 0])
result += build_grid_beam_capped_x(default_beam_args, 25,1, 1).translate([0, base + stride * 3, 0])
result += build_grid_beam_capped_x(default_beam_args, 25,1, 1).translate([0, base + stride * 4, 0])
result += build_grid_beam_capped_x(default_beam_args, 20,1, 1).translate([0, base + stride * 5, 0])
result += build_grid_beam_capped_x(default_beam_args, 20,1, 1).translate([0, base + stride * 6, 0])
result += build_grid_beam_capped_x(default_beam_args, 20,1, 1).translate([0, base + stride * 7, 0])
result += build_grid_beam(default_beam_args, 5,1, 1).translate([-default_beam_args.unit * 5 - spacing, base + stride * 8, 0])
result += build_grid_beam(default_beam_args, 5,1, 1).translate([0, base + stride * 8, 0])
result += build_grid_beam(default_beam_args, 5,1, 1).translate([default_beam_args.unit* 5 + spacing, base + stride * 8, 0])
result += build_grid_beam(default_beam_args, 5,1, 1).translate([-default_beam_args.unit * 5 - spacing, base + stride * 9, 0])
result += build_grid_beam(default_beam_args, 5,1, 1).translate([0, base + stride * 9, 0])
result += build_grid_beam(default_beam_args, 5,1, 1).translate([default_beam_args.unit* 5 + spacing, base + stride * 9, 0])

result = result.rotate([0,0,0], [0,0,1],45)
# Duplicate a mirror image on other side of the bed:
result += result.rotate([0,0,0], [0,0,1], 180)
#result = build_grid_beam_capped_x_plugged(default_beam_args, 10,1, 1).translate([0, default_beam_args.half_unit * 6, 0])
#cq.exporters.export(result, "gridbeam_test_01.step")
cq.exporters.export(result, "gridbeam_bed_01.svg")
#cq.exporters.export(result, "gridbeam_test_01.stl")
#cq.exporters.export(result, "gridbeam_test_01.3mf")
cq.exporters.export(result, "gridbeam_bed_01.3mf")
