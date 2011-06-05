from math import pi, sin, cos
 
from direct.showbase.ShowBase import ShowBase
from direct.task import Task

from panda3d.core import NodePath, GeomNode, Point2

from cube import MakeCube

from random import randint

def fletgress(tex):
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
                    MakeCube(geom, float(i), float(j), float(k), texpos=texpos)
    chunk = NodePath(geom)
    chunk.setTexture(tex)
    return chunk

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        chunk = fletgress(self.loader.loadTexture("media/grass.png"))
        chunk.reparentTo(self.render)
        
        #self.cube.setScale(0.25, 0.25, 0.25)
        
        #self.cube.setPos(-8, 42, 0)
        #self.cube.setPos(0, 20, 0)
        #self.cube.setPos(0, 0, 0)
 
        #self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
 
    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont
 
app = MyApp()
app.run()
