import pygame
import sys
from pygame.locals import *
from grid_generator import fill_grid, set_grid

"""
CHANGE THIS:

options: easy, medium, hard, insane

"""
DIFFICULTY = 'hard'



pygame.init()

# set screen dims
GRID_DIM = 900
SIDE_SQUARES = 9

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHT_GRAY = (200,200,200)
RED = (255, 0, 0)

# font
pygame.font.init()
FONT = pygame.font.SysFont('Comic Sans MS', 22)

# set FPS
clock = pygame.time.Clock()
FPS = 10
clock.tick(FPS)

# create window
GAME_DISPLAY = pygame.display.set_mode((GRID_DIM+1,GRID_DIM+1))
GAME_DISPLAY.fill(WHITE)
pygame.display.set_caption('Sudoku')

class button():
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.x + self.width, self.y + self.height))
        
    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

def draw_grid(grid):
    # Draw lines
    for i in range(0, GRID_DIM+GRID_DIM//9, GRID_DIM//9):
        pygame.draw.line(GAME_DISPLAY, LIGHT_GRAY, (i, 0), (i, GRID_DIM))
        pygame.draw.line(GAME_DISPLAY, LIGHT_GRAY, (0, i), (GRID_DIM, i))       

    for i in range(0, GRID_DIM+GRID_DIM//3, GRID_DIM//3):
        pygame.draw.line(GAME_DISPLAY, BLACK, (i, 0), (i, GRID_DIM))
        pygame.draw.line(GAME_DISPLAY, BLACK, (0, i), (GRID_DIM, i))
    
    # Fill numbers
    x, y = 0, 0 # used to index numbers in grid
    for i in range(0, GRID_DIM, GRID_DIM//9):
        for j in range(0, GRID_DIM, GRID_DIM//9):
            textsurface = FONT.render(str(grid[x][y]), False, BLACK)
            GAME_DISPLAY.blit(textsurface, (i+(GRID_DIM//9)*0.45, j+(GRID_DIM//9)*0.4))
            pygame.display.update()
            y+=1
        y = 0
        x+=1


# def redraw(tile):
    # tile.draw(GAME_DISPLAY)
    
   
def main():
    grid = [[0 for i in range(SIDE_SQUARES)] for i in range(SIDE_SQUARES)]
    grid = fill_grid(grid)
    grid = set_grid(grid, DIFFICULTY)
    
    draw_grid(grid)
    pygame.image.save(GAME_DISPLAY, "sudoku_puzzle.jpeg")
    while True:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            # if event.type == pygame.MOUSEMOTION:
                # if test.isOver(pos):
                    # test.color = RED
                # else:
                    # test.color = BLACK
        pygame.display.update()            
        
if __name__ == "__main__":
    main()