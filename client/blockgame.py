from math import pi, sin, cos
 
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.gui.DirectGui import *
from panda3d.core import NodePath, GeomNode, Point2, TextNode

from numpy import zeros

from render import loadResources, makeChunkNode

class BlockGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.setFrameRateMeter(True)

        self.res = loadResources(self.loader)
        self.chunks = {} # Dictionary of (array, nodepath) tuples
        
        chunk = zeros((16,16,16))
        for i in range(5):
            for j in range(5):
                chunk[5+i][5+j][7] = 1 # Make platform
        chunk[0][0][0] = 77
        chunk[15][15][15] = 35
        self.chunks["test"] = makeChunkNode(chunk, self.res["blocktexture"])
        self.chunks["test"].reparentTo(self.render)
        
        self.chunks["test"].setPos(-8,-6,-9)
 
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        
        self.makeMenu()
        
    def addressEntered(self, address):
        self.menuFrame.hide()
        if address:
            self.menuStatus.show()
            self.menuStatus["text"] = "Connecting to %s..." % address
        else:
            self.menuStatus.show()
            self.menuStatus["text"] = "Loading server list..."
        
    def makeMenu(self):
        self.menuFrame = DirectFrame() # Menu Frame
        self.menuTitle = DirectLabel(
                            text="BlockGame",
                            scale=0.3,
                            pos=(0, 0, 0.4),
                            frameColor=(0,0,0,0)
                            )
        self.menuTitle.reparentTo(self.menuFrame)
        text = "Enter address or leave blank for server list:"
        self.menuLabel = DirectLabel(
                            text=text,
                            scale=0.075,
                            pos=(0, 0, 0.15),
                            frameColor=(0,0,0,0)
                            )
        self.menuLabel.reparentTo(self.menuFrame)
        self.menuAddress = DirectEntry(
                            scale=0.1,
                            pos=(-0.5, 0, -0.15),
                            command=self.addressEntered
                            )
        self.menuAddress.reparentTo(self.menuFrame)
        self.menuStatus = DirectLabel( # ("Connecting...")
                            scale=0.1,
                            frameColor=(0,0,0,0)
                            )
        self.menuStatus.hide()

    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        #self.camera.setPos(5 * sin(angleRadians), -5.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees*10, 0, 0)
        return Task.cont
