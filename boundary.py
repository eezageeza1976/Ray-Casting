#boundary class
import pygame as pg
import consts
import vector
from vector import Vector2D

############################################################
#Boundary class used for creating 'walls' or screen boundary
#arguments: Screen - Surface to be used when drawing
#           x1, x1 - Boundary start positon
#           x2, y2 - Boundary end position
#
############################################################
class Boundary:
    def __init__(self, screen, x1, y1, x2, y2):
        self.screen = screen
        self.a = Vector2D(x1, y1)
        self.b = Vector2D(x2, y2)



#Used to draw the boundary using it's own vectors
    def draw(self):
        pg.draw.aaline(self.screen, consts.GREEN, (self.a.x, self.a.y), (self.b.x, self.b.y))
 
 

############################################################
#Ray class used for creating the rays coming from the source particle
#constructor: pos - Starting position of ray
#             angle - Direction of the ray given as an angle in RADIANS
#
############################################################        
class Ray:
    def __init__(self, pos, angle):
        self.pos = pos
        self.dir = vector.from_angle(angle)

#Not used in this example. Used if there is an individual Ray object to get the cursor position
    def lookAt(self, mouse_pos):
        self.dir.x = mouse_pos[0] - self.pos.x
        self.dir.y = mouse_pos[1] - self.pos.y
        self.dir = VectorClass.normalize(self.dir) * 10

#Not used in this example. Helper method to draw Ray objects
    def draw(self, screen):
        pg.draw.aaline(screen, consts.WHITE, (self.pos.x, self.pos.y),
                       (self.dir.x + self.pos.x, self.dir.y + self.pos.y))


#Used to calculate the projected intersection point of two lines
#argument: wall
#          A boundary object where the Ray object is going to intersect
    def cast(self, wall):
        x1 = wall.a.x     #boundary object start and end 
        y1 = wall.a.y
        x2 = wall.b.x
        y2 = wall.b.y
        
        x3 = self.pos.x                #Ray object pos
        y3 = self.pos.y
        x4 = self.pos.x + self.dir.x   #Ray object direction
        y4 = self.pos.y + self.dir.y
        
        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4) #calculate the denominator for the intersect equation
        if den == 0:       #check if the denominator is not 0 (both lines are parallel to each other)
            return False   #otherwise return False and exit

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den   #Calculate t to find the intersect point
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den  #Calculate u to find the intersect point
        
        if (t > 0 and t < 1 and u > 0):  #Check to see if both line segments intersect (0 < t < 1 and 0 < u < 1)
            pt = Vector2D()              #Create a new vector pt
            pt.x = x1 + t * (x2 - x1)    #Calculate the x and y coords for the intersect point
            pt.y = y1 + t * (y2 - y1)
            
            return pt                    #Return the new vector (intersect point of the two lines)
        else:
            return False                 #If not within the check parameters above then return False
        
        
        
        
        
        
        