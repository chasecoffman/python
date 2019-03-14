import platform
from Bullet import Bullet 
from Enemy import Enemy
from Player import Player
from SpriteManager import sprites
from raindrop import raindrop
from JiggleBot import JiggleBot
from ScreenSaverBot import ScreenSaverBot
from Armored import Armored
import SpriteManager

def setup():
    print "Built with Processing Python version " + platform.python_version()
    size(500, 500)
    
    
    player = Player(width / 2, height - 100, 1);
    SpriteManager.setPlayer(player)
    SpriteManager.spawn(Enemy(100, 100, 2))
    
    enemyTeam = 2
    
    SpriteManager.spawn(player)
    SpriteManager.spawn(Enemy(0, 0, enemyTeam))
    SpriteManager.spawn(Enemy(500, 150, enemyTeam))
                        
def draw():
    background(0)
    SpriteManager.animate()


def keyPressed():
    SpriteManager.player.keyDown()    
        
def keyReleased():
    SpriteManager.player.keyUp()
