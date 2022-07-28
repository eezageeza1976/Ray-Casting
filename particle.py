#Particle class
import pygame as pg
import consts
import vector
import math
from vector import Vector2D
from boundary import Ray

############################################################
#Particle class used for creating an array of Ray objects
#constructor: screen - Used in the draw() method. Placed here so only passed once
#
############################################################
class Particle:
    def __init__(self, screen):
        self.screen = screen
        self.pos = Vector2D(consts.WIN_WIDTH/2, consts.WIN_HEIGHT/2)
        self.rays = []      #An array to store all the Ray objects
        
        for a in range(0, 360, 1):                   #Create the array of Ray objects
            ray = Ray(self.pos, math.radians(a))     #Creating one Ray object per degree(converted to radians)
            self.rays.append(ray)                    #Add to rays array


#draw method used to draw the light source
    def draw(self):
        pg.draw.circle(self.screen, consts.WHITE, (self.pos.x, self.pos.y), 5)
        
#check which is the closest boundary object and stopping the Ray at that wall
#argument: walls
#          An array of boundary objects
    def look(self, walls):
        for ray in self.rays:        #Loop through the Ray array
            closest = None           #variable for the closest wall
            record = math.inf        #variable set to infinity. Reset for every wall
            for wall in walls:       #Loop through the walls array
                pt = ray.cast(wall)  #Call the Ray class cast() method with the boundary object to check
                if pt:               #If pt is returned
                    d = vector.dist(self.pos, pt)  #check the distance between the particle position and pt position
                    if d < record:                      #if d is less than record 
                        record = d                      #set record as the currant distance
                        closest = pt                    #set the closest wall as this wall
                                                        #loop through all the boundary objects to find out which
                                                        #is the closest
            if closest:    #Then draw the ray from the current position to the closest intersect point
                pg.draw.aaline(self.screen, consts.GRAY_ALPHA, (self.pos.x, self.pos.y), (closest.x, closest.y))
                
#Update the particle object position to the mouse position        
    def update(self, mouse_pos):
        self.pos.x = mouse_pos[0]
        self.pos.y = mouse_pos[1]
        
        