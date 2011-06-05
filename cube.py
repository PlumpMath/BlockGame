from panda3d.core import CardMaker, NodePath, GeomNode, Point3
from copy import deepcopy

cards = { # (top-left, top-right, bottom-right, bottom-left) tuples
    "front": (
      Point3(0.0, 0.0, 0.0),
      Point3(1.0, 0.0, 0.0),
      Point3(1.0, 0.0, 1.0),
      Point3(0.0, 0.0, 1.0)
    ),
    "back": (
      Point3(1.0, 1.0, 0.0),
      Point3(0.0, 1.0, 0.0),
      Point3(0.0, 1.0, 1.0),
      Point3(1.0, 1.0, 1.0)
    ),
    "left": (
      Point3(0.0, 1.0, 0.0),
      Point3(0.0, 0.0, 0.0),
      Point3(0.0, 0.0, 1.0),
      Point3(0.0, 1.0, 1.0)
    ),
    "right": (
      Point3(1.0, 0.0, 0.0),
      Point3(1.0, 1.0, 0.0),
      Point3(1.0, 1.0, 1.0),
      Point3(1.0, 0.0, 1.0)
    ),
    "top": (
      Point3(1.0, 0.0, 0.0),
      Point3(0.0, 0.0, 0.0),
      Point3(0.0, 1.0, 0.0),
      Point3(1.0, 1.0, 0.0)
    ),
    "bottom": (
      Point3(0.0, 0.0, 1.0),
      Point3(1.0, 0.0, 1.0),
      Point3(1.0, 1.0, 1.0),
      Point3(0.0, 1.0, 1.0)
    )
}

cardcolors = {
    "front": (1.0, 0.0, 0.0, 0.0), # red
    "back": (0.0, 1.0, 0.0, 0.0), # green
    "left": (0.0, 0.0, 1.0, 0.0), # blue
    "right": (1.0, 1.0, 0.0, 0.0), # yellow
    "top": (0.0, 1.0, 1.0, 0.0), # cyan
    "bottom": (1.0, 0.0, 1.0, 0.0) # magenta
}

def MakeCube(geom, x, y, z, scale=1.0, texpos=None, colors=False):
    """
    Function that adds six cards to a GeomNode to form a cube
    
    geom: GeomNode to add cards to
    x, y, z: Position offset
    scale: Optional, Scale factor, cube is 1x1x1 by default
    texpos: Optional, Dictionary of tuples with texture co-ordinates
            Tuple has Point2 for top-left and Point2 for bottom-right
            Faces are "front", "back", "left", "right", "top", "bottom"
    colors: Optional, if True set different color for each face for debugging
            (see cardcolors)
    """
    cardmaker = CardMaker("cardmaker")
    
    mycards = deepcopy(cards)
    for k, i in mycards.iteritems():
        points = i
        for j in points:
            j += Point3(x, y, z)
            j *= scale
        cardmaker.setFrame(*points)
        
        if texpos:
            cardmaker.setUvRange(*texpos[k])
        if colors:
            cardmaker.setColor(*cardcolors[k])
        geom.addGeomsFrom(cardmaker.generate())
