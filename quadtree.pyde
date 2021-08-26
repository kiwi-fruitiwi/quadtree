# This is a python port of Daniel Shiffman's Coding Challenge #98.1:
# Quadtree - Part 1
#
# We're trying to build this without PVector
# 
# BUG: why does it not count bottom left points in each boundary? rounding error?
#          this was an integer division error in subdivide when we take w/2 instead of w/2.0
# BUG: another problem was drawing points off screen with the mouse
#          fixed!


from primitives import Rectangle, Point
from Quadtree import Quadtree


def setup():
    global qt, points
          
    size(600, 600)
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
    
    for i in range(10000):
        x = randomGaussian() * (width * 0.2) + width/2
        y = randomGaussian() * (height * 0.2) + height/2
        
        x = constrain(x, 0, width)
        y = constrain(y, 0, height)
        
        p = Point(x, y)
        points.append(p)
        qt.insert(p)
    
    print("Finished setup")
        
        
def draw():
    global qt, points
    
    background(209, 95, 33)
    strokeWeight(1)
    qt.show()
    
    # show where all of the points generated are
    strokeWeight(5)
    # for p in points:
    #     point(p.x, p.y)
    
    text("{} out of {}".format(qt.count(), len(points)), 30, 30)


def add_point_at_mouse():
    global qt, points
    p = Point(mouseX, mouseY)
    r = Rectangle(0,0, width, height)
    
    # we don't want to add any points outside of the canvas when we drag our mouse offscreen
    if r.contains(p):
        points.append(p)
        qt.insert(p)
    

def mouseDragged():
    global qt, points
    add_point_at_mouse()
    

def mouseWheel(event):
    print event    
    add_point_at_mouse()
    
def keyPressed():
    global qt, points
    
    # testing
    if key == 'a':
        p = Point(0, height)
        points.append(p)
        qt.insert(p)
