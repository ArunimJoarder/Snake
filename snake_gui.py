#!/usr/bin/env python3

import pygame
from snake_engine import *

pygame.init()

screenWidth     = 900
screenHeight    = 900
food_radius     = int((screenWidth/boardSize[0])/2)
snake_body_radius = int((screenWidth/boardSize[0])/2)

NAVYBLUE = (10, 20, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

foodColours = [NAVYBLUE, RED, YELLOW, WHITE]

def wipeScreen(win):
    win.fill(BLACK)

def getCoordinates(coor):
    y = int(screenWidth/boardSize[0]) * coor[0] + round(snake_body_radius)
    x = int(screenWidth/boardSize[1]) * coor[1] + round(snake_body_radius)
    return (x,y)

def drawSnake(win):
    for part in snake.body:
        center = getCoordinates(part)
        pygame.draw.circle(win, NAVYBLUE, center, snake_body_radius)
    pygame.draw.circle(win, WHITE, getCoordinates(snake.body[0]), snake_body_radius)

def drawFood(win):
    center = getCoordinates(gameBoard.foodLocation)
    pygame.draw.circle(win, foodColours[gameBoard.foodType - 1], center, food_radius)

def updateScreen(win):
    wipeScreen(win)
    drawSnake(win)
    drawFood(startWin)
    pygame.display.update()

startWin = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Snake")


while not gameover:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
            message  = 'Bubbye!'

    dropFood()
    
    # updateScreen(startWin)
    # gameBoard.printBoard()
    # print()

    keys = pygame.key.get_pressed()
    turn = 0
    if keys[pygame.K_LEFT]:
        turn = -1
    elif keys[pygame.K_RIGHT]:
        turn = 1

    gameover, message = moveSnake(turn)
    updateScreen(startWin)

    if gameover:
        print()
        print('GAMEOVER')
        print(message)

    pygame.time.delay(120)