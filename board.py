import pygame
import os
from images import Images
from random import randint


# Constants
BOMB = 'b'
FLAG = 'f'


class Board:
    def __init__(self, columns, rows, block_size, bombs):
        print("Creating Board")
        self.columns = columns
        self.rows = rows
        self.block_size = block_size
        self.bomb_count = bombs
        self.board_display = []
        self.board = []
        self.reset()
    
    def load():
        pass
    
    def reset(self):
        self.board_display = [[False for x in range(self.columns)] for y in range(self.rows)]
        self.board = [[0 for x in range(self.columns)] for y in range(self.rows)]
        self.placeBombs()

    def placeBombs(self):
        print("Placing bombs")
        possibilities = []
        for y in range(self.rows):
            for x in range(self.columns):
                possibilities.append((x, y))
        
        for n in range(self.bomb_count):
            index = randint(0, len(possibilities) - 1)
            selected = possibilities.pop(index)
            self.board[selected[1]][selected[0]] = 9

        # @todo: Fix the calculation of how many bombs are near
    
    def render(self, screen):
        for y in range(self.rows):
            for x in range(self.columns):
                image = Images[self.board[y][x]] if self.board_display[y][x] == True else Images[11]
                screen.blit(pygame.transform.scale(image, (self.block_size, self.block_size)) , (x * self.block_size, y * self.block_size))
        pygame.display.flip()