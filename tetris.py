import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

colors = [(0,255,255),(255,60,245),(255,45,45),(55,255,65),(245,255,50),(255,180,195)]


#Play zone
screen_width = 800
screen_height = 700
play_zone_W  = 300
play_zone_H  = 600
block_size = 30

top_left_x = (screen_width - play_zone_W) // 2
top_left_y = screen_height - play_zone_H

#Shapes--matrix of each shape in a 5x5 with shapes determined in matrices
#with possible rotations of each shape

I = [['00200',
      '00200',
      '00200',
      '00200',
      '00200'],
     ['00000',
      '00000',
      '22222',
      '00000',
      '00000']]
B = [['00000',
      '00220',
      '00220',
      '00220',
      '00000'],
     ['00000',
      '00000',
      '02220',
      '02220',
      '00000']]
T = [['00000',
      '00200',
      '00200',
      '02220',
      '00000'],
     ['00000',
      '00020',
      '02220',
      '00020',
      '00000'],
     ['00000',
      '02220',
      '00200',
      '00200',
      '00000'],
     ['00000',
      '02000',
      '02220',
      '02000',
      '00000']]
J = [['00020',
      '00020',
      '02020',
      '02220',
      '00000'],
     ['00000',
      '22220',
      '00020',
      '00220',
      '00000'],
     ['00000',
      '02220',
      '02020',
      '02000',
      '02000'],
     ['00000',
      '02200',
      '02000',
      '02222',
      '00000']]
L = [['00020',
      '00020',
      '00020',
      '02220',
      '00000'],
     ['00000',
      '22220',
      '00020',
      '00020',
      '00000'],
     ['00000',
      '02220',
      '02000',
      '02000',
      '02000'],
     ['00000',
      '02000',
      '02000',
      '02222',
      '00000']]
Z = [['00020',
      '00020',
      '00220',
      '00200',
      '00200'],
     ['00000',
      '22200',
      '00222',
      '00000',
      '00000']]

shapes = [I, B, T, J, L, Z]
colors = colors = [(0,255,255),(255,60,245),(255,45,45),(55,255,65),(245,255,50),(255,180,195)]

class Shape(object):
    #standard Tetris map size.
    play_zone_H = play_zone_W
    cols = play_zone_H

    def __init__(self, cols, play_zone_H, shape):
        self.x = cols
        self.y = play_zone_H
        self.shape = shape
        self.color = random.randint(1, len(colors)-1)
        self.rotation = 0 #Base orientation 
        #self.body = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]


def make_shape(): #provide new shape in top middle of grid
    #self.shape = Shape(3,0)
    return Shape( 5, 0 , random.choice(shapes))

def convert_shape(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]
 
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '2':
                positions.append((shape.x + j, shape.y + i))
 
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)
 
    return positions

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

    def collision(shape, grid): 
        open_spots = [[(j,i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
        open_spots = [j for sub in open_spots for j in sub]

        conshape = convert_shape(shape)

        for pos in conshape:
            if pos not in open_spots:
                if pos[1] > -1:
                    return False
        return True



def createGrid(stopped_shapes={}):
    grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if ( j, i) in stopped_shapes:
                blocked = stopped_shapes[(j,i)]
                grid[i,j] = blocked
    return grid

def drawGrid(surface, grid):
    x = top_left_x
    y = top_left_y

    for i in range(len(grid)):
        pygame.draw.line(surface, (128, 128, 128), (x, y + i*block_size), (x+play_zone_W, y+ i*block_size))
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (128, 128, 128), (x + j*block_size, y), (x + j*block_size, y + play_zone_H))

#def drawWindow(surface, grid):
    #surface.fill((0,0,0))

def drawshape(shape, surface):
    #font = pygame.font.SysFont('comicsans', 30)
   # label = font.render('Next Shape', 1, (255,255,255))

    x = top_left_x + play_zone_W + 50
    y = top_left_y + play_zone_H/2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (x + j*block_size, y + i*block_size, block_size, block_size), 0)

    #surface.blit(label, (x + 10, y - 30))

    
def move(shape, grid):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.display.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_piece.x -=1
                if not (collision(current_piece, grid)):
                    current_piece.x += 1
            if event.key == pygame.K_RIGHT:
                current_piece.x += 1
                if not (collision(current_piece, grid)):
                    current_piece.x -=1
            if event.key == pygame.K_DOWN:
                current_piece.y +=1
                if not (collision(current_piece,grid)):
                    current_piece.y -=1 
            if event.key == pygame.K_UP:
                current_piece.rotation +=1
                if not(collision(current_piece, grid)):
                    current_piece -=1
    
    piece_pos = convert_shape(shape)

    for i in range(len(piece_pos)):
        x , y  = piece_pos[i]
        if y > -1:
            grid[y][x] = shape.color

def main(window):
    currPos = 0
    width = 500
    height = 500
    #play_zone_H = []
    cols = []
    stopped_shapes = {}
    #marked_boxes = [[0]*play_zone_W]*play_zone_H
    run = True
    current_piece = make_shape() 
    next_shape = make_shape()
    grid = createGrid(stopped_shapes)
    window.fill((0,0,0))

    #square.append()
    clock = pygame.time.Clock()
    #window = pygame.display.set_mode((width, height))

    #print(len(square))

    while run:
        window.fill((0,0,0))
        grid = createGrid(stopped_shapes)
        pygame.time.delay(50)
        clock.tick(10)

        move(current_piece, grid)      

        #window.fill((0,0,0))
        drawGrid(window, grid)
        #drawshape(next_shape, window)
        pygame.display.update()

window = pygame.display.set_mode((screen_width, screen_height))
main(window)         