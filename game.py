import pygame
import random
from enum import Enum
from collections import namedtuple
pygame.init()

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x', 'y')

BLOCK_SIZE = 20

class Game():
    
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h

        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake')

        self.clock = pygame.time.Clock()

        self.direction = Direction.RIGHT

        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head, Point(self.head.x-BLOCK_SIZE, self.head.y)]


    def play_step():
        pass

if __name__ == '__main__':
    game = Game()

    while True:
        game.play_step()

    pygame.quit()