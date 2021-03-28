import numpy as np 
import random
import pygame
import numpy as np

board = np.zeros((20, 10))

T = np.array([
    (0,1,0,0),
    (1,1,0,0),
    (0,1,0,0),
    (0,0,0,0)
    ])

class Shape:
    def __init__(self, shape_number, shape_color):
        self.shape = shape_number
        self.color = shape_color

def drawShape(window, color):
    pygame.draw.rect(window, color, (0, 0, random.randrange(400,800), random.randrange(400,800)))

def main():

    newShape = np.array()
    emptyShape = np.zeros((4, 4))
    
    for i in range(T.shape[0]):
        for j in range(T.shape[1]):
            # only draw squares in cells populated with a 1
            if(T[i][j] == 1):
                board[i][j+4] = 1

    print(board)

    coords = []
    pairs = []

    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if(board[i][j] == 1):
                coords.append(i)
                coords.append(j)
                pairs.append(list(coords))
                coords.pop()
                coords.pop()

    print(pairs)


main()
