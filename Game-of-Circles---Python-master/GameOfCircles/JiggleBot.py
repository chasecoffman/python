from Sprite import Sprite

class JiggleBot(Sprite):
    
    speed = 4
    diameter = 75
    c = color(100, 100, 255)
        
    def move(self):
        self.y += random(-self.speed, self.speed)
        self.x += random(-self.speed, self.speed)
        self.x = constrain(self.x, 0, width)
        self.x = constrain(self.y, 0, height)
