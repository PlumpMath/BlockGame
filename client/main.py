from twisted.internet.task import LoopingCall
from twisted.internet import reactor

from blockgame import BlockGame

import sys

def step():
    """
    Helper function to kill app when Panda goes wrong
    """
    try:
        game.taskMgr.step()
    except Exception as e:
        reactor.stop()

game = BlockGame()
LoopingCall(step).start(1/60)
try:
    reactor.run()
except KeyboardInterrupt:
    reactor.stop()
