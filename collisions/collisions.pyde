# Kiwi, 2021.08.28
# Quadtree collisions with Daniel Shiffman of the Coding Train
# Coding Challenge #98.3: Quadtree Collisions - Part 3
# https://www.youtube.com/watch?v=z0YFFg_nBjw
# translation to Python

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 4
        self.c = color(0, 0, 50)
    
    
    def move(self):
        self.x += random(-1, 1)
        self.y += random(-1, 1)
    
    
    def render(self):
        noStroke()
        fill(self.c)
        circle(self.x, self.y, self.r*2)
       
         
    def intersects(self, other):
        # check if distance is less than sum of the radii
        distance = dist(self.x, self.y, other.x, other.y)
        if distance < self.r + other.r:
            return True
        else:
            return False   
    
        
def setup():
    global particles
    
    frameRate(144)
    colorMode(HSB, 360, 100, 100, 100)
    size(600, 400)
    particles = []
    
    # populate particles
    for i in range(1000):
        particles.append(Particle(random(width), random(height)))
        
    
def draw():
    global particles
    
    background(209, 95, 33)
        
    # check if particles collide
    for p in particles:
        for other in particles:
            if p != other:
                if p.intersects(other):
                    p.c = color(0, 0, 100)
    
    for p in particles:
        p.move()
        p.render()
        
        # reset the color
        p.c = color(0, 0, 50)
