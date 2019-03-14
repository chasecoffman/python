import SpriteManager
from Sprite import Sprite

class Armored(Sprite):
    armor = 10
    
    def display(self):
        stroke(100)
        strokeWeight(self.armor)
        fill(0, 225, 0)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        noStroke()
        
    def handleCollision(self):
        self.armor -= 1
        if self.armor < 0:
            SpriteManager.destroy(self)
    
    
