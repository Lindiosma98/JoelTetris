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

# Color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Determines the upper left block of the play zone grid
#for the play zone to be in the middle of the screen
play_top_x = (width - play_width) // 2
play_top_y = height - play_height


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
        pygame.draw.line(window, WHITE, [play_width, x], [2*play_width, x], 1)
        x += square_size
    # Draw vertical lines
    for _ in range(cols+1):
        pygame.draw.line(window, WHITE, [y+play_width, 0], [y+play_width, play_height], 1)
        y += square_size

        


#puts shape into array (current plan involves active shape being marked by 2's on array)
#def shape(<indicate what shape>):

#IMPORTANT each function involved with movement 
#need to be able to handle not 
#running out of the sides of the game, and
#more importantly collisions with other blocks

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
        window.fill(BLACK)

        # Draw crosshatched pattern on window
        draw_grid(window)

        pygame.display.flip()

        #rotate()
        #move()
        #drop()
        #print(sa)

    pygame.quit()

main()