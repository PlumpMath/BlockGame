from direct.gui.DirectGui import *

from twisted.internet.protocol import Factory, Protocol
from twisted.internet.error import DNSLookupError

from server.main import runServer

from protocol import connect

class Menu():
    def __init__(self, parent):
        self.parent = parent
    
        self.frame = DirectFrame() # Menu Frame
        self.title = DirectLabel(
                            text="BlockGame",
                            scale=0.3,
                            pos=(0, 0, 0.4),
                            frameColor=(0,0,0,0)
                            )
        self.title.reparentTo(self.frame)
        text = "Enter address\n\
or leave blank for single-player:"
        self.label = DirectLabel(
                            text=text,
                            scale=0.075,
                            pos=(0, 0, 0.15),
                            frameColor=(0,0,0,0)
                            )
        self.label.reparentTo(self.frame)
        self.address = DirectEntry(
                            scale=0.1,
                            pos=(-0.5, 0, -0.15),
                            command=self.addressEntered
                            )
        self.address.reparentTo(self.frame)
        
        self.status = DirectLabel( # ("Connecting...", etc)
                            scale=0.1,
                            frameColor=(0,0,0,0)
                            )
        self.status.hide()
        
        self.back = DirectButton(
                            text="Back",
                            scale=0.1,
                            pos=(0, 0, -0.5)
                            )
        self.back.hide()
        
        self.hide, self.show = self.frame.hide, self.frame.show
        
    def addressEntered(self, address):
        self.frame.hide()
        if not address:
            self.status.show()
            self.status["text"] = "Starting server..."
            runServer(True)
            address = "127.0.0.1"
        self.status.show()
        self.status["text"] = "Connecting to %s..." % address
        self.parent.factory = connect(address, 54321, self.connected, 
                                        self.connectError)
        
    def connected(self, protocol):
        self.parent.protocol = protocol
        self.status["text"] = "Connected"
        
    def connectError(self, error):
        if error.trap(DNSLookupError):
            self.status["text"] = "Could not find hostname"
        else:
            self.status["text"] = str(error)
        self.back["command"] = self.backFromError
        self.back.show()
        
    def backFromError(self):
        self.status.hide()
        self.back.hide()
        self.frame.show()
