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
    (2,2,0,0),
    (2,2,0,0),
    (0,0,0,0),
    (0,0,0,0)
    ])
J = np.array([
    (0,0,3,0),
    (3,3,3,0),
    (0,0,0,0),
    (0,0,0,0)
    ])
L = np.array([
    (4,4,4,0),
    (0,0,4,0),
    (0,0,0,0),
    (0,0,0,0)
    ])
Z = np.array([
    (5,0,0,0),
    (5,5,0,0),
    (0,5,0,0),
    (0,0,0,0)
    ])
S = np.array([
    (0,6,0,0),
    (6,6,0,0),
    (6,0,0,0),
    (0,0,0,0)
    ])
I = np.array([
    (0,7,0,0),
    (0,7,0,0),
    (0,7,0,0),
    (0,7,0,0)
    ])

# Index this to access one of the np arrays above. i.e. "Shapes[2]" would equal J
Shapes = [T, O, J, L, Z, S, I]

def rotate(board):

    # Create an empty 4x4 array to hold the shape grabbed from the board
    emptyShape = np.zeros((4, 4))

    # lists for storing coordinates
    coords = []
    pairs = []

    # get coordinates of the unique shapes in the board
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if(board[i][j] == 1):
                coords.append(i)
                coords.append(j)
                pairs.append(list(coords))
                coords.pop()
                coords.pop()
                board[i][j] = 0

    # get the x values from the coordinates
    for i in pairs:
        coords.append(i[0])

    # get the minimum x value
    minimum_x = min(coords)

    coords.clear()

    # get the y values from the coordinates
    for i in pairs:
        coords.append(i[1])

    # get the minimum y value
    minimum_y = min(coords)

    coords.clear()

    # subtract the minimum coordinate values from the shape when it's on the board
    # this creates the original shape as it's stored in a 4x4 array
    for i in range(len(pairs)):
        pairs[i][0] -= minimum_x
        pairs[i][1] -= minimum_y

    # fill in the 1's
    for i in range(4):
        emptyShape[pairs[i][0]][pairs[i][1]] = 1

    # rotate the recreated shape array
    rotated_shape = np.rot90(emptyShape)

    # This chunk here was me attempting to mitigate the shift created by rotation, might use this idea to some extent later
    '''for i in range(rotated_shape.shape[0]):
        for j in range(rotated_shape.shape[1]):
            if(rotated_shape[i][j] == 1):
                rotated_shape[i-1][j] = 1
                rotated_shape[i][j] = 0'''

    #print(rotated_shape)

    # Draw the rotated shape back to the game board at its original position
    for i in range(emptyShape.shape[0]):
        for j in range(emptyShape.shape[1]):
            if(rotated_shape[i][j] == 1):
                board[i+minimum_x][j+minimum_y] = 1
                

def generateShapeIndex():
    shape_number = random.randrange(0,7)
    if(shape_number == 0):
        shape_color = colors[shape_number]
    elif(shape_number == 1):
        shape_color = colors[shape_number]
    elif(shape_number == 2):
        shape_color = colors[shape_number]
    elif(shape_number == 3):
        shape_color = colors[shape_number]
    elif(shape_number == 4):
        shape_color = colors[shape_number]
    elif(shape_number == 5):
        shape_color = colors[shape_number]
    elif(shape_number == 6):
        shape_color = colors[shape_number]

    return shape_number

def unique

# Places the first shape of the game. Should be randomly generated, but that can't happen until all shapes can be moved without a segfault.
def placeStartingShape(window, board):
    shape_number = generateShapeIndex()
    print(shape_number)
    shape = Shapes[shape_number]
    #shape = Shapes[2]
    #print(shape)

    for i in range(shape.shape[0]):
        for j in range(shape.shape[1]):
            # only draw squares in cells populated with a 1-7
            if(shape[i][j] == 1):
                board[i][j+4] = 1
            else if(shape[i][j] == 2):
                board[i][j+4] = 2
            else if(shape[i][j] == 3):
                board[i][j+4] = 3
            else if(shape[i][j] == 4):
                board[i][j+4] = 4
            else if(shape[i][j] == 5):
                board[i][j+4] = 5
            else if(shape[i][j] == 6):
                board[i][j+4] = 6
            else if(shape[i][j] == 7):
                board[i][j+4] = 7

# Spawns new shape at the top of the board when there are no active blocks
def spawnShape(window, board):
    active = False
    shape_number = generateShapeIndex()
    shape = Shapes[shape_number]
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if(board[i][j] == 1 or board[i][j] == 2 or board[i][j] == 3 or board[i][j] == 4 or board[i][j] == 5 or board[i][j] == 6 or board[i][j] == 7):
                active = True

    if(active == False):
       for i in range(shape.shape[0]):
        for j in range(shape.shape[1]):
            # only draw squares in cells populated with 1-7
            if(shape[i][j] == 1):
                board[i][j+4] = 1 # 8 when frozen
            else if(shape[i][j] == 2):
                board[i][j+4] = 2 # 9 when frozen
            else if(shape[i][j] == 3):
                board[i][j+4] = 3 # 10 when frozen
            else if(shape[i][j] == 4):
                board[i][j+4] = 4 # 11 when frozen
            else if(shape[i][j] == 5):
                board[i][j+4] = 5 # 12 when frozen
            else if(shape[i][j] == 6):
                board[i][j+4] = 6 # 13 when frozen
            else if(shape[i][j] == 7):
                board[i][j+4] = 7 # 14 when frozen

# Fill the squares on the grid with color. Only fills cells populated with a 1
def drawShapes(window, board):
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if(board[i][j] == 1):
                pygame.draw.rect(window, colors[1], (j*square_size+450, i*square_size+margin, square_size, square_size))
            else if(board[i][j] == 2):
                pygame.draw.rect(window, colors[2], (j*square_size+450, i*square_size+margin, square_size, square_size))
            else if(board[i][j] == 3):
                pygame.draw.rect(window, colors[3], (j*square_size+450, i*square_size+margin, square_size, square_size))
            else if(board[i][j] == 4):
                pygame.draw.rect(window, colors[4], (j*square_size+450, i*square_size+margin, square_size, square_size))
            else if(board[i][j] == 5):
                pygame.draw.rect(window, colors[5], (j*square_size+450, i*square_size+margin, square_size, square_size))
            else if(board[i][j] == 6):
                pygame.draw.rect(window, colors[6], (j*square_size+450, i*square_size+margin, square_size, square_size))
            else if(board[i][j] == 7):
                pygame.draw.rect(window, colors[7], (j*square_size+450, i*square_size+margin, square_size, square_size))

# Draws all frozen shapes (2) to the board
def drawFrozenShapes(window, board):
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if(board[i][j] == 8):
                pygame.draw.rect(window, colors[1], (j*square_size+450, i*square_size+margin, square_size, square_size))
            else if(board[i][j] == 9):
                pygame.draw.rect(window, colors[2], (j*square_size+450, i*square_size+margin, square_size, square_size))
            else if(board[i][j] == 10):
                pygame.draw.rect(window, colors[3], (j*square_size+450, i*square_size+margin, square_size, square_size))
            else if(board[i][j] == 11):
                pygame.draw.rect(window, colors[4], (j*square_size+450, i*square_size+margin, square_size, square_size))
            else if(board[i][j] == 12):
                pygame.draw.rect(window, colors[5], (j*square_size+450, i*square_size+margin, square_size, square_size))
            else if(board[i][j] == 13):
                pygame.draw.rect(window, colors[6], (j*square_size+450, i*square_size+margin, square_size, square_size))
            else if(board[i][j] == 14):
                pygame.draw.rect(window, colors[7], (j*square_size+450, i*square_size+margin, square_size, square_size))

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
            if(((board[i][j] == 0 or (board[i][j] == 1 or board[i][j] == 2 or board[i][j] == 3 or board[i][j] == 4 
                or board[i][j] == 5 or board[i][j] == 6 or board[i][j] == 7) and i == 19) 
                or (board[i][j] == 0 or (board[i][j] == 1 or board[i][j] == 2 or board[i][j] == 3 or board[i][j] == 4 
                or board[i][j] == 5 or board[i][j] == 6 or board[i][j] == 7)):
                and (board[i+1][j] == 8 or board[i+1][j] == 9 or board[i+1][j] == 10 
                or board[i+1][j] == 11 or board[i+1][j] == 12 or board[i+1][j] == 13 or board[i+1][j] == 14)):
                for i in range(rows):
                    for j in range(cols):
                        if(board[i][j] == 1):
                            board[i][j] = 8
                        else if(board[i][j] == 2):
                            board[i][j] = 9
                        else if(board[i][j] == 3):
                            board[i][j] = 10
                        else if(board[i][j] == 4):
                            board[i][j] = 11
                        else if(board[i][j] == 5):
                            board[i][j] = 12
                        else if(board[i][j] == 6):
                            board[i][j] = 13
                        else if(board[i][j] == 7):
                            board[i][j] = 14

def clearRow():
    rowFull = True
    rows, cols = board.shape[0], board.shape[1]    
    for i in range(rows):
        for j in range(cols):
            if (board[i][j] == 0 or (board[i][j] == 1 or board[i][j] == 2 or board[i][j] == 3 
                or board[i][j] == 4 or board[i][j] == 5 or board[i][j] == 6 or board[i][j] == 7)):
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
        if (board[i][j] == 8 or board[i][j] == 9 or board[i][j] == 10 or board[i][j] == 11 or board[i][j] == 12 or board[i][j] == 13 or board[i][j] == 14):
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
            if (board[i][j] == 1 or board[i][j] == 2 or board[i][j] == 3 or board[i][j] == 4 
                or board[i][j] == 5 or board[i][j] == 6 or board[i][j] == 7):
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
                if((board[i][j] == 1 or board[i][j] == 2 or board[i][j] == 3 or board[i][j] == 4 
                    or board[i][j] == 5 or board[i][j] == 6 or board[i][j] == 7) and j > 0 
                    and (board[i][j-1] != 8 or board[i][j-1] != 9 or board[i][j-1] != 10 
                    or board[i][j-1] != 11 or board[i][j-1] != 12 or board[i][j-1] != 13 or board[i][j-1] != 14)):
                    new_coords.append(i)
                    new_coords.append(j-1)
                    new_pairs.append(list(new_coords))
                    new_coords.pop()
                    new_coords.pop()

    elif(dir == "R"):
        for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                if((board[i][j] == 1 or board[i][j] == 2 or board[i][j] == 3 or board[i][j] == 4 
                    or board[i][j] == 5 or board[i][j] == 6 or board[i][j] == 7) and j < 9 
                    and (board[i][j+1] != 8 or board[i][j+1] != 9 or board[i][j+1] != 10 
                    or board[i][j+1] != 11 or board[i][j+1] != 12 or board[i][j+1] != 13 or board[i][j+1] != 14)):
                    new_coords.append(i)
                    new_coords.append(j+1)
                    new_pairs.append(list(new_coords))
                    new_coords.pop()
                    new_coords.pop()

    elif(dir == "U"):
        rotate(board)

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
        emptyShape = np.zeros((4, 4))

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
        pygame.time.delay(50)
        # One hundred ticks per second
        clock.tick(5)
        
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
                elif keys[pygame.K_UP]:
                    #print("Right")
                    dirx = "U"

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