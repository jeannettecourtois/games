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
Strategy = Callable[[State, Player], Action]

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

GRID_5: Grid = ((0, 0, 0), (X, X, X), (0, 0, 0))

GRID_6: Grid = ((O, 0, X), (O, O, X), (O, 0, O))


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
    if first_diagonal(the_grid, player):
        return True
    if second_diagonal(the_grid, player):
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
        
def first_diagonal(grid: list[list[int]], player: Player) -> bool:
    diagonal = []
    for i in range(3):
        diagonal.append(grid[i][i])
    if len(set(diagonal)) == 1 and diagonal[0] == player:
        return True
    return False 

def second_diagonal(grid: list[list[int]], player: Player) -> bool:
    diagonal = []
    for i in range(3):
        diagonal.append(grid[i][2-i])
    if len(set(diagonal)) == 1 and diagonal[0] == player:
        return True
    return False

def final(grid: State) -> bool:
    if line(grid, X) or line(grid, O):
        return True
    elif len(legals(grid)) == 0:
        return True
    else:
        return False

def score(grid: State) -> Score:
    if final(grid) and line(grid, X):
        return 1.0
    elif final(grid) and line(grid, O):
        return -1.0
    else: 
        return 0.0
        
def play(grid: State, player: Player, action: Action) -> State:
    the_grid = grid_tuple_to_grid_list(grid)
    the_grid[action[0]][action[1]] = player
    return grid_list_to_grid_tuple(the_grid)
    
# Strategy = Callable[[State, Player], Action]
def tictactoe(strategy_X: Strategy, strategy_O: Strategy, debug: bool = False) -> Score:
    grid = EMPTY_GRID
    player = X #we start with player X
    # We play until the game is finished
    while not(final(grid)):
        if debug:
            print(grid)
            raise Exception("We had to stop the game for debugging")
        if player == X:
            action = strategy_X(grid, player)
            grid = play(grid, player, action)
            player = O
        if player == O:
            action = strategy_O(grid, player)
            grid = play(grid, player, action)
            player = X 
    return score(grid)

#this player always uses the first legal action available
def strategy_first_legal(grid: State, player: Player) -> Action:
    actions = legals(grid)
    return actions[0]  

#this player always uses a random legal action available
def strategy_random(grid: State, player: Player) -> Action:
    actions = legals(grid)
    random_number = random.randint(0, len(legals(grid))-1)
    return actions[random_number]

def minmax(grid: State, player: Player) -> Score:
    pass

# Eventual classes we will need 
class Player: 
    pass 
class Game: 
    pass 
class Score:
    pass 


def main():
    print("Hello Tic Tac Toe")
    # grid_1 = grid_tuple_to_grid_list(GRID_1)
    # print(grid_list_to_grid_tuple(grid_1))
    print(grid_tuple_to_grid_list(GRID_1))
    print(play(GRID_1, X, (0,0)))

if __name__ == "__main__":
    main()