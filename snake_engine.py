#!/usr/bin/env python3

import numpy as np
import random as rn
from snake_pieces import *

boardSize = (30,30)

gameBoard = Board(boardSize)

snake = Snake()
snake.draw(gameBoard)

gameover = False

food = Food(0,0)

def dropFood():
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

def moveSnake(turn):
    snake.facing = (snake.facing + turn) % 4
    
    snake.move(gameBoard)

    gameover, message = snake.checkDead(gameBoard)

    foodPos = gameBoard.foodLocation
    if snake.body[0] == foodPos:
        snake.grow(gameBoard, gameBoard.foodType)
        gameBoard.foodLeft = False

    return gameover, message

# while not gameover:
    
#     dropFood()
    
#     gameBoard.printBoard()
#     print()

#     turn = input('which direction?: ')
#     if turn == 'a':
#         turn = -1
#     elif turn == 'd':
#         turn = 1
#     else:
#         turn = 0

#     gameover, message = moveSnake(turn)

#     if gameover:
#         print()
#         print('GAMEOVER')
#         print(message)

    