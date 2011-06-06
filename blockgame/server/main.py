from twisted.internet import protocol, reactor

class BlockGameProtocol(protocol.Protocol):
    pass

class BlockGameFactory(protocol.ServerFactory):
    protocol = BlockGameProtocol

def runServer():
    reactor.listenTCP(54321, BlockGameFactory())
    reactor.run()

if __name__ == "__main__":
    runServer()
