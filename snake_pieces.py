#!/usr/bin/env python3

import numpy as np
import random as rn

class Board:
    def __init__(self, size):
        (self.NoRows, self.NoCols)  = size
        self.board                  = np.zeros(size, dtype = np.int8)
        self.foodLeft               = False
        self.foodLocation           = None
        self.foodType               = None

    def changeBoard(self, x, y, val):
        self.board[x,y] = val

    def printBoard(self):
        print(self.board)

class Food:
    def __init__(self, x, y):
        self.x          = x
        self.y          = y
        self.type       = rn.choice([1,1,1,1,1,1,1,1,1,2,2,2,3,3,4])
        self.isEaten    = 0

    def drop(self, board):
        board.foodType      = self.type
        board.foodLocation  = [self.x, self.y]
        board.changeBoard(self.x, self.y, self.type)

class Snake:
    def __init__(self, x, y):
        self.length     = 2
        self.facing     = 2
        self.body       = [[x,y]]
        self.isGrowing  = 0

    def draw(self, board):
        for part in self.body:
            board.changeBoard(part[0], part[1], 77)

        board.changeBoard(self.body[0][0], self.body[0][1], 55)
    
    def grow(self, board, growLength):
        for i in range(growLength):
            self.body.append([self.body[len(self.body) - 1][0],self.body[len(self.body) - 1][1]])
        self.isGrowing = 1

    def move(self, board):
        length = len(self.body)
        board.changeBoard(self.body[length - 1][0], self.body[length - 1][1], 0)

        if not self.isGrowing:
            for i in range(length - 1, 0, -1):
                self.body[i][0] = self.body[i - 1][0]
                self.body[i][1] = self.body[i - 1][1]

        else:
            for i in range(length - 2, 0, -1):
                self.body[i][0] = self.body[i - 1][0]
                self.body[i][1] = self.body[i - 1][1]
            self.isGrowing = 0
        
        if self.facing == 0:
            self.body[0][0] += 1
        elif self.facing == 1:
            self.body[0][1] += -1
        elif self.facing == 2:
            self.body[0][0] += -1
        elif self.facing == 3:
            self.body[0][1] += 1
        

    def checkDead(self, board):
        isDead = False
        deathMessage = 'temp'
        count = 0
        for part in self.body:
            if self.body[0] == part:
                count += 1
            if count > 1:
                deathMessage = 'You bit yourself!!'
                isDead = True

        head_x = self.body[0][0]
        head_y = self.body[0][1]

        if head_x > board.NoRows - 1 or head_x < 0 or head_y > board.NoCols - 1 or head_y < 0:
            deathMessage = 'You crashed into a wall!!'
            isDead = True

        if not isDead:
            self.draw(board)

        return isDead, deathMessage