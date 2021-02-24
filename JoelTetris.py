import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

colors = [(0,255,255),(255,60,245),(255,45,45),(55,255,65),(245,255,50),(255,180,195)]

#Play zone
play_zone_W   = 10
play_zone_H   = 20

#Shapes--matrix of each shape in a 5x5 with shapes determined in matrices
#with possible rotations of each shape

I = [['00100',
      '00100',
      '00100',
      '00100',
      '00100'],
     ['00000',
      '00000',
      '11111',
      '00000',
      '00000']]
B = [['00000',
      '00110',
      '00110',
      '00110',
      '00000'],
     ['00000',
      '00000',
      '01110',
      '01110',
      '00000']]
T = [['00000',
      '00100',
      '00100',
      '01110',
      '00000'],
     ['00000',
      '00010',
      '01110',
      '00010',
      '00000'],
     ['00000',
      '01110',
      '00100',
      '00100',
      '00000'],
     ['00000',
      '01000',
      '01110',
      '01000',
      '00000']]
J = [['00010',
      '00010',
      '01010',
      '01110',
      '00000'],
     ['00000',
      '11110',
      '00010',
      '00110',
      '00000'],
     ['00000',
      '01110',
      '01010',
      '01000',
      '01000'],
     ['00000',
      '01100',
      '01000',
      '01111',
      '00000']]
L = [['00010',
      '00010',
      '00010',
      '01110',
      '00000'],
     ['00000',
      '11110',
      '00010',
      '00010',
      '00000'],
     ['00000',
      '01110',
      '01000',
      '01000',
      '01000'],
     ['00000',
      '01000',
      '01000',
      '01111',
      '00000']]
Z = [['00010',
      '00010',
      '00110',
      '00100',
      '00100'],
     ['00000',
      '11100',
      '00111',
      '00000',
      '00000']]

Shapes = [I, B, T, J, L, Z]
colors = colors = [(0,255,255),(255,60,245),(255,45,45),(55,255,65),(245,255,50),(255,180,195)]

class Shape(object):
    #standard Tetris map size.
    rows = play_zone_W
    cols = play_zone_H

    def __init__(self, cols, rows, shape):
        self.x = cols
        self.y = rows
        self.shape  =  shape
        self.color = random.randint(1, len(colors)-1)
        self.rotation = 0 #Base orientation 

class Tetris:
    
    score  = 0
    grid   = []
    width  = play_zone_W
    height = play_zone_H
    curr_shape = None
    next_shape = None


    def __init(self, width, height): #initialize tetris grid
        self.width = width
        self.height = height
        self.grid = []
        self.score = 0
        for _ in range (height):
            new_row = []
            for _ in range (width): 
                new_row.append(0) #for each row set all values to 0 showing no shapes in grid
            self.grid.append(new_row)

    def make_shape(self): #provide new shape in top middle of grid
        #self.shape = Shape(3,0)
        pass

    def make_next_shape(self):
        #self.shape = Shape(0,0)
        pass

    def collision(self): #handle shapes colliding
        #collision false for now
        #go through 5x5 matrix in nested loop
        #if cell out of bounds\touching shape\bottom of grid
        #check on directions for collision, if true
        #shape collided = true
        pass

    def clear_row(self): #clear rows when row is full
        pass

    def auto_down(self): #moves shape down a space per time automatically
        pass

    def move_down(self): #move shape straight down instantly
        pass

    def move_sidew(self): #move L or R
        pass

    def rotate(self): #rotate
        pass

    def stop(self): #stops shape from moving whether ticking down or collision
        pass
