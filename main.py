import pygame as pg
import consts
import random
from particle import Particle
from boundary import Boundary

def windowSetup():
    window = pg.display.set_mode((consts.WIN_WIDTH, consts.WIN_HEIGHT))
    window.fill(consts.BLACK)
    return window

def main(screen):
    running = True   #game running
    walls = []       #array to hold a list of walls
    
    #generate 5 random walls
    for i in range(5):
        x1 = random.randint(0, consts.WIN_WIDTH)
        x2 = random.randint(0, consts.WIN_WIDTH)
        y1 = random.randint(0, consts.WIN_HEIGHT)
        y2 = random.randint(0, consts.WIN_HEIGHT)        
        walls.append(Boundary(screen, x1, y1, x2, y2))   #addthem to the walls list
    
    #create the boundary of the screen and add them to the walls list
    walls.append(Boundary(screen, 0, 0, consts.WIN_WIDTH, 0))
    walls.append(Boundary(screen, consts.WIN_WIDTH, 0, consts.WIN_WIDTH, consts.WIN_HEIGHT))
    walls.append(Boundary(screen, consts.WIN_WIDTH, consts.WIN_HEIGHT, 0, consts.WIN_HEIGHT))
    walls.append(Boundary(screen, 0, consts.WIN_HEIGHT, 0, 0))
    
    particle = Particle(screen) #new Particle object
    
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
        
        screen.fill(consts.BLACK)
        #Draw all the walls onto the screen
        for wall in walls:
            wall.draw()
            
        particle.update(pg.mouse.get_pos())    #update the particle with the mouse position
        particle.look(walls)                   #Call the Particle look method 
        particle.draw()                        #Call the Particle draw method
        pg.display.flip()

if __name__ == '__main__':
    pg.init()
    main(windowSetup())
    pg.quit()