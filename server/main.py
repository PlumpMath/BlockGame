from twisted.internet import protocol, reactor

class BlockGameProtocol(protocol.Protocol):
    pass

class BlockGameFactory(protocol.ServerFactory):
    protocol = BlockGameProtocol

reactor.listenTCP(54321, BlockGameFactory())
reactor.run()
