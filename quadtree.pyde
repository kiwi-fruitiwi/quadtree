# This is a python port of Daniel Shiffman's Coding Challenge #98.1:
# Quadtree - Part 1
#
# We're trying to build this without PVector
# 

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
        return (p.x >= self.x) and (p.x < self.x+self.w) and (p.y >= self.y) and (p.y < self.y+self.h)
                


class Quadtree():
    def __init__(self, boundary, n): # boundary is a Rectangle
        self.boundary = boundary
        
        # how big is the quadtree? when do I need to subdivide? 
        # this is a job for capacity
        self.capacity = n
        self.points = []
        self.divided = False
        
        # self.northwest = None
        # self.northeast = None
        # self.southeast = None
        # self.southwest = None


    def insert(self, p): # p is a Point
        if not self.boundary.contains(p):
            return
        
        if len(self.points) < self.capacity:
            self.points.append(p)
        else:
            if not self.divided:
                self.subdivide()
            
            self.northwest.insert(p)        
            self.northeast.insert(p)      
            self.southeast.insert(p)      
            self.southwest.insert(p)
    
    
    def __repr__(self):
        # return "I'm a quadtree with capacity {}".format(self.capacity)
        return str(self.points)
        
            
    # we will split into 4 subsections: nw, ne, sw, se
    def subdivide(self):        
        # local variables to make code more readable
        x = self.boundary.x
        y = self.boundary.y
        w = self.boundary.w
        h = self.boundary.h        
        
        nw = Rectangle(x, y, w/2, h/2)
        ne = Rectangle(x+w/2, y, w/2, h/2)
        sw = Rectangle(x, y+h/2, w/2, h/2)
        se = Rectangle(x+w/2, y+h/2, w/2, h/2)
        
        self.northwest = Quadtree(nw, self.capacity)
        self.northeast = Quadtree(ne, self.capacity)
        self.southeast = Quadtree(se, self.capacity)
        self.southwest = Quadtree(sw, self.capacity)
        
        self.divided = True
    
    
    def count(self):
        # if self.northwest exists, then all the other 3 quadrants will also exist
        # because they are only created together. love, Cody
        # oops lol, we already have a self.divided that we can use for this
        if self.divided:
            return len(self.points) + self.northwest.count() + self.northeast.count() + self.southwest.count() + self.southeast.count()
        else:
            return len(self.points)
    
    
    # return a list of points in this quadtree
    # TODO: not sure why [:] doesn't work. copy() is in Python3 only too ; ;
    def point_list(self):
            
        p = self.points[:]
        
        if self.divided:
            nw = self.northwest.point_list()[:]
            ne = self.northeast.point_list()[:]
            sw = self.southwest.point_list()[:]
            se = self.southeast.point_list()[:]
            
            return p.extend(nw.extend(ne.extend(se.extend(sw))))
        else:
            return p
    
    
    def show(self):
        stroke(0, 0, 100, 100)
        noFill()
        rect(self.boundary.x, self.boundary.y, self.boundary.w, self.boundary.h)
        
        if self.divided: # checking existence
            self.northwest.show()
            self.northeast.show()
            self.southeast.show()
            self.southwest.show()


def setup():    
    size(700, 700)
    colorMode(HSB, 360, 100, 100, 100)
    background(209, 95, 33)
    boundary = Rectangle(0, 0, width, height)
    qt = Quadtree(boundary, 4)
    points = []    
    

    strokeWeight(1)
    # the default rectMode is CORNER, which puts the first point at the top left corner
    for i in range(500):
        p = Point(random(width), random(height))
        qt.insert(p)
        
        # we can iterate through this at first to display created points
        # but! we can also use this to compare with qt's points to find bugs
        points.append(p)

    
    print qt.count()
    qt.show()
    
    # show where all of the points generated are
    strokeWeight(5)
    for p in points:
        point(p.x, p.y)
    

def draw():
    noLoop()
    # background(209, 95, 33)


    
