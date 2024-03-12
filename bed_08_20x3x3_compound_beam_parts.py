import cadquery as cq
import sys
import copy
import beam
from beam import *

filename_base = "gridbeam_bed_09_20x3x3_compound_beam_parts"

spacing = default_beam_args.half_unit / 4
stride  = spacing + default_beam_args.unit
base = stride + stride / 2 #spacing /+ default_beam_args.unit
step = [int(0)]
y = [int(0)]

def post(i):
    old = i[0]
    i[0] += 1
    return old * stride

result  = build_grid_beam_capped_x(default_beam_args, 20,1, 1).translate([0, stride / 2, 0])
result += build_grid_beam_capped_x(default_beam_args, 20,1, 1).translate([0, base + post(step), 0])
result += build_grid_beam_capped_x(default_beam_args, 20,1, 1).translate([0, base + post(step), 0])
result += build_grid_beam_capped_x(default_beam_args, 20,1, 1).translate([0, base + post(step), 0])
result += build_grid_beam_capped_x(default_beam_args, 3,1, 1).translate([0, base + post(step), 0])
result += build_grid_beam_capped_x(default_beam_args, 3,1, 1).translate([0, base + post(step), 0])
result += build_grid_beam_capped_x(default_beam_args, 3,1, 1).translate([0, base + post(step), 0])
result += build_grid_beam_capped_x(default_beam_args, 3,1, 1).translate([0, base + post(step), 0])

#post(step)
#post(step)
#result += build_grid_beam_only_vertical(default_beam_args, 4,4, 1).translate([0, base + post(step), 0])
#result = result.rotate([0,0,0], [0,0,1],45)

#singles = cq.Workplane("XY" )
for h in range(1, 9):
    y[0] += 1
    step[0] = 0
    for i in range(2):
        #singles += build_grid_beam_only_vertical(default_beam_args, 1, 1, 1).translate([default_beam_args.half_unit + spacing + post(step), y[0] * stride, 0])
        pass
#singles = singles.rotate([0,0,0], [0,0,1],-45)
#result += singles

#result += result.rotate([0,0,0], [0,0,1], 180)
#result += result.rotate([0,0,0], [0,0,1], 90)

#result = result.clean()

cq.exporters.export(result, filename_base+".3mf")

# Visualise with the bed attached:
bed = cq.Workplane("XY" ).box(300, 300, 1).translate([0, 0, -default_beam_args.half_unit - spacing])
result += bed
cq.exporters.export(result, filename_base+".svg")