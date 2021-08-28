class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 8
    
    
    def move(self):
        self.x += random(-1, 1)
        self.y += random(-1, 1)
    
    
    def render(self):
        noStroke()
        fill(0, 0, 100)
        circle(self.x, self.y, self.r)
        
                

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return "({},{})".format(self.x, self.y)
        

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        print(self)
    
    # test if this contains a point
    def contains(self, p):
        # we're using the same inclusion as python's range: [a, b)
        # this makes it so the center of each quadtree isn't shared
        # but is also guaranteed to belong to the se boundary
        # the above is no longer true
        
        # BUG currently inserting points at (width, height) only inserts 1/4 of the time
        # resolved! this was because of integer division during subdivide
        return (p.x >= self.x) and (p.x <= self.x+self.w) and (p.y >= self.y) and (p.y <= self.y+self.h)


    # do we intersects with another rectangle?
    def intersects(self, target):
        # there are eight cases for intersection; we can reduce the computation time by 
        # finding the four cases that fail intersection and taking a logical NOT
        return not (
                (self.x > target.x + target.w) or 
                (self.y > target.y + target.h) or 
                (target.x > self.x + self.w) or 
                (target.y > self.y + self.h))
    
    
    def __repr__(self):
        s = "I am a rectangle at point {},{} with width {} and height {}"
        return s.format(self.x, self.y, self.w, self.h)        
