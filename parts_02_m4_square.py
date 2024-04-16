# Parts with m4 counterbored holes suitable for m3 furniture sleeve bolts.
import cadquery as cq
import sys
import copy
import beam
from beam import *

filename_base = "gridbeam_parts_02_m4_no_x_"
beam_args = copy.deepcopy(default_beam_args)
beam_args.corner_rounding_outer = 0.25
beam_args.bolt_shaft_diameter = 4.0 # Dial this for innacurate printing..
beam_args.bolt_bore_diameter = 999
beam_args.bolt_bore_depth = 200

def int_to_3ds(number):
    """
    Converts a positive integer into a three-digit string padded with leading zeros if necessary.
    
    Args:
    number (int): The positive integer to be converted.
    
    Returns:
    str: The three-digit string representation of the number padded with leading zeros.
    """
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a positive integer")

    return f"{number:03d}"

def build_beam(x, y, z):
    result  = build_grid_beam_capped_x(beam_args, x, y, z)
    result = result.clean()
    filename = filename_base  + int_to_3ds(x) + "x"+ int_to_3ds(y) + "x" + int_to_3ds(z)
    cq.exporters.export(result, filename + ".step")
    cq.exporters.export(result, filename +".svg")
    return result

result = build_beam(3, 1, 1)