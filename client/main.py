from math import pi, sin, cos
 
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import NodePath, GeomNode, Point2, Texture

from cube import MakeCube

from random import randint

from threading import Thread

from twisted.internet.task import LoopingCall
from twisted.internet import reactor

def makeChunk(tex, x, y, z):
    geom = GeomNode("fletgresschenk")
    texpos = {
        "front": (Point2(0, 0), Point2(1.0, 1.0)),
        "back": (Point2(0, 0), Point2(1.0, 1.0)),
        "left": (Point2(0, 0), Point2(1.0, 1.0)),
        "right": (Point2(0, 0), Point2(1.0, 1.0)),
        "top": (Point2(0, 0), Point2(0.2, 0.2)),
        "bottom": (Point2(0.0, 0.9), Point2(1.0, 1.0))
    }
    for i in range(8):
        for j in range(8):
            for k in range(8):
                if randint(0,5) < 5:
                    MakeCube(geom, float(x+i), float(y+j), float(z+k), texpos=texpos)
    chunk = NodePath(geom)
    chunk.setTexture(tex)
    chunk.flattenStrong()
    return chunk

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.setFrameRateMeter(True)

        tex = self.loader.loadTexture("media/grass.png")
        tex.setMagfilter(Texture.FTNearest)
        self.chunk = makeChunk(tex, 0, 0, 0)
        self.chunk.reparentTo(self.render)
 
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
 
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont
 
app = MyApp()
LoopingCall(app.taskMgr.step).start(1 / 60)
reactor.run()
