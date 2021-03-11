import math
import random
import pygame
import numpy as np
import tkinter as tk
from tkinter import messagebox

width = 500
height = 500
rows = 20
cols = 10
squareArray = [[0]*cols]*rows
#0 = no block, 1 = stationary block, 2 = active shape
sa = np.array(squareArray)
collision = False

#puts shape into array (current plan involves active shape being marked by 2's on array)
#def shape(<indicate what shape>):

#IMPORTANT each function involved with movement need to beable to handle not running out of the sides of the game, and
#more importantly collisions with other blocks

#rotates shape
#def rotate(<indicate direction>):

#def move(<indicate direction>):

#def drop(<indicate fast or slow>):

def main():
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
        
main()