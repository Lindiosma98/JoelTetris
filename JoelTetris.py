import math
import random
import pygame
import numpy as np
import tkinter as tk
from tkinter import messagebox

width = 800 #Screen
height = 700 #Screen
play_width = 300 #Play zone
play_height = 600 #Play zone
square_size = 30 #Size per block
rows = 20
cols = 10

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
    stopped_pieces = {} #Dictionary for pieces placed and not moving on grid in form
                        # (x,y): 0,1,2 where 0-no block, 1-curr block moving, 2-block done moving

    run = True
    while run:
        collision = False
        #shape()
        while not(collision):
            pass
            #take keyboard inputs here
            #rotate()
            #move()
            #drop()
    print(sa)
    #put display stuff here

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Joel Tetris.inc")

main()