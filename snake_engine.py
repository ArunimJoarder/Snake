#!/usr/bin/env python3

import numpy as np
import random as rn
from snake_pieces import *

boardSize = (13,13)

gameBoard = Board(boardSize)

snake = Snake()
snake.draw(gameBoard)

gameover = False

# food = Food(4,4)
# food.drop(gameBoard)

gameBoard.printBoard()
print()

while not gameover:
    
    if not gameBoard.foodLeft:
        food_allowed = False
        while not food_allowed:
            food_x = rn.randrange(boardSize[0])
            food_y = rn.randrange(boardSize[0])
            food_allowed = True
            for part in snake.body:
                if part == [food_x, food_y]:
                    food_allowed = False

        food = Food(food_x, food_y)
        food.drop(gameBoard)
        gameBoard.foodLeft = True
        gameBoard.printBoard()
        print()

    turn = input('which direction?: ')
    if turn == 'l':
        turn = -1
    elif turn == 'r':
        turn = 1
    else:
        turn = 0

    snake.facing = (snake.facing + turn) % 4
    
    snake.move(gameBoard)
    
    gameover = snake.checkDead(gameBoard)

    if snake.body[0] == [food_x, food_y]:
        snake.grow(gameBoard, food.type)
        gameBoard.foodLeft = False

    gameBoard.printBoard()
    print()


    