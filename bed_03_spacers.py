import cadquery as cq
import sys
import copy
import beam
from beam import *

filename_base = "gridbeam_bed_03"

def post(i):
    old = i[0]
    i[0] += 1
    return old

def build_row(result):
    result  += build_grid_beam_only_vertical(default_beam_args, 1, 1, 1).translate([stride * 1, 0, 0])
    result  += build_grid_beam_only_vertical(default_beam_args, 1, 1, 1).translate([stride * 2, 0, 0])
    result  += build_grid_beam_only_vertical(default_beam_args, 1, 1, 1).translate([stride * 3, 0, 0])
    result  += build_grid_beam_only_vertical(default_beam_args, 1, 1, 1).translate([stride * 4, 0, 0])
    result  += build_grid_beam_only_vertical(default_beam_args, 1, 1, 1).translate([stride * 5, 0, 0])
    result = result.translate([0, stride, 0])
    return result

spacing = default_beam_args.half_unit / 4
stride  = spacing + default_beam_args.unit
base = stride #spacing /+ default_beam_args.unit
step = [int(0)]

result   = build_row(cq.Workplane("XY"))
result  += build_row(result)
result  += build_row(result)
result  += build_row(result)
result  += build_row(result)

cq.exporters.export(result, filename_base + ".3mf")

# Visualise with the bed attached:
bed = cq.Workplane("XY" ).box(300, 300, 1).translate([0, 0, -default_beam_args.half_unit - spacing])
result += bed
cq.exporters.export(result, filename_base + ".svg")