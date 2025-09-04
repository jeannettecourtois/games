import time 
import pygame 
import numpy as np
from typing import Callable

#Rules of the game of life 
#Rule 1: A live cell with fewer than two live neighbours dies, as if caused by under-population.
#Rule 2: A live cell with two or three live neighbours remains alive (survival).
#Rule 3: A live cell with more than three live neighbours dies, as if by over-population.
#Rule 4: A dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

pygame.init() # Initialize the pygame modules

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)

WIDTH, HEIGHT = 800, 800
TILE_SIZE = 20
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

def draw_grid(positions):
    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row*TILE_SIZE), (WIDTH, row*TILE_SIZE))
        


def main():
    running = True 
    
    positions = set()
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(GREY)
        draw_grid(positions)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
