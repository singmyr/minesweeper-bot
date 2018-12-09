import pygame
from board import Board

class Game:
    def __init__(self):
        print("Creating Game")
    
    def init(self, columns, rows, block_size, bombs):
        self.board = Board(columns, rows, block_size, bombs)
        pygame.init()
        pygame.display.set_caption("Minesweeper")
        self.screen = pygame.display.set_mode((columns * block_size, rows * block_size), pygame.HWSURFACE | pygame.DOUBLEBUF)
    
    def start(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.board.render(self.screen)