# This is a python port of Daniel Shiffman's Coding Challenge #98.1:
# Quadtree - Part 1
#
# We're trying to build this without PVector
# 
# BUGS: why does it not count bottom left points in each boundary?
# is this a rounding error?


from primitives import Rectangle, Point
from Quadtree import Quadtree


def setup():
    global qt, points
          
    size(700, 700)
    colorMode(HSB, 360, 100, 100, 100)
    background(209, 95, 33)
    boundary = Rectangle(0, 0, width, height)
    qt = Quadtree(boundary, 4)
    points = []    
    
    
    strokeWeight(1)
    # # the default rectMode is CORNER, which puts the first point at the top left corner
    # for i in range(500):
    #     p = Point(random(width), random(height))
    #     qt.insert(p)
        
    #     # we can iterate through this at first to display created points
    #     # but! we can also use this to compare with qt's points to find bugs
    #     points.append(p)
    
    for i in range(50):
        points.append(Point(width/2, height/2))
        
        
def draw():
    global qt, points
    
    background(209, 95, 33)
    strokeWeight(1)
    qt.show()
    
    # show where all of the points generated are
    strokeWeight(5)
    for p in points:
        point(p.x, p.y)
    
    text("{} out of {}".format(qt.count(), len(points)), 30, 30)


def mouseDragged():
    global qt, points
    
    p = Point(mouseX, mouseY)
    points.append(p)
    qt.insert(p)
    print p
    

def mouseWheel(event):
    print event
    
    p = Point(mouseX, mouseY)
    points.append(p)
    qt.insert(p)
