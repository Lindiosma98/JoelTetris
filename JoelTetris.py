import math
import random
import pygame
import numpy as np
import tkinter as tk
from tkinter import messagebox

width = 800 # Display width
height = 700 # Display height
play_width = 300 # Play zone
play_height = 600 # Play zone
square_size = 30 # Size per block
rows = 20
cols = 10

# margin to place around the board, just for aesthetic purposes
margin = 50

# Color constants
# [Black, White, Teal, Purple, Red, Green, Yellow]
colors = [(0,0,0),(255,255,255),(0,255,255),(255,60,245),(255,45,45),(55,255,65),(245,255,50)]
bg_color = (125, 150, 175)

board = np.zeros((20, 10))

# Numpy arrays for shapes. 4x4. Column-major.
T = np.array([
    (0,1,0,0),
    (1,1,0,0),
    (0,1,0,0),
    (0,0,0,0)
    ])
O = np.array([
    (1,1,0,0),
    (1,1,0,0),
    (0,0,0,0),
    (0,0,0,0)
    ])
J = np.array([
    (0,0,1,0),
    (1,1,1,0),
    (0,0,0,0),
    (0,0,0,0)
    ])
L = np.array([
    (0,0,0,0),
    (1,1,1,0),
    (0,0,1,0),
    (0,0,0,0)
    ])
Z = np.array([
    (1,0,0,0),
    (1,1,0,0),
    (0,1,0,0),
    (0,0,0,0)
    ])
S = np.array([
    (0,1,0,0),
    (1,1,0,0),
    (1,0,0,0),
    (0,0,0,0)
    ])
I = np.array([
    (0,1,0,0),
    (0,1,0,0),
    (0,1,0,0),
    (0,1,0,0)
    ])

# Index this to access one of the np arrays above. i.e. "Shapes[2]" would equal J
Shapes = [T, O, J, L, Z, S, I]

# Places the first shape of the game. Should be randomly generated, but that can't happen until all shapes can be moved without a segfault.
def placeStartingShape(window, board):
    #shape = Shapes[random.randrange(len(Shapes)-1)]
    shape = Shapes[1]
    for i in range(shape.shape[0]):
        for j in range(shape.shape[1]):
            # only draw squares in cells populated with a 1
            if(shape[i][j] == 1):
                board[i][j] = 1

# Fill the squares on the grid with color. Only fills cells populated with a 1
def drawShapes(window, board):
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if(board[i][j] == 1):
                #print(j,i)
                #print(j*square_size+450, i*square_size+margin)
                pygame.draw.rect(window, colors[2], (j*square_size+450, i*square_size+margin, square_size, square_size))

# This needs to be implemented correctly...this ain't the way.
'''def fall(window, board):
    for i in range(board.shape[0]-1):
        for j in range(board.shape[1]-1):
            if(board[i][j] == 1):
                board[i+1][j] = 1
                break'''

                
# Draws crosshatched pattern on canvas
def draw_grid(window):
    x, y = 0, 0

    # Draw horizontal lines
    for _ in range(rows+1):
        # params: (window name, line color, [line start x, line start y], [line end x, line end y], thickness)
        pygame.draw.line(window, colors[0], [(width/2)+margin, y+margin], [width-margin, y+margin], 1)
        y += square_size

    # Draw vertical lines
    for _ in range(cols+1):
        # params: (window name, line color, [line start x, line start y], [line end x, line end y], thickness)
        pygame.draw.line(window, colors[0], [width/2+x+margin, 0+margin], [width/2+x+margin, height-margin], 1)
        x += square_size


def move(window, dir):
    # simple list of shape coordinate values (aka where the 1's are in the board)
    coords = []

    # the same list as above, but converted into list of lists (each of length 2 for easy and sensible indexing)
    pairs = []
    
    # grabbing max row and col values
    rows, cols = board.shape[0], board.shape[1]
    
    # loop through board array, store locations of 1's (aka where the shape currently is located)
    for i in range(rows):
        for j in range(cols):
            if(board[i][j] == 1):
                coords.append(i)
                coords.append(j)
                pairs.append(list(coords))
                coords.pop()
                coords.pop()

    #print(pairs)
    
    # This strategy of block movement currently only works for the O block (2x2). Segfaults otherwise.
    if(dir == "L"):
        # Only move left if the leftmost parts of the block aren't at index 0 of the board
        if(pairs[0][1] != 0 and pairs[2][1] != 0):
            board[pairs[0][0]][pairs[0][1]-1] = 1
            board[pairs[2][0]][pairs[2][1]-1] = 1
            board[pairs[1][0]][pairs[1][1]] = 0
            board[pairs[3][0]][pairs[3][1]] = 0
    elif(dir == "R"):
        # Only move right if the rightmost parts of the block aren't at index 9 of the board
        if(pairs[1][1] != 9 and pairs[3][1] != 9):
            board[pairs[1][0]][pairs[1][1]+1] = 1
            board[pairs[3][0]][pairs[3][1]+1] = 1
            board[pairs[0][0]][pairs[0][1]] = 0
            board[pairs[2][0]][pairs[2][1]] = 0
    elif(dir == "D"):
        pass

    # Empty the coordinate lists for the next call to this function
    pairs.clear()
    coords.clear()


def main():

    # Initialization stuff
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Joel Tetris")
    clock = pygame.time.Clock()
    game_over = False
    random.seed()
    dirx = ""

    # Place the first shape
    placeStartingShape(window, board)

    # Game loop
    while not game_over:
        pygame.time.delay(100)
        # One hundred ticks per second
        clock.tick(100)
        
        # Event handling (user input)
        pygame.key.set_repeat(1, 10) 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                game_over = True 

            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    #print("Left")
                    dirx = "L"
                elif keys[pygame.K_RIGHT]:
                    #print("Right")
                    dirx = "R"

        # Move the block in the direction dirx
        move(window, dirx)
        dirx = ""
        #fall(window, board)
         
        # Clear the screen and set the screen background
        window.fill(bg_color)

        # Print the board state in console
        print(board)

        # Draw shape to screen
        drawShapes(window, board)

        # Draw crosshatched pattern on window
        draw_grid(window)
        pygame.display.flip()

        #rotate()
        #move()
        #drop()
        #print(sa)
        #stopped_pieces = {} #Dictionary for pieces placed and not moving on grid in form
                            # (x,y): 0,1,2 where 0-no block, 1-curr block moving, 2-block done moving
        #Create grid 10x20 that has 0 throughout to show no blocks
        #stopped_pieces keeps track of spaces of pieces that are
        #locked into the grid by game collision rules
        '''def create_grid(stopped_pieces = {}):
            grid = [[0 for _ in range(10)] for _ in range(20)]

            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if (i,j) in stopped_pieces:
                        stopped = stopped_pieces[(i,j)]
                        grid[i][j] = stopped
            return grid'''       
    pygame.quit()

main()