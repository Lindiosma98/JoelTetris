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

#def shape():
#def rotate():
#def move():
#def drop():


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

        for i in range(play_zone_W):
            for j in range(play_zone_H):
                if mb[j][i] == 2:
                    disw = self.w // play_zone_W
                    dish = self.h // play_zone_H
                    pygame.draw.rect(window, (255,0,0), (i*disw-1,j*dish-1, disw+2, dish+2))

        window.fill((0,0,0))
        square.draw(window)
        drawGrid(width, height, window)
        pygame.display.update()