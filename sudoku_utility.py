import numpy as np
from random import choice, sample
import itertools
import time

BOARD_DIM = 9
EASY_CLUES = 40
MEDIUM_CLUES = 30
HARD_CLUES = 23
INSANE_CLUES = 17 # lowest amount of clues to still provide a unique solution

def print_grid(grid):

    for i in range(BOARD_DIM):
        if i in [(BOARD_DIM*(1/3)),(BOARD_DIM*(2/3))]: # print horizontal dividers
            print("- "*(BOARD_DIM+2))
        for j in range(BOARD_DIM):
            if j in [(BOARD_DIM*(1/3)),(BOARD_DIM*(2/3))]: # print vertical dividers
                print("|", end=" ")
            print(grid[i][j], end=" ")
        print()


def fill_grid(grid):

    # get all permutations for 1-9
    all_permutes = list(itertools.permutations(list(range(1,BOARD_DIM+1)), r=BOARD_DIM))
    
    # append one permutation to each row
    for i in range(BOARD_DIM):

        # get each current square as list
        curr_square_set = []
        for j in range(0, BOARD_DIM, int(BOARD_DIM*(1/3))):
            for k in range(0, BOARD_DIM, int(BOARD_DIM*(1/3))):
                square = set(grid[m][l] for m in range(k, k+(int(BOARD_DIM*(1/3)))) for l in range(j, j+(int(BOARD_DIM*(1/3)))))
                curr_square_set.append(square)
        
        # use logic to determine valid rows
        allowed = False
        while not allowed:
            allowed = True
            row_choice = choice(all_permutes)
            for j in range(len(row_choice)):
                if i < BOARD_DIM*(1/3): # ensure digit isn't in current square
                    if j < BOARD_DIM*(1/3):
                        if row_choice[j] in curr_square_set[0]:
                            allowed = False
                            break
                    elif j < BOARD_DIM*(2/3):
                        if row_choice[j] in curr_square_set[3]:
                            allowed = False
                            break                      
                    elif j < BOARD_DIM:
                        if row_choice[j] in curr_square_set[6]:
                            allowed = False
                            break                        
                elif i < BOARD_DIM*(2/3):
                    if j < BOARD_DIM*(1/3):
                        if row_choice[j] in curr_square_set[1]:
                            allowed = False
                            break                     
                    elif j < BOARD_DIM*(2/3):
                        if row_choice[j] in curr_square_set[4]:
                            allowed = False
                            break                        
                    elif j < BOARD_DIM:
                        if row_choice[j] in curr_square_set[7]:
                            allowed = False
                            break                       
                elif i < BOARD_DIM:
                    if j < BOARD_DIM*(1/3):
                        if row_choice[j] in curr_square_set[2]:
                            allowed = False
                            break                       
                    elif j < BOARD_DIM*(2/3):
                        if row_choice[j] in curr_square_set[5]:
                            allowed = False
                            break                       
                    elif j < BOARD_DIM:
                        if row_choice[j] in curr_square_set[8]:
                            allowed = False
                            break
                              
                else:
                    allowed = False
                    break 
        
        # remove the all rows with same digit at same index as selected row_choice
        all_permutes = [ row for row in all_permutes if all(x != y for x, y in zip(row, row_choice))] 
        
        grid[i] = list(row_choice) # add valid row to grid
              
    return grid
 
 
def set_grid(grid, difficulty):
    squares = BOARD_DIM*BOARD_DIM

    if difficulty == 'easy':
        clues = EASY_CLUES 
    elif difficulty == 'medium':
        clues = MEDIUM_CLUES 
    elif difficulty == 'hard':
        clues = HARD_CLUES 
    else:
        clues = INSANE_CLUES
        
    # randomly remove squares based on difficulty
    for i in sample(range(squares), squares-clues):
        grid[i//BOARD_DIM][i%BOARD_DIM] = " " 

    return grid
        


def play():
    # generate blank grid
    grid = [[0 for i in range(BOARD_DIM)] for i in range(BOARD_DIM)]
    
    # get difficulty from user
    while True:
        difficulty = input("Please enter a difficulty (easy, medium, hard, insane): ")
        if difficulty.lower() in ['easy', 'medium', 'hard', 'insane']:
            break
            
    # create valid grid of numbers
    print("Generating a new Sudoku grid...")
    grid = fill_grid(grid)

    # set grid according to difficulty
    grid = set_grid(grid, difficulty)
    
    # print final grid
    print_grid(grid)  


if __name__ == "__main__":
    play()
