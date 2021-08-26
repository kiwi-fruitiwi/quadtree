class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return "({},{})".format(self.x, self.y)
        

class Rectangle():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    # test if this contains a point
    def contains(self, p):
        # we're using the same inclusion as python's range: [a, b)
        # this makes it so the center of each quadtree isn't shared
        # but is also guaranteed to belong to the se boundary
        # the above is no longer true
        
        
        return (p.x >= self.x) and (p.x <= self.x+self.w) and (p.y >= self.y) and (p.y <= self.y+self.h)            
