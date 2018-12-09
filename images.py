import pygame
import os


Images = {
    0: pygame.image.load(os.path.join("assets/images", "0.png")),
    1: pygame.image.load(os.path.join("assets/images", "1.png")),
    2: pygame.image.load(os.path.join("assets/images", "2.png")),
    3: pygame.image.load(os.path.join("assets/images", "3.png")),
    4: pygame.image.load(os.path.join("assets/images", "4.png")),
    5: pygame.image.load(os.path.join("assets/images", "5.png")),
    6: pygame.image.load(os.path.join("assets/images", "6.png")),
    7: pygame.image.load(os.path.join("assets/images", "7.png")),
    8: pygame.image.load(os.path.join("assets/images", "8.png")),
    "b": pygame.image.load(os.path.join("assets/images", "bomb.png")),
    "f": pygame.image.load(os.path.join("assets/images", "flag.png")),
    "a": pygame.image.load(os.path.join("assets/images", "available.png"))
}


""" class Images:
    def __init__(self):
        self.IMAGE_0 = pygame.image.load(os.path.join("assets/images", "0.png"))
        self.IMAGE_1 = pygame.image.load(os.path.join("assets/images", "1.png"))
        self.IMAGE_2 = pygame.image.load(os.path.join("assets/images", "2.png"))
        self.IMAGE_3 = pygame.image.load(os.path.join("assets/images", "3.png"))
        self.IMAGE_4 = pygame.image.load(os.path.join("assets/images", "4.png"))
        self.IMAGE_5 = pygame.image.load(os.path.join("assets/images", "5.png"))
        self.IMAGE_6 = pygame.image.load(os.path.join("assets/images", "6.png"))
        self.IMAGE_7 = pygame.image.load(os.path.join("assets/images", "7.png"))
        self.IMAGE_8 = pygame.image.load(os.path.join("assets/images", "8.png"))
        self.IMAGE_BOMB = pygame.image.load(os.path.join("assets/images", "BOMB.png"))
        self.IMAGE_FLAG = pygame.image.load(os.path.join("assets/images", "FLAG.png"))
        self.IMAGE_AVAILABLE = pygame.image.load(os.path.join("assets/images", "AVAILABLE.png"))
        self.IMAGE_0 = pygame.image.load(os.path.join("assets/images", "0.png"))
        self.IMAGE_0 = pygame.image.load(os.path.join("assets/images", "0.png"))
        self.IMAGE_0 = pygame.image.load(os.path.join("assets/images", "0.png"))
        self.IMAGE_0 = pygame.image.load(os.path.join("assets/images", "0.png"))
        self.IMAGE_0 = pygame.image.load(os.path.join("assets/images", "0.png")) """