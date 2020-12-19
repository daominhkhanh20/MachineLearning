import pygame
import numpy as np
from random import randint
import sys

class snakeAi:

    '''
     |--------------------- (height) x axis
     |
     |
     |
     |
     |
     (width) y axis
    '''
    def __init__(self, gui=False, width=600, height=600,
                 BLACK = (0, 0, 0),
                 WHITE = (255, 255, 255),
                 YELLOW=(255,255,0),
                 RED=[255, 0, 0], score=0,sizeBlock=20, finished=False):
        self.gui = gui
        self.height = height
        self.width = width
        self.RED=RED
        self.YELLOW=YELLOW
        self.finished = finished
        self.score = score
        self.clock = pygame.time.Clock()
        self.WHITE=WHITE
        self.BLACK=BLACK
        self.sizeBlock=sizeBlock
        self.timer=0

    def drawGrid(self,display):
        x,y=0,0
        while x<self.width or y<self.height:
            if x==self.width and y<self.height:
                y+=self.sizeBlock
                pygame.draw.line(display,self.WHITE,(0,y),(self.width,y))
            elif y==self.height and x<self.width:
                x+=self.sizeBlock
                pygame.draw.line(display,self.WHITE,(x,0),(x,self.height))
            else:
                y+=self.sizeBlock
                pygame.draw.line(display,self.WHITE,(0,y),(self.width,y))
                x+=self.sizeBlock
                pygame.draw.line(display,self.WHITE,(x,0),(x,self.height))


    def display_apple(self, display,food):
        pygame.draw.rect(display,self.RED,pygame.Rect(food[0],food[1],self.sizeBlock,self.sizeBlock))


    def display_snake(self, display, snake):
        i=0
        for position in snake:
            if i==0:
                pygame.draw.rect(display, self.YELLOW, pygame.Rect(
                    position[0], position[1], self.sizeBlock, self.sizeBlock))
            else:
                pygame.draw.rect(display, self.WHITE, pygame.Rect(
                    position[0], position[1], self.sizeBlock, self.sizeBlock))
            i+=1

    def start(self):
        self.snake_init()
        self.food_int()
        if self.gui:
            self.display = pygame.display.set_mode((self.width, self.height))
            self.display.fill(self.BLACK)
            self.drawGrid(self.display)
            pygame.display.flip()
        return self.get_observation()

    def snake_init(self):
        self.snake=[[80,80],[60,80]]
        #self.score=len(self.snake)

    def food_int(self):
        self.food = []
        while len(self.food) == 0:
            #self.food = [randint(2,self.width//20-2) * 20, randint(2, self.height//20-2) * 20]
            self.food = [randint(1,self.width//20-1) * 20, randint(1, self.height//20-1) * 20]
            if self.food in self.snake:
                self.food = []

    def get_observation(self):
        return self.finished, self.snake, self.score, self.food


    def step(self, key,i=1):
        point = list(self.snake[0])
        if key == 0:  # left
            point[0] -= self.sizeBlock
        elif key == 1:  # down
            point[1] += self.sizeBlock
        elif key == 2:  # right
            point[0] += self.sizeBlock
        elif key == 3:  # up
            point[1] -= self.sizeBlock
        if self.gui:
            self.display.fill(self.BLACK)
            self.drawGrid(self.display)
            self.display_apple(self.display,self.food)
            self.display_snake(self.display, self.snake)

        if self.food_eaten():
            self.score += 1
            self.food_int()
            self.snake.insert(0, point)
        else:
            self.snake.insert(0, point)
            self.snake.pop()

        self.check_collision(self.snake)

        if self.gui:
            pygame.display.set_caption("Snake,score:" + str(self.score)+"      Game:"+str(i))
            pygame.display.flip()

        if self.finished:
            pygame.time.delay(500)
            pygame.display.quit()
            pygame.quit()

        self.timer+=self.clock.tick(30)

        return self.get_observation()

    def food_eaten(self):
        return self.snake[0] == self.food

    def collision_barrier(self, snake_head):
        x, y = snake_head
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return 1
        return 0

    def collision_body(self, snake_head):
        if snake_head in self.snake[1:]:
            return 1
        return 0

    def check_collision(self, snake_body):
        if self.collision_body(snake_body[0]) == 1 or self.collision_barrier(snake_body[0]):
            self.finished = True

    def get_sizeBlock(self):
        return self.sizeBlock

    def get_sizeScreen(self):
        return self.width,self.height

