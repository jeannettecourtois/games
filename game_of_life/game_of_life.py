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



    

def main(dimx:float, dimy:float, cellsize:float):
    pygame.init() #initializing the game 
    surface = pygame.display.set_mode(())
if __name__ == "__main__":
    main()
