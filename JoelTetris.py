import math
import random
import time
import pygame
import pygame.freetype
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
shape_number = -1
shape_color = -1
board = np.zeros((rows, cols))

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
    (1,1,1,0),
    (0,0,1,0),
    (0,0,0,0),
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

def generateShapeIndex():
    shape_number = random.randrange(0,7)
    if(shape_number == 0):
        shape_color = colors[0]
    elif(shape_number == 1):
        shape_color = colors[1]
    elif(shape_number == 2):
        shape_color = colors[2]
    elif(shape_number == 3):
        shape_color = colors[3]
    elif(shape_number == 4):
        shape_color = colors[4]
    elif(shape_number == 5):
        shape_color = colors[5]
    elif(shape_number == 6):
        shape_color = colors[6]

    return shape_number

# Places the first shape of the game. Should be randomly generated, but that can't happen until all shapes can be moved without a segfault.
def placeStartingShape(window, board):
    shape_number = generateShapeIndex()
    print(shape_number)
    shape = Shapes[shape_number]
    #shape = Shapes[2]
    #print(shape)

    for i in range(shape.shape[0]):
        for j in range(shape.shape[1]):
            # only draw squares in cells populated with a 1
            if(shape[i][j] == 1):
                board[i][j+4] = 1

# Spawns new shape at the top of the board when there are no active blocks
def spawnShape(window, board):
    active = False
    shape_number = generateShapeIndex()
    shape = Shapes[shape_number]
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if(board[i][j] == 1):
                active = True

    if(active == False):
       for i in range(shape.shape[0]):
        for j in range(shape.shape[1]):
            # only draw squares in cells populated with a 1
            if(shape[i][j] == 1):
                board[i][j+4] = 1        

# Fill the squares on the grid with color. Only fills cells populated with a 1
def drawShapes(window, board):
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if(board[i][j] == 1):
                pygame.draw.rect(window, colors[3], (j*square_size+450, i*square_size+margin, square_size, square_size))

# Draws all frozen shapes (2) to the board
def drawFrozenShapes(window, board):
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if(board[i][j] == 2):
                pygame.draw.rect(window, colors[4], (j*square_size+450, i*square_size+margin, square_size, square_size))

# This function is essentially the same as move(), but does not have a direction parameter
# Need to vary the fall speed somehow
def fall(window, board):
    coords = []
    pairs = []

    rows, cols = board.shape[0], board.shape[1]

    for i in range(rows):
        for j in range(cols):
            if(board[i][j] == 1):
                coords.append(i)
                coords.append(j)
                pairs.append(list(coords))
                coords.pop()
                coords.pop()

    new_pairs = []
    new_coords = []

    for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                if(board[i][j] == 1 and i < 19):
                    new_coords.append(i+1)
                    new_coords.append(j)
                    new_pairs.append(list(new_coords))
                    new_coords.pop()
                    new_coords.pop()


    if(len(new_pairs) == 4):
        # for each element in new_pairs (coordinates)
        for i in range(4):
            # set old pairs to 0
            board[pairs[i][0]][pairs[i][1]] = 0
        for i in range(4):
            # set new pairs to 1
            board[new_pairs[i][0]][new_pairs[i][1]] = 1

    new_coords.clear()
    new_pairs.clear()

# freezes a shape if it touches the bottom
def freezeShapes(window, board):
    rows, cols = board.shape[0], board.shape[1]    
    for i in range(rows):
        for j in range(cols):
            if((board[i][j] == 1 and i == 19) or (board[i][j] == 1 and board[i+1][j] == 2)):
                for i in range(rows):
                    for j in range(cols):
                        if(board[i][j] == 1):
                            board[i][j] = 2

def clearRow():
    rowFull = True
    rows, cols = board.shape[0], board.shape[1]    
    for i in range(rows):
        for j in range(cols):
            if (board[i][j] == 0 or board[i][j] == 1):
                rowFull = False
        if rowFull:
            for k in range(rows):
                for l in range(cols):
                    if k + 1 < i:
                        board[i-k][l] = board[i-k-1][l]
        rowFull = True

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

def checkGameState():
    rows, cols = board.shape[0], board.shape[1] 
    for i in range(cols):
        if board[1][i] == 2:
            return True
    return False

# Moves pieces left and right
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
    new_pairs = []
    new_coords = []
    
    if(dir == "L"):
        # Get all coordinates one cell to the left of current 1's
        for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                if(board[i][j] == 1 and j > 0 and board[i][j-1] != 2):
                    new_coords.append(i)
                    new_coords.append(j-1)
                    new_pairs.append(list(new_coords))
                    new_coords.pop()
                    new_coords.pop()

    elif(dir == "R"):
        for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                if(board[i][j] == 1 and j < 9 and board[i][j+1] != 2):
                    new_coords.append(i)
                    new_coords.append(j+1)
                    new_pairs.append(list(new_coords))
                    new_coords.pop()
                    new_coords.pop()
        
    # Prevents segfault by ensuring all coordinates in the new_pairs list are on the board
    if(len(new_pairs) == 4):
        # for each element in new_pairs (coordinates)
        for i in range(4):
            # set old pairs to 0
            board[pairs[i][0]][pairs[i][1]] = 0
        for i in range(4):
            # set new pairs to 1
            board[new_pairs[i][0]][new_pairs[i][1]] = 1

    elif(dir == "D"):
        pass

    # Empty the coordinate lists for the next call to this function
    #pairs.clear()
    #coords.clear()
    new_coords.clear()
    new_pairs.clear()


def main():

    # Initialization stuff
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Joel Tetris")
    #image = pygame.image.load('joel8bit.png')
    clock = pygame.time.Clock()
    game_over = False
    random.seed()
    dirx = ""

    # Place the first shape
    placeStartingShape(window, board)

    # Game loop
    while not game_over:
        # Changes block movement speed
        pygame.time.delay(10)
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

        # Prevent any shapes that have hit the bottom of the board from moving
        freezeShapes(window, board)

        # Clear the screen and set the screen background
        window.fill(bg_color)

        # Print the board state in console
        #print(board)

        # Draw frozen shapes to the screen
        drawFrozenShapes(window, board)

        # Clears a full row of squares
        clearRow()

        game_over = checkGameState() 

        # Spawn a new shape when all shapes are frozen
        spawnShape(window, board)

        # Draw shape to screen
        drawShapes(window, board)

        # Block falls downward one unit every tick
        fall(window, board)

        # Draw crosshatched pattern on window
        draw_grid(window)
        
        pygame.display.update()
             
    pygame.quit()

main()