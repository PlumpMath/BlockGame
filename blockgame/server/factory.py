from twisted.internet.protocol import Factory

from server.protocol import BlockGameServerProtocol

class BlockGameServerFactory(Factory):
    protocol = BlockGameServerProtocol
    port = 54321
    
    def __init__(self, local):
        pass
