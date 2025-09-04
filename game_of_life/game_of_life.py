import time 
import pygame 
import numpy as np
from typing import Callable

#Rules of the game of life 
#Rule 1: A live cell with fewer than two live neighbours dies, as if caused by under-population.
#Rule 2: A live cell with two or three live neighbours remains alive (survival).
#Rule 3: A live cell with more than three live neighbours dies, as if by over-population.
#Rule 4: A dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

#defining some basic colors 

COLOR_BG = (10, 10, 10)
COLOR_GRID = (40, 40, 40)
COLOR_DIE_NEXT = (170, 170, 170)
COLOR_ALIVE_NEXT = (255, 255, 255)

def update(screen, cells, size, with_progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))
    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE_NEXT
    
    if cells[row, col] == 1:
        if alive < 2 or alive > 3:
            if with_progress:
                color = COLOR_DIE_NEXT
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
    else: 
        if alive == 3:
            updated_cells[row, col] = 1
            if with_progress:
                color = COLOR_ALIVE_NEXT
    pygame.draw.rect(screen, color, (col*size, row*size, size-1, size-1))
    
    return updated_cells
    

def main():
    pygame.init() #initializing the pygame library
    screen = pygame.display.set_mode((800, 800)) #setting the display window
    cells = np.zeros((60, 80))
    screen.fill(COLOR_GRID)
    update(screen, cells, 10)
    
    pygame.display.flip()
    pygame.display.update()
    
    running = False 
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running 
                    update(screen, cells, 10)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1]//10, pos[0]//10] = 1
                update(screen, cells, 10)
                pygame.display.update()
        screen.fill(COLOR_GRID)
        if running:
            cells = update(screen, cells, 10, with_progress=True)
            pygame.display.update()
        time.sleep(0.001)
if __name__ == "__main__":
    main()
