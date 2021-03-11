import math
import random
import pygame
import numpy as np
import tkinter as tk
from tkinter import messagebox

width = 500
height = 500
rows = 20
cols = 20
game_array = [[0]*rows]*cols
#def shape():
#def rotate():
#def move():
#def drop():

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
        
main()

while run:
        pygame.time.delay(50)
        clock.tick(10)

        if not(square.pos[1] >= play_zone_H-1):
            square.move()
        else:
            pass
            #print(mb)

        #for i in range(play_zone_W):
         #   for j in range(play_zone_H):
          #      if mb[j][i] == 2:
           #         disw = self.w // play_zone_W
            #        dish = self.h // play_zone_H
             #       pygame.draw.rect(window, (255,0,0), (i*disw-1,j*dish-1, disw+2, dish+2))

        #window.fill((0,0,0))
        #square.draw(window)
        #drawGrid(width, height, window)
        #pygame.display.update()