import cadquery as cq
import sys
import copy
import beam
from beam import *

filename_base = "gridbeam_bed_05"
spacing = default_beam_args.half_unit / 4
stride  = spacing + default_beam_args.unit
base = stride #spacing /+ default_beam_args.unit
step = [int(0)]
y = [int(0)]

def post(i):
    old = i[0]
    i[0] += 1
    return old * stride

result = cq.Workplane("XY" )
for h in range(1, 9):
    y[0] += 1
    step[0] = 0
    for i in range(1):
        result += build_grid_beam_spacer(default_beam_args, h).translate([post(step), y[0] * stride, h/2])

# Duplicate a mirror image in other three quadrants of the bed:
result += result.rotate([0,0,0], [0,0,1], 180)
result += result.rotate([0,0,0], [0,0,1], 90)
#result = result.clean()

cq.exporters.export(result, filename_base+".3mf")

# Visualise with the bed attached:
bed = cq.Workplane("XY" ).box(300, 300, 1).translate([0, 0, -default_beam_args.half_unit - spacing])
result += bed
cq.exporters.export(result, filename_base+".svg")