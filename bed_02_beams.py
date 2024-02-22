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
result  = build_grid_beam_capped_x(default_beam_args, 40,1, 1)
result += build_grid_beam_capped_x(default_beam_args, 35,1, 1).translate([0, base + stride * post(step), 0])

result += build_grid_beam_capped_x(default_beam_args, 2,1, 1).translate([-default_beam_args.unit * (30/2 + 1) - spacing, base + stride * step[0], 0])
result += build_grid_beam_capped_x(default_beam_args, 2,1, 1).translate([default_beam_args.unit * (30/2 + 1) + spacing, base + stride * step[0], 0])
result += build_grid_beam_capped_x(default_beam_args, 30,1, 1).translate([0, base + stride * post(step), 0])

result += build_grid_beam_capped_x(default_beam_args, 2,1, 1).translate([-default_beam_args.unit * (25/2 + 1) - spacing, base + stride * step[0], 0])
result += build_grid_beam_capped_x(default_beam_args, 2,1, 1).translate([default_beam_args.unit * (25/2 + 1) + spacing, base + stride * step[0], 0])
result += build_grid_beam_capped_x(default_beam_args, 25,1, 1).translate([0, base + stride * post(step), 0])

result += build_grid_beam_capped_x(default_beam_args, 2,1, 1).translate([-default_beam_args.unit * (25/2 + 1) - spacing, base + stride * step[0], 0])
result += build_grid_beam_capped_x(default_beam_args, 2,1, 1).translate([default_beam_args.unit * (25/2 + 1) + spacing, base + stride * step[0], 0])
result += build_grid_beam_capped_x(default_beam_args, 25,1, 1).translate([0, base + stride * post(step), 0])

result += build_grid_beam_capped_x(default_beam_args, 25,1, 1).translate([0, base + stride * post(step), 0])

result += build_grid_beam_capped_x(default_beam_args, 3,1, 1).translate([-default_beam_args.unit * (20/2 + 1.5) - spacing, base + stride * step[0], 0])
result += build_grid_beam_capped_x(default_beam_args, 3,1, 1).translate([default_beam_args.unit * (20/2 + 1.5) + spacing, base + stride * step[0], 0])
result += build_grid_beam_capped_x(default_beam_args, 20,1, 1).translate([0, base + stride * post(step), 0])

result += build_grid_beam_capped_x(default_beam_args, 2,1, 1).translate([-default_beam_args.unit * (20/2 + 1) - spacing, base + stride * step[0], 0])
result += build_grid_beam_capped_x(default_beam_args, 2,1, 1).translate([default_beam_args.unit * (20/2 + 1) + spacing, base + stride * step[0], 0])
result += build_grid_beam_capped_x(default_beam_args, 20,1, 1).translate([0, base + stride * post(step), 0])

result += build_grid_beam_capped_x(default_beam_args, 3,1, 1).translate([-default_beam_args.unit * (16/2 + 1.5) - spacing * 2.5, base + stride * step[0], 0])
result += build_grid_beam_capped_x(default_beam_args, 3,1, 1).translate([ default_beam_args.unit * (16/2 + 1.5) + spacing * 2.5, base + stride * step[0], 0])
result += build_grid_beam_capped_x(default_beam_args, 4,1, 1).translate([-default_beam_args.unit * 6 - spacing*1.5, base + stride * step[0], 0])

result += build_grid_beam_capped_x(default_beam_args, 4,1, 1).translate([-default_beam_args.unit * 2 - spacing*0.5, base + stride * step[0], 0])
result += build_grid_beam_capped_x(default_beam_args, 4,1, 1).translate([ default_beam_args.unit * 2 + spacing*0.5, base + stride * step[0], 0])
result += build_grid_beam_capped_x(default_beam_args, 4,1, 1).translate([ default_beam_args.unit * 6 + spacing*1.5, base + stride * post(step), 0])

result += build_grid_beam_capped_x(default_beam_args, 2,1, 1).translate([-default_beam_args.unit * (15/2 + 1) - spacing * 2, base + stride * step[0], 0])
result += build_grid_beam_capped_x(default_beam_args, 2,1, 1).translate([ default_beam_args.unit * (15/2 + 1) + spacing * 2, base + stride * step[0], 0])
result += build_grid_beam_capped_x(default_beam_args, 5,1, 1).translate([-default_beam_args.unit * 5 - spacing, base + stride * step[0], 0])
result += build_grid_beam_capped_x(default_beam_args, 5,1, 1).translate([0, base + stride * step[0], 0])
result += build_grid_beam_capped_x(default_beam_args, 5,1, 1).translate([default_beam_args.unit* 5 + spacing, base + stride * post(step), 0])

result += build_grid_beam_capped_x(default_beam_args, 5,1, 1).translate([-default_beam_args.unit * 5 - spacing, base + stride * step[0], 0])
result += build_grid_beam_capped_x(default_beam_args, 5,1, 1).translate([0, base + stride * step[0], 0])
result += build_grid_beam_capped_x(default_beam_args, 5,1, 1).translate([default_beam_args.unit* 5 + spacing, base + stride * post(step), 0])

result += build_grid_beam_capped_x(default_beam_args, 10,1, 1).translate([0, base + stride * step[0], 0])
result += build_grid_beam_capped_x(default_beam_args, 2,1, 1).translate([-default_beam_args.unit * (10/2 + 1) - spacing, base + stride * step[0], 0])
result += build_grid_beam_capped_x(default_beam_args, 2,1, 1).translate([ default_beam_args.unit * (10/2 + 1) + spacing, base + stride * step[0], 0])
post(step)

result += build_grid_beam_capped_x(default_beam_args, 9,1, 1).translate([0, base + stride * step[0], 0])
result += build_grid_beam_capped_x(default_beam_args, 2,1, 1).translate([-default_beam_args.unit * (9/2 + 1) - spacing, base + stride * step[0], 0])
result += build_grid_beam_capped_x(default_beam_args, 2,1, 1).translate([ default_beam_args.unit * (9/2 + 1) + spacing, base + stride * step[0], 0])
post(step)

result += build_grid_beam_capped_x(default_beam_args, 8,1, 1).translate([default_beam_args.unit, base + stride * step[0], 0])
result += build_grid_beam(default_beam_args, 2,1, 1).translate([-default_beam_args.unit * (8/2) - spacing, base + stride * step[0], 0])
post(step)

result += build_grid_beam_capped_x(default_beam_args, 9,1, 1).translate([0, base + stride * step[0], 0])
post(step)
#result += build_grid_beam_capped_x(default_beam_args, 7,1, 1).translate([0, base + stride * step[0], 0])
#post(step)
result += build_grid_beam_capped_x(default_beam_args, 6,1, 1).translate([0, base + stride * step[0], 0])
post(step)
#result += build_grid_beam_capped_x(default_beam_args, 5,1, 1).translate([0, base + stride * step[0], 0])
#post(step)
result += build_grid_beam(default_beam_args, 4,1, 1).translate([0, base + stride * step[0], 0])
post(step)
#result += build_grid_beam(default_beam_args, 3,1, 1).translate([0, base + stride * step[0], 0])
#post(step)
result += build_grid_beam(default_beam_args, 2,1, 1).translate([0, base + stride * step[0], 0])
post(step)

result = result.rotate([0,0,0], [0,0,1],45)
# Duplicate a mirror image on other side of the bed:
result += result.rotate([0,0,0], [0,0,1], 180)

bed = cq.Workplane("XY" ).box(300, 300, 1).translate([0, 0, -default_beam_args.half_unit - spacing])


cq.exporters.export(result, "gridbeam_bed_02.3mf")

# Visualise with the bed attached:
result += bed
cq.exporters.export(result, "gridbeam_bed_02.svg")