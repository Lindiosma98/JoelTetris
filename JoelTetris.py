import math
import random
import pygame
import numpy as np
import tkinter as tk
from tkinter import messagebox

colors = [(0,255,255),(255,60,245),(255,45,45),(55,255,65),(245,255,50),(255,180,195)]


#Play zone
play_zone_W   = 40
play_zone_H   = 40

marked_boxes = [[0]*play_zone_W]*play_zone_H
mb = np.array(marked_boxes)
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
    play_zone_H = play_zone_W
    cols = play_zone_H

    def __init__(self, cols, play_zone_H, shape):
        self.x = cols
        self.y = play_zone_H
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

    def clear_row(self): #clear play_zone_H when row is full
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

class cube(object):
    w = 500
    h = 500
    def __init__(self,start,dirnx=0,dirny=1,color=(255,0,0)):
        self.pos = start
        self.dirnx = 0
        self.dirny = 1
        self.color = color

    def move(self):
        mb[self.pos[1]][self.pos[0]] = 0
        keypress = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    keypress = True

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    keypress = True
        if False:
            pass
        elif keypress:
            if self.dirnx == -1 and self.pos[0] <= 0:
                pass
            elif self.dirnx == 1 and self.pos[0] >= play_zone_W-1:
                pass
            else:
                self.pos = (self.pos[0] + self.dirnx, self.pos[1])
        else:
            self.pos = (self.pos[0], self.pos[1] + 1)
        
        mb[self.pos[1]][self.pos[0]] = 2

    def collision():
        hit = False
        #if self.pos[1] >= play_zone_H-1:
         #   hit = True
        #elif self.pos[1] + 1 == 1:
            #hit = True
        return()

    def draw(self, surface, eyes=False):
        disw = self.w // play_zone_W
        dish = self.h // play_zone_H
        i = self.pos[0] 
        j = self.pos[1]
    
        pygame.draw.rect(surface, self.color, (i*disw+1,j*dish+1, disw-2, dish-2))

#def shape()


def randomSquare():

    x = random.randrange(play_zone_W)
    y = 0
        
    return (x,y)

def drawGrid(w, h, surface):
    sizeBtwnW = w // play_zone_W
    sizeBtwnH = h // play_zone_H

    x = 0
    y = 0
    for l in range(play_zone_W):
        x = x + sizeBtwnW
        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))

    for l in range(play_zone_H):
        y = y + sizeBtwnH
        pygame.draw.line(surface, (255,255,255), (0,y),(h,y))

def main():
    currPos = 0
    width = 500
    height = 500
    #play_zone_H = []
    #cols = []
    run = True
    square = cube(randomSquare(), color=(0,255,0))

    #square.append()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((width, height))

    #print(len(square))

    while run:
        pygame.time.delay(50)
        clock.tick(10)

        if not(square.pos[1] >= play_zone_H-1):
            square.move()
        else:
            pass
            #print(mb)


        window.fill((0,0,0))
        square.draw(window)
        drawGrid(width, height, window)
        pygame.display.update()
        
main()
