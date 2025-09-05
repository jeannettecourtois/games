import time 
import pygame 
import numpy as np
import random 
from typing import Callable

#Rules of the game of life 
#Rule 1: A live cell with fewer than two live neighbours dies, as if caused by under-population.
#Rule 2: A live cell with two or three live neighbours remains alive (survival).
#Rule 3: A live cell with more than three live neighbours dies, as if by over-population.
#Rule 4: A dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

#this game of life with this set of rules is "Turing Complete", meaning that this kind of machine can theorically perform any calculation 


#colors 

color_about_to_die = (200, 200, 200) #gray
color_alive = (255, 255, 255) #green 
color_background = (10, 10, 40) #blue 
color_grid = (30, 30, 60) #blue

def update(surface, the_cells, size):
    nxt = np.zeros((the_cells.shape[0], the_cells.shape[1]))
    for row, col in np.ndindex(the_cells.shape):
        num_alive = np.sum(the_cells[row-1:row+2, col-1:col+2]) - the_cells[row][col] #careful with slacing 
        if the_cells[row][col] == 1 and num_alive < 2 or num_alive >3:
            color = color_about_to_die #according to the rules 
        elif (the_cells[row][col] == 1 and 2 <= num_alive <= 3) or (the_cells[row][col] == 0 and num_alive == 3):
            nxt[row][col] = 1
            color = color_alive
        color = color if the_cells[row][col] == 1 else color_background
        pygame.draw.rect(surface, color, (col*size, row*size, size-1, size-1)) #coordinates then size -> pygame.draw.rect(surface, color, (x, y, w, h))
    return nxt

def init(dimx, dimy):
    cells = np.zeros((dimy, dimx))
    #the Gosper glider fun
    pattern = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
    pos = (3, 3)
    cells[pos[0]:pos[0]+pattern.shape[0], pos[1]:pos[1]+pattern.shape[1]] = pattern
    return cells 



def main(dimx, dimy, cellcize):
    pygame.init() #initializing the game 
    surface = pygame.display.set_mode((dimx*cellcize, dimy*cellcize)) #pygame.display.set_mode((w, h)) -> it returns a surface 
    pygame.display.set_caption("John Conway's Game of Life")
    cells = init(dimx, dimy)
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 
            
        surface.fill(color_grid)
        cells = update(surface, cells, cellcize)
        pygame.display.update()
if __name__ == "__main__":
    main(120, 90, 8)
