import cadquery as cq
import sys
import copy

class BeamArgs:
    def __init__(self):
        self.unit = 10 # 10mm fundamental unit on which whole grid is based.
        self.half_unit = self.unit / 2.0
        self.corner_rounding_outer = 0.5
        self.bolt_shaft_diameter = 5.01 # The hardware tends to have 4.9xmm diameter so don't need much slop added.
        self.bolt_contersink_diameter = self.bolt_shaft_diameter + 0.5
        self.bolt_contersink_angle = 45 # Conutersink chamfers the lip of all holes slightly, It isn't to mate with sloped hardware
        self.bolt_bore_diameter = self.unit * 0.8
        self.bolt_bore_depth = 1.0
        
default_beam_args = BeamArgs()

# a small number, e.g. to add or subtract from x.
def relative_epsilon(x):
    return x / 65536

def round_beam(args, beam):
    """Round the external edges of an already-built beam.
    
    Args:
        args (BeamArgs): The common parameters to a whole class of generated beams
        like external dimensions and bore diameters which make generated models compatible.
        beam (Workplane) The beam.
    Returns:
        Workplane representing the constructed beam.
    """

    # Round the four vertical edges:
    result = beam.edges("|Z").fillet(args.corner_rounding_outer)
    # Chamfer the eight original horizontal edges and the eight curved sections at the corners:
    # Chamfers the bore hole too: result = result.faces(">Z or <Z").chamfer(args.corner_rounding_outer - relative_epsilon(args.corner_rounding_outer))
    # Pick out one edge on top and one on bottom and the chamfer propagates around the perimeters:
    result = result.edges("(>Z and >X) or (<Z and >X)").chamfer(args.corner_rounding_outer - relative_epsilon(args.corner_rounding_outer))
    return result

def build_beam(args, width = 1, length = 2, height = 1):
    """Build a solid beam, great for calibrating shrinkage and warparge from grid beam structures.
    
    These beams lack surface details like bores which might throw out your calipers.
    
    Args:
        args (BeamArgs): The common parameters to a whole class of generated beams
        like external dimensions and bore diameters which make generated models compatible.
        width  (int) X-axis dimension of beam in multiples of the fundamental unit cube.
        length (int) Y-axis dimension of beam in multiples of the fundamental unit cube.
        height (int) Z-axis dimension of beam in multiples of the fundamental unit cube.
    Returns:
        Workplace representing the constructed beam.
    """
    result = cq.Workplane("XY" ).box(args.unit * width, args.unit * length, args.unit * height)
    result = round_beam(args, result)
    result = result.clean()
    return result

def build_grid_beam_v1(args, width = 1, length = 2, height = 1): # BeamArgs
    """Build a beam with holes, suitable for 3D Printing.
    
    Args:
        args (BeamArgs): The common parameters to a whole class of generated beams
        like external dimensions and bore diameters which make generated models compatible.
        width  (int) X-axis dimension of beam in multiples of the fundamental unit cube.
        length (int) Y-axis dimension of beam in multiples of the fundamental unit cube.
        height (int) Z-axis dimension of beam in multiples of the fundamental unit cube.
    Returns:
        Workplace representing the constructed beam.
    """
    result = cq.Workplane("XY" ).box(args.unit * width, args.unit * length, args.unit * height)
    
    # Bore out the bolt penerations:
    result = result.faces("<X").workplane()
    result = result.rarray(args.unit, args.unit, length, height).cskHole(args.bolt_shaft_diameter, args.bolt_contersink_diameter, args.bolt_contersink_angle)
    result = result.faces(">X").workplane()
    result = result.rarray(args.unit, args.unit, length, height).cskHole(args.bolt_shaft_diameter, args.bolt_contersink_diameter, args.bolt_contersink_angle)
    
    result = result.faces(">Y").workplane().center(width*args.half_unit, 0)
    result = result.rarray(args.unit, args.unit, width, height).cskHole(args.bolt_shaft_diameter, args.bolt_contersink_diameter, args.bolt_contersink_angle)
    result = result.faces("<Y").workplane()#.center(width*args.half_unit, 0)
    result = result.rarray(args.unit, args.unit, width, height).cskHole(args.bolt_shaft_diameter, args.bolt_contersink_diameter, args.bolt_contersink_angle)
    
    result = result.faces("<Z").workplane().center(0, -length * args.half_unit)
    result = result.rarray(args.unit, args.unit, width, length).cskHole(args.bolt_shaft_diameter, args.bolt_contersink_diameter, args.bolt_contersink_angle)
    result = result.faces(">Z").workplane()#.center(0, -length * args.half_unit)
    result = result.rarray(args.unit, args.unit, width, length).cskHole(args.bolt_shaft_diameter, args.bolt_contersink_diameter, args.bolt_contersink_angle)

    result = round_beam(args, result)
    result = result.clean()

    return result

def build_grid_beam_bored(args, width = 1, length = 2, height = 1): # BeamArgs
    """Build a beam with boreholes for attaching metal hardware, suitable for 3D Printing.
    
    Args:
        args (BeamArgs): The common parameters to a whole class of generated beams
        like external dimensions and bore diameters which make generated models compatible.
        width  (int) X-axis dimension of beam in multiples of the fundamental unit cube.
        length (int) Y-axis dimension of beam in multiples of the fundamental unit cube.
        height (int) Z-axis dimension of beam in multiples of the fundamental unit cube.
    Returns:
        Workplace representing the constructed beam.
    """
    result = cq.Workplane("XY" ).box(args.unit * width, args.unit * length, args.unit * height)
    
    # Bore out the bolt penerations:
    result = result.faces("<X").workplane()
    result = result.rarray(args.unit, args.unit, length, height).cboreHole(args.bolt_shaft_diameter, args.bolt_bore_diameter, args.bolt_bore_depth)
    result = result.faces(">X").workplane()
    result = result.rarray(args.unit, args.unit, length, height).hole(args.bolt_bore_diameter, args.bolt_bore_depth)
    
    result = result.faces(">Y").workplane().center(width*args.half_unit, 0)
    result = result.rarray(args.unit, args.unit, width, height).cboreHole(args.bolt_shaft_diameter, args.bolt_bore_diameter, args.bolt_bore_depth)
    result = result.faces("<Y").workplane()#.center(width*args.half_unit, 0)
    result = result.rarray(args.unit, args.unit, width, height).hole(args.bolt_bore_diameter, args.bolt_bore_depth)
    
    result = result.faces("<Z").workplane().center(0, -length * args.half_unit)
    result = result.rarray(args.unit, args.unit, width, length).cboreHole(args.bolt_shaft_diameter, args.bolt_bore_diameter, args.bolt_bore_depth)
    result = result.faces(">Z").workplane()#.center(0, -length * args.half_unit)
    result = result.rarray(args.unit, args.unit, width, length).hole(args.bolt_bore_diameter, args.bolt_bore_depth)

    result = round_beam(args, result)
    result = result.clean()

    return result

def drill_grid_beam(args, context, perpendicular_axis = "X", width = 1, height = 1): # BeamArgs
    """Fill one side of a beam with holes, through to the opposite face.
       WIP ... doesn't work for every axis.
    """
    context = context.faces(">"+perpendicular_axis).workplane()
    context = context.rarray(args.unit, args.unit, width, height).hole(args.bolt_shaft_diameter)
    return context

def build_grid_beam(args, width = 1, length = 2, height = 1): # BeamArgs
    """Build a beam with holes, suitable for 3D Printing.
    
    Args:
        args (BeamArgs): The common parameters to a whole class of generated beams
        like external dimensions and bore diameters which make generated models compatible.
        width  (int): X-axis dimension of beam in multiples of the fundamental unit cube.
        length (int): Y-axis dimension of beam in multiples of the fundamental unit cube.
        height (int): Z-axis dimension of beam in multiples of the fundamental unit cube.
        drill_x (bool): If False, the X-axis won't have holes through, so the part will
        be much more solid than otherwise.
    Returns:
        Workplace representing the constructed beam.
    """
    result = cq.Workplane("XY" ).box(args.unit * width, args.unit * length, args.unit * height)
    raw_box = result
    
    # Bore out the bolt penerations with simple, non-chamfered holes:
    result = result.faces(">X").workplane()
    result = result.rarray(args.unit, args.unit, length, height).hole(args.bolt_shaft_diameter)

    result = result.faces(">Y").workplane().center(width*args.half_unit, 0)
    result = result.rarray(args.unit, args.unit, width, height).hole(args.bolt_shaft_diameter)

    result = result.faces(">Z").workplane().center(0, -length * args.half_unit)
    result = result.rarray(args.unit, args.unit, width, length).hole(args.bolt_shaft_diameter)

    result = round_beam(args, result)
    result = result.clean()

    return result

def build_grid_beam_capped_x(args, width = 1, length = 2, height = 1): # BeamArgs
    """Build a beam with holes, suitable for 3D Printing but without holes parallel to the x-axis.
    
    Args:
        args (BeamArgs): The common parameters to a whole class of generated beams
        like external dimensions and bore diameters which make generated models compatible.
        width  (int): X-axis dimension of beam in multiples of the fundamental unit cube.
        length (int): Y-axis dimension of beam in multiples of the fundamental unit cube.
        height (int): Z-axis dimension of beam in multiples of the fundamental unit cube.
    Returns:
        Workplace representing the constructed beam.
    """
    result = cq.Workplane("XY" ).box(args.unit * width, args.unit * length, args.unit * height)
    raw_box = result
    
    # Bore out the bolt penerations with simple, non-chamfered holes:
    result = result.faces(">Y").workplane()#.center(width*args.half_unit, 0)
    result = result.rarray(args.unit, args.unit, width, height).hole(args.bolt_shaft_diameter)

    result = result.faces(">Z").workplane().center(0, -length * args.half_unit)
    result = result.rarray(args.unit, args.unit, width, length).hole(args.bolt_shaft_diameter)

    result = round_beam(args, result)
    result = result.clean()

    return result

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
result  = build_grid_beam(default_beam_args, 10,1)
result += build_grid_beam_capped_x(default_beam_args, 10,1, 1).translate([0, default_beam_args.half_unit * 3, 0])
#cq.exporters.export(result, "gridbeam_test_01.step")
cq.exporters.export(result, "gridbeam_test_01.svg")
#cq.exporters.export(result, "gridbeam_test_01.stl")
#cq.exporters.export(result, "gridbeam_test_01.3mf")
cq.exporters.export(result, "gridbeam_test_01.1x10.3mf")
