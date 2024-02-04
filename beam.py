import cadquery as cq
import sys

class BeamArgs:
    def __init__(self):
        self.unit = 10 # 10mm fundamental unit on which whole grid is based.
        self.half_unit = self.unit / 2.0
        self.corner_rounding_outer = 0.5
        self.bolt_shaft_diameter = 5.01 # The hardware tends to have 4.9xmm diameter so don't need much slop added.
default_beam_args = BeamArgs()

# a small number, e.g. to add or subtract from x.
def relative_epsilon(x):
    return x / 65536

# Build a solid beam, great for calibrating shrinkage and warparge from grid beam structures:
def build_beam(args, length = 2, width = 1, height = 1): # BeamArgs
    result = cq.Workplane("XY" ).box(args.unit * width, args.unit * length, args.unit * height)
    # Round the four vertical edges:
    result = result.edges("|Z").fillet(args.corner_rounding_outer)
    # Chamfer the eight original horizontal edges and the eight curved sections at the corners:
    result = result.faces(">Z or <Z").chamfer(args.corner_rounding_outer - relative_epsilon(args.corner_rounding_outer))
    return result

# Build 
def build_grid_beam(args, length = 2, width = 1, height = 1): # BeamArgs
    result = cq.Workplane("XY" ).box(args.unit * width, args.unit * length, args.unit * height)
    
    # Bore out the bolt penerations along the x-axis:
    result = result.faces("<X").workplane()
    # result = yz_plane.cskHole(args.bolt_shaft_diameter, 9.9, 120.0, depth=200, )
    result = result.center(-length * args.unit / 2 + args.half_unit, -height * args.unit / 2 + args.half_unit)
    result = result .hole(args.bolt_shaft_diameter)
    for z in range(height):
        z_coord = args.half_unit + z * args.unit
        for y in range(length):
            y_coord = args.half_unit + y * args.unit
            #result = result.center(y_coord, z_coord)
            #result = result.hole(args.bolt_shaft_diameter)
            #result = result.cskHole(args.bolt_shaft_diameter, 9.9, 120.0, depth=200, )
            #result = yz_plane.hole(args.bolt_shaft_diameter)
            pass
    
    # Round the four corner vertical edges:
    result = result.edges(">(-1,-1,0) or >(1,-1,0) or >(-1,1,0) or >(1,1,0)").fillet(args.corner_rounding_outer)
    # Chamfer the eight original horizontal edges and the eight curved sections at the corners:
    # (note the originals might have been chopped up by now so we need to select the fragments of them)
    result = result.edges(">(-1,0,-1) or >(1,0,-1) or >(0,-1,-1) or >(0,1,-1) or >(-1,0,1) or >(1,0,1) or >(0,-1,1) or >(0,1,1)").chamfer(args.corner_rounding_outer - relative_epsilon(args.corner_rounding_outer))
    return result

#if __name__ != '__main__':
print(sys.stderr, __name__)
result = build_beam(default_beam_args) + build_grid_beam(default_beam_args, 3, 3, 3).translate([10*9, 0, 0])