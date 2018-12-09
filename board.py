import pygame
import os
from images import Images


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
        self.reset()
    
    def load():
        pass
    
    def reset(self):
        self.board = [["a" for x in range(self.columns)] for y in range(self.rows)]
        self.placeBombs()

    def placeBombs(self):
        print("Placing bombs")
    
    def render(self, screen):
        for y in range(self.rows):
            for x in range(self.columns):
                screen.blit(pygame.transform.scale(Images[self.board[y][x]], (self.block_size, self.block_size)) , (x * self.block_size, y * self.block_size))
        pygame.display.flip()