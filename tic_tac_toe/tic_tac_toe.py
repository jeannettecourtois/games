import math as mt
from typing import Callable
import random
import numpy as np 

# Some data structures

Grid = tuple[tuple[int, ...], ...]
State = Grid
Action = tuple[int, int]
Player = int
Score = float

# Some constants
DRAW = 0
EMPTY = 0
X = 1
O = 2

# Predefined grids

EMPTY_GRID: Grid = ((0, 0, 0), (0, 0, 0), (0, 0, 0))
GRID_0: Grid = EMPTY_GRID
GRID_1: Grid = ((0, 0, 0), (0, X, O), (0, 0, 0))
# (0, 0, 0),
# (0, X, O),
# (0, 0, 0))

GRID_2: Grid = ((O, 0, X), (X, X, O), (O, X, 0))
#((O, 0, X),
# (X, X, O),
# (O, X, 0)

GRID_3: Grid = ((O, 0, X), (0, X, O), (O, X, 0))
#((O, 0, X),
# (0, X, O),
# (O, X, 0))

GRID_4: Grid = ((0, 0, 0), (X, X, O), (0, 0, 0))
#((0, 0, 0),
# (X, X, O),
# (0, 0, 0))

#preliminary functions
def grid_tuple_to_grid_list(grid: Grid) -> list[list[int]]: 
    return [list(row) for row in grid]

def grid_list_to_grid_tuple(grid: list[list[int]]) -> Grid:
    return tuple(tuple(row) for row in grid)

# this function returns all the legal actions in a given state
def legals(grid: State) -> list[Action]: 
    the_grid = grid_tuple_to_grid_list(grid)
    actions = []
    for i in range(3):
        for j in range(3):
            if the_grid[i][j] == EMPTY:
                actions.append((i, j))
    return actions 

def line(grid: State, player: Player) -> bool:
    the_grid = grid_tuple_to_grid_list(grid)
    if the_line(the_grid, player):
        return True
    if the_column(the_grid, player):
        return True
    if diagonal(the_grid, player):
        return True
    return False 


def the_line(grid:list[list[int]], player:Player)->bool:
    for row in grid:
        if (len(set(row)) == 1) and (row[0] == player):
            return True
    return False 

def the_column(grid:list[list[int]], player:Player)->bool:
    column = []
    for j in range(3):
        column.clear()
        for i in range(3):
            column.append(grid[i][j])
        if len(set(column)) == 1 and column[0] == player:
            return True
    return False 
        
def diagonal(grid: list[list[int]], player: Player) -> bool:
    diagonal = []
    for i in range(3):
        diagonal.append(grid[i][i])
    if len(set(diagonal)) == 1 and diagonal[0] == player:
        return True
    return False 


            
        
# Eventual classes we will need 
class Player: 
    pass 
class Game: 
    pass 
class Score:
    pass 


def main():
    print("Hello Tic Tac Toe")
    grid_1 = grid_tuple_to_grid_list(GRID_1)
    print(grid_list_to_grid_tuple(grid_1))

if __name__ == "__main__":
    main()