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
i_counter = 0

# margin to place around the board, just for aesthetic purposes
margin = 50

# Color constants
colors = [(128,0,128),(0,255,255),(0,0,255),(255,165,0),(255,0,0),(0,255,0),(255, 255, 0)]
joel_colors = [(128,0,128),(0,255,255),(0,0,255),(255,165,0),(255,0,0),(0,255,0),(255, 255, 0)]
joelmode_colors = [(128,0,128),(0,255,255),(0,0,255),(255,165,0)]

bg_color = (36,36,36)

shape_number = -1
shape_color = -1

next_sn = -1
next_sc = -1

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

JJM = np.array([
    (8,8,8,0),
    (0,8,0,0),
    (8,8,0,0),
    (0,0,0,0)
    ])
    #50 to help with collison
OJM = np.array([
    (9,9,9,0),
    (9,0,9,0),
    (9,9,9,0),
    (0,0,0,0)
    ])
EJM = np.array([
    (10,10,10,0),
    (10,10,10,0),
    (10,0,0,0),
    (10,10,10,0)
    ])
LJM = np.array([
    (11,0,0,0),
    (11,0,0,0),
    (11,0,0,0),
    (11,11,11,0)
    ])

# Index this to access one of the np arrays above. i.e. "Shapes[2]" would equal J
Shapes = [T, O, J, L, Z, S, I]
JoelShapes = [JJM, OJM, EJM, LJM]

def rotate(board):

    # Create an empty 4x4 array to hold the shape grabbed from the board
    empty_shape = np.zeros((4, 4))

    # lists for storing coordinates
    coords = []
    pairs = []
    empty_columns = 0
    empty = False
    current_color = 0

    # get coordinates of the unique shapes in the board
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if(board[i][j] >= 1 and board[i][j] <= 7):
                current_color = board[i][j]
                coords.append(i)
                coords.append(j)
                pairs.append(list(coords))
                coords.pop()
                coords.pop()
                

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
        empty_shape[pairs[i][0]][pairs[i][1]] = current_color

    pairs.clear()

    #print("Original shape: \n" + str(empty_shape))
    # rotate the recreated shape array
    rotated_shape = np.rot90(empty_shape)

    need_shift = False
    for i in range(empty_shape.shape[0]):
        for j in range(empty_shape.shape[1]):
            if(rotated_shape[i][j] == current_color):
                if (i+minimum_x >= rows):
                    need_shift = True
                    minimum_x = minimum_x - 1 
                if (i+minimum_x < 0):
                    need_shift = True
                    minimum_x = minimum_x + 1 
                if (j+minimum_y >= cols):
                    need_shift = True
                    minimum_y = minimum_y - 1
                if (j+minimum_y < 0):
                    need_shift = True
                    minimum_y = minimum_y + 1
                if (board[i+minimum_x][j+minimum_y] >= 12 and board[i+minimum_x][j+minimum_y] <= 18):
                    return
    
    while (need_shift):
        need_shift = False
        for i in range(empty_shape.shape[0]):
            for j in range(empty_shape.shape[1]):
                if(rotated_shape[i][j] == current_color):
                    if (i+minimum_x >= rows):
                        need_shift = True
                        minimum_x = minimum_x - 1 
                    if (i+minimum_x < 0):
                        need_shift = True
                        minimum_x = minimum_x + 1 
                    if (j+minimum_y >= cols):
                        need_shift = True
                        minimum_y = minimum_y - 1
                    if (j+minimum_y < 0):
                        need_shift = True
                        minimum_y = minimum_y + 1
                    if (board[i+minimum_x][j+minimum_y] >= 12 and board[i+minimum_x][j+minimum_y] <= 18):
                        return
                        
        
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if(board[i][j] == current_color):
                board[i][j] = 0
    #print("Rotated Shape: \n" + str(rotated_shape))

    empty_columns = 0
    empty_rows = 0

    for i in range(4):
        empty = False
        for j in range(4):
            if(empty_shape[j][i] >= 1 and empty_shape[j][i] <= 7):
                empty = True
        if(empty==False):
            empty_columns+=1

    # This chunk here was me attempting to mitigate the shift created by rotation, might use this idea to some extent later
    if(empty_columns != 0):
        for i in range(rotated_shape.shape[0]):
            for j in range(rotated_shape.shape[1]):
                if(rotated_shape[i][j] >= 1 and rotated_shape[i][j] <= 7 or rotated_shape[i][j] >= 12 and rotated_shape[i][j] <= 18):
                    rotated_shape[i-(empty_columns)][j] = current_color
                    rotated_shape[i][j] = 0

        #print("Rotated and Shifted Shape: \n" + str(rotated_shape))
    
    # Draw the rotated shape back to the game board at its original position
    for i in range(empty_shape.shape[0]):
        for j in range(empty_shape.shape[1]):
            if(rotated_shape[i][j] == 1):
                board[i+minimum_x][j+minimum_y] = 1
            elif(rotated_shape[i][j] == 2):
                board[i+minimum_x][j+minimum_y] = 2
            elif(rotated_shape[i][j] == 3):
                board[i+minimum_x][j+minimum_y] = 3
            elif(rotated_shape[i][j] == 4):
                board[i+minimum_x][j+minimum_y] = 4
            elif(rotated_shape[i][j] == 5):
                board[i+minimum_x][j+minimum_y] = 5
            elif(rotated_shape[i][j] == 6):
                board[i+minimum_x][j+minimum_y] = 6
            elif(rotated_shape[i][j] == 7):
                board[i+minimum_x][j+minimum_y] = 7

def rotateJoelMode(board):
    # Create an empty 4x4 array to hold the shape grabbed from the board
    empty_shape = np.zeros((4, 4))

    # lists for storing coordinates
    coords = []
    pairs = []
    empty_columns = 0
    empty = False
    current_color = 0

    # get coordinates of the unique shapes in the board
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if(board[i][j] >= 8 and board[i][j] <= 11):
                current_color = board[i][j]
                coords.append(i)
                coords.append(j)
                pairs.append(list(coords))
                coords.pop()
                coords.pop()
                

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
    for i in range(6):
        empty_shape[pairs[i][0]][pairs[i][1]] = current_color
    

    pairs.clear()

    #print("Original shape: \n" + str(empty_shape))
    # rotate the recreated shape array
    rotated_shape = np.rot90(empty_shape)

    need_shift = False
    for i in range(empty_shape.shape[0]):
        for j in range(empty_shape.shape[1]):
            if(rotated_shape[i][j] == current_color):
                if (i+minimum_x >= rows):
                    need_shift = True
                    minimum_x = minimum_x - 1 
                if (i+minimum_x < 0):
                    need_shift = True
                    minimum_x = minimum_x + 1 
                if (j+minimum_y >= cols):
                    need_shift = True
                    minimum_y = minimum_y - 1
                if (j+minimum_y < 0):
                    need_shift = True
                    minimum_y = minimum_y + 1
                if (board[i+minimum_x][j+minimum_y] >= 19 and board[i+minimum_x][j+minimum_y] <= 22):
                    return
    
    while (need_shift):
        need_shift = False
        for i in range(empty_shape.shape[0]):
            for j in range(empty_shape.shape[1]):
                if(rotated_shape[i][j] == current_color):
                    if (i+minimum_x >= rows):
                        need_shift = True
                        minimum_x = minimum_x - 1 
                    if (i+minimum_x < 0):
                        need_shift = True
                        minimum_x = minimum_x + 1 
                    if (j+minimum_y >= cols):
                        need_shift = True
                        minimum_y = minimum_y - 1
                    if (j+minimum_y < 0):
                        need_shift = True
                        minimum_y = minimum_y + 1
                    if (board[i+minimum_x][j+minimum_y] >= 19 and board[i+minimum_x][j+minimum_y] <= 22):
                        return
                        
        
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if(board[i][j] == current_color):
                board[i][j] = 0
    #print("Rotated Shape: \n" + str(rotated_shape))

    empty_columns = 0
    empty_rows = 0

    for i in range(4):
        empty = False
        for j in range(4):
            if(empty_shape[j][i] >= 8 and empty_shape[j][i] <= 11):
                empty = True
        if(empty==False):
            empty_columns+=1

    # This chunk here was me attempting to mitigate the shift created by rotation, might use this idea to some extent later
    if(empty_columns != 0):
        for i in range(rotated_shape.shape[0]):
            for j in range(rotated_shape.shape[1]):
                if(rotated_shape[i][j] >= 8 and rotated_shape[i][j] <= 11 or rotated_shape[i][j] >= 19 and rotated_shape[i][j] <= 22):
                    rotated_shape[i-(empty_columns)][j] = current_color
                    rotated_shape[i][j] = 0

        #print("Rotated and Shifted Shape: \n" + str(rotated_shape))
    
    # Draw the rotated shape back to the game board at its original position
    for i in range(empty_shape.shape[0]):
        for j in range(empty_shape.shape[1]):
            if(rotated_shape[i][j] == 8):
                board[i+minimum_x][j+minimum_y] = 8
            elif(rotated_shape[i][j] == 9):
                board[i+minimum_x][j+minimum_y] = 9
            elif(rotated_shape[i][j] == 10):
                board[i+minimum_x][j+minimum_y] = 10
            elif(rotated_shape[i][j] == 11):
                board[i+minimum_x][j+minimum_y] = 11

def generateShapeIndex():
    shape_number = random.randrange(7)

    return shape_number

def generateShapeIndexJoelMode():
    shape_number = random.randrange(4)

    return shape_number

# Places the first shape of the game. Should be randomly generated, but that can't happen until all shapes can be moved without a segfault.
def placeStartingShape(window, board):
    shape_number = generateShapeIndex()
    next_sn = generateShapeIndex()

    # Change this index to change shape
    shape = Shapes[shape_number]
    
    for i in range(shape.shape[0]):
        for j in range(shape.shape[1]):
            # only draw squares in cells populated with a 1-4
            board[i][j+4] = shape[i][j]

def placeStartingShapeJoelMode(window, board):
    shape_number = generateShapeIndexJoelMode()
    next_sn = generateShapeIndexJoelMode()
    print("Shape_Num")
    print(shape_number)
    print("next_sn")
    print(next_sn)

    # Change this index to change shape
    shape = JoelShapes[shape_number]
    print("Shape")
    print(shape)
    
    for i in range(shape.shape[0]):
        for j in range(shape.shape[1]):
            # only draw squares in cells populated with a 1-4
            board[i][j+4] = shape[i][j]

# Spawns new shape at the top of the board when there are no active blocks
def spawnShape(window, board):
    global next_sn
    active = False
    shape_number = next_sn
    #print(shape_number)
    shape = Shapes[shape_number]
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if(board[i][j] >= 1 and board[i][j] <= 7):
                active = True

    if(active == False):
        next_sn = generateShapeIndex()
        for i in range(shape.shape[0]):
            for j in range(shape.shape[1]):
                # only draw squares in cells populated with 1-7
                if(shape[i][j] == 1):
                    board[i][j+4] = 1 # 12 when frozen
                elif(shape[i][j] == 2):
                    board[i][j+4] = 2 # 13 when frozen
                elif(shape[i][j] == 3):
                    board[i][j+4] = 3 # 14 when frozen
                elif(shape[i][j] == 4):
                    board[i][j+4] = 4 # 15 when frozen
                elif(shape[i][j] == 5):
                    board[i][j+4] = 5 # 16 when frozen
                elif(shape[i][j] == 6):
                    board[i][j+4] = 6 # 17 when frozen
                elif(shape[i][j] == 7):
                    board[i][j+4] = 7 # 18 when frozen

def spawnShapeJoelMode(window, board):
    global next_sn
    active = False
    shape_number = next_sn
    #print(shape_number)
    shape = JoelShapes[shape_number]
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if(board[i][j] >= 8 and board[i][j] <= 11):
                active = True

    if(active == False):
        next_sn = generateShapeIndexJoelMode()
        for i in range(shape.shape[0]):
            for j in range(shape.shape[1]):
                # only draw squares in cells populated with 8-11
                if(shape[i][j] == 8):
                    board[i][j+4] = 8 # 19 when frozen
                elif(shape[i][j] == 9):
                    board[i][j+4] = 9 # 20 when frozen
                elif(shape[i][j] == 10):
                    board[i][j+4] = 10 # 21 when frozen
                elif(shape[i][j] == 11):
                    board[i][j+4] = 11 # 22 when frozen

# Fill the squares on the grid with color. Only fills cells populated with a 1
def drawShapes(window, board):
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if(board[i][j] == 1):
                pygame.draw.rect(window, colors[0], (j*square_size+450, i*square_size+margin, square_size, square_size))
            elif(board[i][j] == 2):
                pygame.draw.rect(window, colors[1], (j*square_size+450, i*square_size+margin, square_size, square_size))
            elif(board[i][j] == 3):
                pygame.draw.rect(window, colors[2], (j*square_size+450, i*square_size+margin, square_size, square_size))
            elif(board[i][j] == 4):
                pygame.draw.rect(window, colors[3], (j*square_size+450, i*square_size+margin, square_size, square_size))
            elif(board[i][j] == 5):
                pygame.draw.rect(window, colors[4], (j*square_size+450, i*square_size+margin, square_size, square_size))
            elif(board[i][j] == 6):
                pygame.draw.rect(window, colors[5], (j*square_size+450, i*square_size+margin, square_size, square_size))
            elif(board[i][j] == 7):
                pygame.draw.rect(window, colors[6], (j*square_size+450, i*square_size+margin, square_size, square_size))

def drawShapesJoelMode(window, board):
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if(board[i][j] == 8):
                pygame.draw.rect(window, joelmode_colors[0], (j*square_size+450, i*square_size+margin, square_size, square_size))
            elif(board[i][j] == 9):
                pygame.draw.rect(window, joelmode_colors[1], (j*square_size+450, i*square_size+margin, square_size, square_size))
            elif(board[i][j] == 10):
                pygame.draw.rect(window, joelmode_colors[2], (j*square_size+450, i*square_size+margin, square_size, square_size))
            elif(board[i][j] == 11):
                pygame.draw.rect(window, joelmode_colors[3], (j*square_size+450, i*square_size+margin, square_size, square_size))

def drawNextShape(window, board):
    start_x = -1
    start_y = -1
    shape = Shapes[next_sn]
    for i in range(shape.shape[0]):
        for j in range(shape.shape[1]):
            if(shape[i][j] >= 1 and shape[i][j] <= 7):
                if(start_x == -1):
                    start_x = i
                    start_y = j
                #print(int(shape[i][j]) - 1)
                ns = int(shape[i][j]) - 1
                pygame.draw.rect(window, colors[ns], ((10+j-start_y) * square_size, (10+i-start_x) * square_size+margin, square_size, square_size)) 
                #pygame.draw.rect(window, colors[ns], (j*square_size+450, i*square_size+margin, square_size, square_size))

def drawNextShapeJoelMode(window, board):
    start_x = -1
    start_y = -1
    print(next_sn)
    shape = JoelShapes[next_sn]
    print("next shape")
    print(shape)
    for i in range(shape.shape[0]):
        for j in range(shape.shape[1]):
            if(shape[i][j] >= 8 and shape[i][j] <= 11):
                if(start_x == -1):
                    start_x = i
                    start_y = j
                print("ns")
                print(int(shape[i][j]) - 8)
                ns = int(shape[i][j]) - 8
                pygame.draw.rect(window, joelmode_colors[ns], ((10+j-start_y) * square_size, (10+i-start_x) * square_size+margin, square_size, square_size)) 
                #pygame.draw.rect(window, colors[ns], (j*square_size+450, i*square_size+margin, square_size, square_size))

# Draws all frozen shapes (2) to the board
def drawFrozenShapes(window, board):
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if(board[i][j] == 12):
                pygame.draw.rect(window, colors[0], (j*square_size+450, i*square_size+margin, square_size, square_size))
            elif(board[i][j] == 13):
                pygame.draw.rect(window, colors[1], (j*square_size+450, i*square_size+margin, square_size, square_size))
            elif(board[i][j] == 14):
                pygame.draw.rect(window, colors[2], (j*square_size+450, i*square_size+margin, square_size, square_size))
            elif(board[i][j] == 15):
                pygame.draw.rect(window, colors[3], (j*square_size+450, i*square_size+margin, square_size, square_size))
            elif(board[i][j] == 16):
                pygame.draw.rect(window, colors[4], (j*square_size+450, i*square_size+margin, square_size, square_size))
            elif(board[i][j] == 17):
                pygame.draw.rect(window, colors[5], (j*square_size+450, i*square_size+margin, square_size, square_size))
            elif(board[i][j] == 18):
                pygame.draw.rect(window, colors[6], (j*square_size+450, i*square_size+margin, square_size, square_size))

def drawFrozenShapesJoelMode(window, board):
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if(board[i][j] == 19):
                pygame.draw.rect(window, joelmode_colors[0], (j*square_size+450, i*square_size+margin, square_size, square_size))
            elif(board[i][j] == 20):
                pygame.draw.rect(window, joelmode_colors[1], (j*square_size+450, i*square_size+margin, square_size, square_size))
            elif(board[i][j] == 21):
                pygame.draw.rect(window, joelmode_colors[2], (j*square_size+450, i*square_size+margin, square_size, square_size))
            elif(board[i][j] == 22):
                pygame.draw.rect(window, joelmode_colors[3], (j*square_size+450, i*square_size+margin, square_size, square_size))

# This function is essentially the same as move(), but does not have a direction parameter
# Need to vary the fall speed somehow
def fall(window, board):
    coords = []
    pairs = []

    rows, cols = board.shape[0], board.shape[1]

    for i in range(rows):
        for j in range(cols):
            if(board[i][j] >= 1 and board[i][j] <= 7):
                coords.append(i)
                coords.append(j)
                pairs.append(list(coords))
                coords.pop()
                coords.pop()

    new_pairs = []
    new_coords = []
    curr_shape = -1

    for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                if((board[i][j] >= 1 and board[i][j] <= 7) and i < 19):
                    curr_shape = board[i][j]
                    new_coords.append(i+1)
                    new_coords.append(j)
                    new_pairs.append(list(new_coords))
                    new_coords.pop()
                    new_coords.pop()
                    if (i+1 >= rows or board[i+1][j] >= 8):
                        return


    if(len(new_pairs) == 4):
        # for each element in new_pairs (coordinates)
        for i in range(4):
            # set old pairs to 0
            board[pairs[i][0]][pairs[i][1]] = 0
        for i in range(4):
            # set new pairs to 1
            board[new_pairs[i][0]][new_pairs[i][1]] = curr_shape #Problem lies here for colors
    #print(new_pairs)
    new_coords.clear()
    new_pairs.clear()

def fallJoelMode(window, board):
    coords = []
    pairs = []

    rows, cols = board.shape[0], board.shape[1]

    for i in range(rows):
        for j in range(cols):
            if(board[i][j] >= 8 and board[i][j] <= 11):
                coords.append(i)
                coords.append(j)
                pairs.append(list(coords))
                coords.pop()
                coords.pop()

    new_pairs = []
    new_coords = []
    curr_shape = -1

    for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                if((board[i][j] >= 8 and board[i][j] <= 11) and i < 19):
                    curr_shape = board[i][j]
                    new_coords.append(i+1)
                    new_coords.append(j)
                    new_pairs.append(list(new_coords))
                    new_coords.pop()
                    new_coords.pop()
                    if (i+1 >= rows or board[i+1][j] >= 19):
                        return


    if(len(new_pairs) == 6):
        # for each element in new_pairs (coordinates)
        for i in range(6):
            # set old pairs to 0
            board[pairs[i][0]][pairs[i][1]] = 0
        for i in range(6):
            # set new pairs to 1
            board[new_pairs[i][0]][new_pairs[i][1]] = curr_shape #Problem lies here for colors
    elif(len(new_pairs) == 8):
        # for each element in new_pairs (coordinates)
        for i in range(8):
            # set old pairs to 0
            board[pairs[i][0]][pairs[i][1]] = 0
        for i in range(8):
            # set new pairs to 1
            board[new_pairs[i][0]][new_pairs[i][1]] = curr_shape #Problem lies here for colors
    elif(len(new_pairs) == 10):
        # for each element in new_pairs (coordinates)
        for i in range(10):
            # set old pairs to 0
            board[pairs[i][0]][pairs[i][1]] = 0
        for i in range(10):
            # set new pairs to 1
            board[new_pairs[i][0]][new_pairs[i][1]] = curr_shape #Problem lies here for colors
    #print(new_pairs)
    new_coords.clear()
    new_pairs.clear()

# freezes a shape if it touches the bottom
def freezeShapes(window, board):
    rows, cols = board.shape[0], board.shape[1]    
    for i in range(rows):
        for j in range(cols):
            if(((board[i][j] >= 1 and board[i][j] <=7 ) and i == 19) or (board[i][j] >= 1 and board[i][j] <=7 )
                and (board[i+1][j] >= 8 )):
                for i in range(rows):
                    for j in range(cols):
                        if(board[i][j] == 1):
                            board[i][j] = 12
                        elif(board[i][j] == 2):
                            board[i][j] = 13
                        elif(board[i][j] == 3):
                            board[i][j] = 14
                        elif(board[i][j] == 4):
                            board[i][j] = 15
                        elif(board[i][j] == 5):
                            board[i][j] = 16
                        elif(board[i][j] == 6):
                            board[i][j] = 17
                        elif(board[i][j] == 7):
                            board[i][j] = 18

def freezeShapesJoelMode(window, board):
    rows, cols = board.shape[0], board.shape[1]    
    for i in range(rows):
        for j in range(cols):
            if(((board[i][j] >= 8 and board[i][j] <=11 ) and i == 19) or (board[i][j] >= 8 and board[i][j] <=11 )
                and (board[i+1][j] >= 19 )):
                for i in range(rows):
                    for j in range(cols):
                        if(board[i][j] == 8):
                            board[i][j] = 19
                        elif(board[i][j] == 9):
                            board[i][j] = 20
                        elif(board[i][j] == 10):
                            board[i][j] = 21
                        elif(board[i][j] == 11):
                            board[i][j] = 22

def clearRow(cleared_rows):
    rowFull = True    
    rows, cols = board.shape[0], board.shape[1]    
    for i in range(rows):
        for j in range(cols):
            if (board[i][j] == 0 or (board[i][j] >= 1 and board[i][j] <=7)):
                rowFull = False
        if rowFull:
            cleared_rows = cleared_rows + 1
            for k in range(rows):
                for l in range(cols):
                    if k + 1 < i:
                        board[i-k][l] = board[i-k-1][l]
        rowFull = True
    return cleared_rows
  
def clearRowJoelMode(cleared_rows):
    rowFull = True    
    rows, cols = board.shape[0], board.shape[1]    
    for i in range(rows):
        for j in range(cols):
            if (board[i][j] == 0 or (board[i][j] >= 8 and board[i][j] <=11)):
                rowFull = False
        if rowFull:
            cleared_rows = cleared_rows + 1
            for k in range(rows):
                for l in range(cols):
                    if k + 1 < i:
                        board[i-k][l] = board[i-k-1][l]
        rowFull = True
    return cleared_rows

def updateScore(rowscleared, difficulty, score):
    if difficulty == 1:
        if rowscleared == 1:
            score = score + 40
        elif rowscleared == 2:
            score = score + 100
        elif rowscleared == 3:
            score = score + 300
        elif rowscleared >= 4:
            score = score + 1200
    elif difficulty == 2:
        if rowscleared == 1:
            score = score + 80
        elif rowscleared == 2:
            score = score + 200
        elif rowscleared == 3:
            score = score + 600
        elif rowscleared >= 4:
            score = score + 2400
    elif difficulty == 3:
        if rowscleared == 1:
            score = score + 120
        elif rowscleared == 2:
            score = score + 300
        elif rowscleared == 3:
            score = score + 900
        elif rowscleared >= 4:
            score = score + 3600
    elif difficulty == 9:
        if rowscleared == 1:
            score = score + 400
        elif rowscleared == 2:
            score = score + 1000
        elif rowscleared == 3:
            score = score + 3000
        elif rowscleared >= 4:
            score = score + 12000
    elif difficulty > 9:
        if rowscleared == 1:
            score = score + (40 * (difficulty + 1))
        elif rowscleared == 2:
            score = score + (100 * (difficulty + 1))
        elif rowscleared == 3:
            score = score + (300 * (difficulty + 1))
        elif rowscleared >= 4:
            score = score + (1200 * (difficulty + 1))
    return score

# Draws crosshatched pattern on canvas
def draw_grid(window):
    x, y = 0, 0

    # Draw horizontal lines
    for _ in range(rows+1):
        # params: (window name, line color, [line start x, line start y], [line end x, line end y], thickness)
        pygame.draw.line(window, (69,69,69), [(width//2)+margin, y+margin], [width-margin, y+margin], 1)
        y += square_size

    # Draw vertical lines
    for _ in range(cols+1):
        # params: (window name, line color, [line start x, line start y], [line end x, line end y], thickness)
        pygame.draw.line(window, (69,69,69), [width//2+x+margin, 0+margin], [width//2+x+margin, height-margin], 1)
        x += square_size

def checkGameState():
    rows, cols = board.shape[0], board.shape[1] 
    for i in range(cols):
        if (board[1][i] >= 8):
            return True
    return False

def checkGameStateJoelMode():
    rows, cols = board.shape[0], board.shape[1] 
    for i in range(cols):
        if (board[1][i] >= 19):
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
            if (board[i][j] >= 1 and board[i][j] <= 7):
                coords.append(i)
                coords.append(j)
                pairs.append(list(coords))
                coords.pop()
                coords.pop()

    #print(pairs)
    new_pairs = []
    new_coords = []
    curr_shape = -1

    if(dir == "L"):
        # Get all coordinates one cell to the left of current 1's
        for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                if((board[i][j] >= 1 and board[i][j] <= 7) and (j-1 >= 0) and (board[i][j-1] < 8)):
                    curr_shape = board[i][j]
                    new_coords.append(i)
                    new_coords.append(j-1)
                    new_pairs.append(list(new_coords))
                    new_coords.pop()
                    new_coords.pop()

    elif(dir == "R"):
        for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                if((board[i][j] >= 1 and board[i][j] <= 7) and (j+1 < cols) and (board[i][j+1] < 8)):
                    curr_shape = board[i][j]
                    new_coords.append(i)
                    new_coords.append(j+1)
                    new_pairs.append(list(new_coords))
                    new_coords.pop()
                    new_coords.pop()

    elif(dir == "U"):
        rotate(board)

    elif (dir == "D"):
        # emptyShape = np.zeros((4, 4))
        fall(window, board)

    # Prevents segfault by ensuring all coordinates in the new_pairs list are on the board
    if(len(new_pairs) == 4):
        # for each element in new_pairs (coordinates)
        for i in range(4):
            # set old pairs to 0
            board[pairs[i][0]][pairs[i][1]] = 0
        for i in range(4):
            # set new pairs to 1
            board[new_pairs[i][0]][new_pairs[i][1]] = curr_shape


    # Empty the coordinate lists for the next call to this function
    #pairs.clear()
    #coords.clear()
    new_coords.clear()
    new_pairs.clear()

def moveJoelMode(window, dir):
    # simple list of shape coordinate values (aka where the 1's are in the board)
    coords = []

    # the same list as above, but converted into list of lists (each of length 2 for easy and sensible indexing)
    pairs = []
    
    # grabbing max row and col values
    rows, cols = board.shape[0], board.shape[1]
    
    # loop through board array, store locations of 1's (aka where the shape currently is located)
    for i in range(rows):
        for j in range(cols):
            if (board[i][j] >= 8 and board[i][j] <= 11):
                coords.append(i)
                coords.append(j)
                pairs.append(list(coords))
                coords.pop()
                coords.pop()

    #print(pairs)
    new_pairs = []
    new_coords = []
    curr_shape = -1

    if(dir == "L"):
        # Get all coordinates one cell to the left of current 1's
        for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                if((board[i][j] >= 8 and board[i][j] <= 11) and (j-1 >= 0) and (board[i][j-1] < 19)):
                    curr_shape = board[i][j]
                    new_coords.append(i)
                    new_coords.append(j-1)
                    new_pairs.append(list(new_coords))
                    new_coords.pop()
                    new_coords.pop()

    elif(dir == "R"):
        for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                if((board[i][j] >= 8 and board[i][j] <= 11) and (j+1 < cols) and (board[i][j+1] < 19)):
                    curr_shape = board[i][j]
                    new_coords.append(i)
                    new_coords.append(j+1)
                    new_pairs.append(list(new_coords))
                    new_coords.pop()
                    new_coords.pop()

    elif(dir == "U"):
        rotateJoelMode(board)

    elif (dir == "D"):
        # emptyShape = np.zeros((4, 4))
        fallJoelMode(window, board)

    # Prevents segfault by ensuring all coordinates in the new_pairs list are on the board
    if(len(new_pairs) == 6):
        # for each element in new_pairs (coordinates)
        for i in range(6):
            # set old pairs to 0
            board[pairs[i][0]][pairs[i][1]] = 0
        for i in range(6):
            # set new pairs to 1
            board[new_pairs[i][0]][new_pairs[i][1]] = curr_shape
    elif(len(new_pairs) == 8):
        # for each element in new_pairs (coordinates)
        for i in range(8):
            # set old pairs to 0
            board[pairs[i][0]][pairs[i][1]] = 0
        for i in range(8):
            # set new pairs to 1
            board[new_pairs[i][0]][new_pairs[i][1]] = curr_shape
    if(len(new_pairs) == 10):
        # for each element in new_pairs (coordinates)
        for i in range(10):
            # set old pairs to 0
            board[pairs[i][0]][pairs[i][1]] = 0
        for i in range(10):
            # set new pairs to 1
            board[new_pairs[i][0]][new_pairs[i][1]] = curr_shape

    # Empty the coordinate lists for the next call to this function
    #pairs.clear()
    #coords.clear()
    new_coords.clear()
    new_pairs.clear()

def JoelBlockGame():

    replay = ""
    play_on = True
    
    # Initialization stuff
    score = 0
    difficulty = 0
    not_run = 10
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Joel Block Game")
    image = pygame.image.load("logo.png")
    gameIcon = pygame.image.load('icon.png')
    pygame.display.set_icon(gameIcon)
    pygame.font.init()
    myfont = pygame.font.Font("comfortaa_regular.ttf", 40)
    clock = pygame.time.Clock()
    game_over = False
    random.seed()
    dirx = ""
    cleared_rows = 0

    # Place the first shape
    placeStartingShape(window, board)
    
    while play_on:
        for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                board[i][j] = 0
    # Game loop regular Joel Block Game
        game_over = False
        while not game_over:
            # Changes block movement speed
            pygame.time.delay(75)
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
                    elif keys[pygame.K_UP]:
                        #print("Right")
                        dirx = "U"
                    elif keys[pygame.K_DOWN]:
                        #print("Down")
                        dirx = "D"

            # Move the block in the direction dirx
            move(window, dirx)
            dirx = ""

            # Prevent any shapes that have hit the bottom of the board from moving
            freezeShapes(window, board)

            # Clear the screen and set the screen background
            window.fill(bg_color)

            # Print the board state in console
            print(board)

            # Draw frozen shapes to the screen
            drawFrozenShapes(window, board)

            # Temp value for cleared rows for score tracking
            temp_cleared_rows = cleared_rows
        
            # Clears a full row of squares
            cleared_rows = clearRow(cleared_rows)

            if cleared_rows < 5:
                difficulty = 1
            elif cleared_rows < 10:
                difficulty = 2
            elif cleared_rows < 15:
                difficulty = 3
            elif cleared_rows < 20:
                difficulty = 4
            elif cleared_rows < 25:
                difficulty = 5
            elif cleared_rows < 30:
                difficulty = 6
            elif cleared_rows < 35:
                difficulty = 7
            elif cleared_rows < 40:
                difficulty = 8
            elif cleared_rows < 45:
                difficulty = 9
            elif cleared_rows >= 50:
                difficulty = 10
            
            
            # Updates score based on rows cleared
            score = updateScore((cleared_rows - temp_cleared_rows), difficulty, score)
        
            game_over = checkGameState() 

            # Spawn a new shape when all shapes are frozen
            spawnShape(window, board)

            # Draw shape to screen
            drawShapes(window, board)

            drawNextShape(window, board)

            # Block falls downward one unit every tick
            if (difficulty - not_run >= 0):
                fall(window, board)
                not_run = 10
            else:
                not_run = not_run - 1

        # Draw crosshatched pattern on window
            draw_grid(window)
        
            # Draw game logo
            window.blit(image, (24, 34))
        
            # Draw score and score text on window
            scoreText = myfont.render(f"Score: {score}", True, (255,255,255))
            lineText = myfont.render(f"Level: {difficulty}", True, (255,255,255))
            window.blit(scoreText, (30, 300))
            window.blit(lineText, (30, 350))
        
            pygame.display.update()

        pygame.quit()

        replay = input("Replay Joel Block Game? (y/n) ")
        replay = replay.lower()
        while replay != "y" and replay != "n":
            print("Incorrect input")
            replay = input("Replay Joel Block Game? (y/n) ")

        if replay == "y":
            JoelBlockGame()
        elif replay == "n":
            main()
             
def JoelMode():

    replay = ""
    play_on = True
    
    # Initialization stuff
    score = 0
    difficulty = 0
    not_run = 10
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Joel Block Game")
    image = pygame.image.load("logo.png")
    gameIcon = pygame.image.load('icon.png')
    pygame.display.set_icon(gameIcon)
    pygame.font.init()
    myfont = pygame.font.Font("comfortaa_regular.ttf", 40)
    clock = pygame.time.Clock()
    game_over = False
    random.seed()
    dirx = ""
    cleared_rows = 0

    # Place the first shape
    placeStartingShapeJoelMode(window, board)
    
    while play_on:
        for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                board[i][j] = 0
    # Game loop regular Joel Block Game
        game_over = False
        while not game_over:
            # Changes block movement speed
            pygame.time.delay(75)
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
                    elif keys[pygame.K_UP]:
                        #print("Right")
                        dirx = "U"
                    elif keys[pygame.K_DOWN]:
                        #print("Down")
                        dirx = "D"

            # Move the block in the direction dirx
            moveJoelMode(window, dirx)
            dirx = ""

            # Prevent any shapes that have hit the bottom of the board from moving
            freezeShapesJoelMode(window, board)

            # Clear the screen and set the screen background
            window.fill(bg_color)

            # Print the board state in console
            #print(board)

            # Draw frozen shapes to the screen
            drawFrozenShapesJoelMode(window, board)

            # Temp value for cleared rows for score tracking
            temp_cleared_rows = cleared_rows
        
            # Clears a full row of squares
            cleared_rows = clearRowJoelMode(cleared_rows)

            if cleared_rows < 5:
                difficulty = 1
            elif cleared_rows < 10:
                difficulty = 2
            elif cleared_rows < 15:
                difficulty = 3
            elif cleared_rows < 20:
                difficulty = 4
            elif cleared_rows < 25:
                difficulty = 5
            elif cleared_rows < 30:
                difficulty = 6
            elif cleared_rows < 35:
                difficulty = 7
            elif cleared_rows < 40:
                difficulty = 8
            elif cleared_rows < 45:
                difficulty = 9
            elif cleared_rows >= 50:
                difficulty = 10
            
            
            # Updates score based on rows cleared
            score = updateScore((cleared_rows - temp_cleared_rows), difficulty, score)
        
            game_over = checkGameStateJoelMode() 

            # Spawn a new shape when all shapes are frozen
            spawnShapeJoelMode(window, board)

            # Draw shape to screen
            drawShapesJoelMode(window, board)

            drawNextShapeJoelMode(window, board)

            # Block falls downward one unit every tick
            if (difficulty - not_run >= 0):
                fallJoelMode(window, board)
                not_run = 10
            else:
                not_run = not_run - 1

        # Draw crosshatched pattern on window
            draw_grid(window)
        
            # Draw game logo
            window.blit(image, (24, 34))
        
            # Draw score and score text on window
            scoreText = myfont.render(f"Score: {score}", True, (255,255,255))
            lineText = myfont.render(f"Level: {difficulty}", True, (255,255,255))
            window.blit(scoreText, (30, 300))
            window.blit(lineText, (30, 350))
        
            pygame.display.update()

        pygame.quit()

        replay = input("Replay Joel Block Game? (y/n) ")
        replay = replay.lower()
        while replay != "y" and replay != "n":
            print("Incorrect input")
            replay = input("Replay Joel Block Game? (y/n) ")

        if replay == "y":
            JoelMode()
        elif replay == "n":
            main()

def main():
    replay = ""
    play_on = True

    while play_on:
        print ("""
        1. Joel Block Game
        2. Joel Mode
        3. Exit Game
        """)

        choice = int(input("Pick menu option of your choosing: "))

        while choice < 1 or choice > 3:
            print("No such option, try again")
            choice = int(input("Pick menu option of your choosing: "))

        if choice == 1:
            JoelBlockGame()
        elif choice == 2:
            JoelMode()
        elif choice == 3:
            print("Thanks for playing this ballin game")
            quit()
   
    pygame.quit()

main()