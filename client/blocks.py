from panda3d.core import Point2

FACES = ["top", "bottom", "left", "right", "front", "back"]

TILE = 1.0/16 # Size of a 1tile in a 16x16 texture map

def allFacesSame(texpos):
    """
    Helper function, makes list of faces all with same coordinates.
    """
    r = {}
    for i in FACES:
        r[i] = texpos
    return r
    
def tile(x, y):
    """
    Helper function, finds coordinates of a tile in a 16x16 texture map.
    """
    return (Point2(x * TILE, 1-((y+1) * TILE)), Point2((x+1) * TILE, 1-(y * TILE)))

# List of block types
# Each entry is a tuple of (visible, texcoords)
# visible is a bool as to whether to render or not
# texcoords is a list of texture coordinates for faces, see MakeCube in cube.py
Blocks = {
    0: { # Air
        "visible": False
    },
    1: { # Blue platform thing
        "visible": True,
        "texcoords": allFacesSame(tile(0,0))
    },
    2: { # Unknown block type (? block)
        "visible": True,
        "texcoords": allFacesSame(tile(1,0))
    }
}
