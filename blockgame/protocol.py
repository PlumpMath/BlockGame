from twisted.internet import reactor
from twisted.internet.protocol import Factory, Protocol
from twisted.internet.endpoints import TCP4ClientEndpoint

class BlockGameClientProtocol(Protocol):
    pass

def connect(address, port, callback, errback):
    factory = Factory()
    factory.protocol = BlockGameClientProtocol
    point = TCP4ClientEndpoint(reactor, address, port)
    d = point.connect(factory)
    d.addCallback(callback)
    d.addErrback(errback)
    return factory
