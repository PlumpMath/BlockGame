from panda3d.core import NodePath, GeomNode, CardMaker, Point3
from panda3d.core import Texture

from copy import deepcopy

from blocks import Blocks

FACES = ["top", "bottom", "left", "right", "front", "back"]

CARDS = { # (top-left, top-right, bottom-right, bottom-left) tuples
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

CARDCOLORS = {
    "front": (1.0, 0.0, 0.0, 0.0), # red
    "back": (0.0, 1.0, 0.0, 0.0), # green
    "left": (0.0, 0.0, 1.0, 0.0), # blue
    "right": (1.0, 1.0, 0.0, 0.0), # yellow
    "top": (0.0, 1.0, 1.0, 0.0), # cyan
    "bottom": (1.0, 0.0, 1.0, 0.0) # magenta
}

def loadResources(loader):
    """
    Loads all resources and returns dictionary containing them.
    """
    res = {}
    
    res["blocktexture"] = loader.loadTexture("media/textures.png")
    res["blocktexture"].setMinfilter(Texture.FTNearest)
    res["blocktexture"].setMagfilter(Texture.FTNearest)
    
    return res

def makeCube(geom, x, y, z, scale=1.0, texpos=None, colors=False):
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
    
    mycards = deepcopy(CARDS)
    for k, i in mycards.iteritems():
        points = i
        for j in points:
            j += Point3(x, y, z)
            j *= scale
        cardmaker.setFrame(*points)
        
        if texpos:
            cardmaker.setUvRange(*texpos[k])
        if colors:
            cardmaker.setColor(*CARDCOLORS[k])
        geom.addGeomsFrom(cardmaker.generate())

def makeChunkNode(chunk, texture):
    """
    Function that creates a NodePath containing a chunk from a block array
    
    chunk: Block array
    texture: Texture map to use
    """
    geom = GeomNode("chunk")
    for x in range(16):
        for y in range(16):
            for z in range(16):
                btype = chunk[x][y][z]
                if not btype in Blocks:
                    btype = 2 # Unknown
                if Blocks[btype]["visible"]:
                    makeCube(geom, float(x), float(y), float(z), 
                             texpos=Blocks[btype]["texcoords"])
    chunk = NodePath(geom)
    chunk.setTexture(texture)
    chunk.flattenStrong()
    return chunk
