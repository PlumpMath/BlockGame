from math import pi, sin, cos
 
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import NodePath, GeomNode, Point2, TextNode

from twisted.internet import reactor

from numpy import zeros

from render import loadResources, makeChunkNode

from menu import Menu

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
        
        self.factory = None
        self.protcol = None
        
        self.menu = Menu(self)
        
    def userExit(self):
        reactor.stop()

    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        #self.camera.setPos(5 * sin(angleRadians), -5.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees*10, 0, 0)
        return Task.cont
