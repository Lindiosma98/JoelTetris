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

# Numpy arrays for shapes. 4x4. Column-major. 
T = np.array([(0,1,0,0),(1,1,0,0),(0,1,0,0),(0,0,0,0)])
O = np.array([(1,1,0,0),(1,1,0,0),(0,0,0,0),(0,0,0,0)])
J = np.array([(0,0,1,0),(1,1,1,0),(0,0,0,0),(0,0,0,0)])
L = np.array([(0,0,0,0),(1,1,1,0),(0,0,1,0),(0,0,0,0)])
Z = np.array([(1,0,0,0),(1,1,0,0),(0,1,0,0),(0,0,0,0)])
S = np.array([(0,1,0,0),(1,1,0,0),(1,0,0,0),(0,0,0,0)])
I = np.array([(0,1,0,0),(0,1,0,0),(0,1,0,0),(0,1,0,0)])

# Upper-Left Corner of Grid
play_top_x = 450 
play_top_y = 50

class Shape:

    # The minimum and maximum values a piece can have for its coordinates: (450, 50), (750, 650)
    left_bound = 450
    right_bound = 750
    up_bound = 50
    down_bound = 650

    '''def __init__(self, width, height, shape, color):
        self.x = width
        self.y = height
        self.shape = shape
        self.color = color
        self.rotation = 0 #Base orientation '''

    '''def draw(window, x, y):
        pygame.draw.rect(window, colors[2], (x, y, square_size, square_size))'''


def draw(window, x, y):
        pygame.draw.rect(window, colors[2], (x, y, square_size, square_size))


# Currently, this is the function that is used to display a shape. Could be streamlined by implementing the draw method above into it. Easy fix.
def fillSquares(window, arr, rows, cols):
    for i in range(rows):
        for j in range(cols):
            #print(rows, cols)
            if(arr[i][j] == 1):
                pygame.draw.rect(window, colors[2], (arr[i][j] * 30 * i + 450, arr[i][j] * 30 * j + 50, square_size, square_size))
                print(arr[i][j] * 30 * i + 450, arr[i][j] * 30 * j)

            #draw(window, (arr[i][j] * 30 * i) + 450, (arr[i][j] * 30 * j))


#squareArray = [[0]*cols]*rows
#0 = no block, 1 = stationary block, 2 = active shape
#sa = np.array(squareArray)
#collision = False

#Create class for pieces

#Create grid 10x20 that has 0 throughout to show no blocks
#stopped_pieces keeps track of spaces of pieces that are
#locked into the grid by game collision rules
def create_grid(stopped_pieces = {}):
    grid = [[0 for _ in range(10)] for _ in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i,j) in stopped_pieces:
                stopped = stopped_pieces[(i,j)]
                grid[i][j] = stopped
    return grid

# Draws crosshatched pattern on canvas
def draw_grid(window):
    x, y = 0, 0

    # Draw horizontal lines
    for _ in range(rows+1):
        pygame.draw.line(window, colors[1], [(width/2)+margin, y+margin], [width-margin, y+margin], 1)
        y += square_size

    # Draw vertical lines
    for _ in range(cols+1):
        pygame.draw.line(window, colors[1], [width/2+x+margin, 0+margin], [width/2+x+margin, height-margin], 1)
        x += square_size

        


#puts shape into array (current plan involves active shape being marked by 2's on array)
#def shape(<indicate what shape>):

#rotates shape
#def rotate(<indicate direction>):

#def move(<indicate direction>):

#def drop(<indicate fast or slow>):

def main():

    # Initialization stuff
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Joel Tetris.inc")
    clock = pygame.time.Clock()
    game_over = False

    stopped_pieces = {} #Dictionary for pieces placed and not moving on grid in form
                            # (x,y): 0,1,2 where 0-no block, 1-curr block moving, 2-block done moving

    # Game loop
    while not game_over:
 
        # Ten ticks per second
        clock.tick(10)
         
        # Event handling (user input)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                game_over = True 
     
         
        # Clear the screen and set the screen background
        window.fill(colors[0])

        # Store cell states (0 = no block, 1 = current block moving, 2 = block done moving)
        stopped_pieces = create_grid(stopped_pieces)

        # Draw crosshatched pattern on window
        draw_grid(window)

        # Demonstrating drawing a block to screen. Change "T" to another shape name to display corresponding shape
        fillSquares(window, T, T.shape[0], T.shape[1])
    
        pygame.display.flip()

        #rotate()
        #move()
        #drop()
        #print(sa)

    pygame.quit()

main()