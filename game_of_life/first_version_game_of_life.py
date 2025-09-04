import numpy as np 
from typing import Callable
import random 


SIZE = random.randint(5, 20)

Grid = list[list[int]]
Cell = int #0 for dead and 1 for alive 
Cycles = int 
def random_grid(size:int) -> Grid:
    the_grid = np.zeros((SIZE, SIZE))
    for i in range(SIZE):
        for j in range(SIZE):
            the_grid[i][j] = random.randint(0, 1)
    return the_grid

def next_grid(number_of_cycles:Cycles)->Grid:
    grid = random_grid(SIZE)
    for i in range(number_of_cycles):
        print(grid)
        for row, col in np.ndindex(grid.shape):
            cells_alive = np.sum(grid[row-1:row+2][col-1:col+2]) - grid[row][col]
            
            if cells_alive < 2 or cells_alive > 3:
                grid[row][col] = 0
            elif grid[row][col] == 1 and (cells_alive == 3 or cells_alive == 2):
                grid[row][col] = 1
            elif grid[row][col] == 0 and cells_alive == 3:
                grid[row][col] = 1  
    return 

print(next_grid(2))