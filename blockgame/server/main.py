from twisted.internet import reactor
from server.factory import BlockGameServerFactory

def runServer(local):
    factory = BlockGameServerFactory(local)
    reactor.listenTCP(factory.port, factory)

if __name__ == "__main__":
    runServer(False)
