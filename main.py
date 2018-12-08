from PIL import ImageGrab
import pyautogui
from random import randint
from time import sleep

# pip3 install pillow
# https://pyautogui.readthedocs.io/en/latest/install.html

# Constants
w = 15
h = 15
boardW = 31
boardH = 16
gridOffsetX = 25
gridOffsetY = 180

# Colors
def getColor(pixel):
    return pixel[0] << 16 | pixel[1] << 8 | pixel[2]

def checkFatal(img, x, y):
    BLACK = 0 << 16 | 0 << 8 | 0
    return getColor(img.getpixel((x + 5, y + 5))) == BLACK

def checkFlag(img, x, y):
    WHITE = 255 << 16 | 255 << 8 | 255
    RED = 253 << 16 | 26 << 8 | 32
    return getColor(img.getpixel((x, y))) == WHITE and getColor(img.getpixel((x + 8, y + 5))) == RED 

def checkAvailable(img, x, y):
    WHITE = 255 << 16 | 255 << 8 | 255
    return getColor(img.getpixel((x, y))) == WHITE

def checkOne(img, x, y):
    BLUE = 8 << 16 | 1 << 8 | 251
    return getColor(img.getpixel((x + 8, y + 8))) == BLUE

def checkTwo(img, x, y):
    GREEN = 9 << 16 | 122 << 8 | 13
    return getColor(img.getpixel((x + 4, y + 2))) == GREEN

def checkThree(img, x, y):
    RED = 253 << 16 | 26 << 8 | 32
    return getColor(img.getpixel((x + 3, y))) == RED

def checkFour(img, x, y):
    DARK_BLUE = 1 << 16 | 0 << 8 | 121
    return getColor(img.getpixel((x + 5, y + 2))) == DARK_BLUE

def checkFive(img, x, y):
    MAROON = 122 << 16 | 7 << 8 | 9
    return getColor(img.getpixel((x + 3, y + 3))) == MAROON

# Functions
def reset():
    pyautogui.click(89, 154)

def scan(board):
    grid = ImageGrab.grab(bbox=(25, 177, 521, 433))
    for y in range(boardH):
        coordY = (y * (h + 1))
        for x in range(boardW):
            coordX = (x * (w + 1))
            if checkFatal(grid, coordX, coordY):
                board[y][x] = -2
            elif checkAvailable(grid, coordX, coordY):
                if checkFlag(grid, coordX, coordY):
                    board[y][x] = -3
                else:
                    board[y][x] = 0
            elif checkOne(grid, coordX, coordY):
                board[y][x] = 1
            elif checkTwo(grid, coordX, coordY):
                board[y][x] = 2
            elif checkThree(grid, coordX, coordY):
                board[y][x] = 3
            elif checkFour(grid, coordX, coordY):
                board[y][x] = 4
            elif checkFive(grid, coordX, coordY):
                board[y][x] = 5
            else:
                board[y][x] = -1
    return board

def getMove(board):
    validMoves = []
    for y in range(boardH):
        for x in range(boardW):
            if board[y][x] == 0:
                validMoves.append((y, x))
            elif board[y][x] == -2:
                # Game over
                return False
    
    if len(validMoves) > 0:
        return validMoves[randint(0, len(validMoves) - 1)]
    return False


def main():
    # grid = ImageGrab.grab(bbox=(25, 177, 521, 433))
    # grid.save('/tmp/image.png', format="PNG")
    # sys.exit()
    pyautogui.click(89, 154)
    while True:
        reset()
        board = [[0 for x in range(boardW)] for y in range(boardH)]
        
        move = getMove(board)
        while move != False:
            print(move)
            coordY = gridOffsetY + (move[0] * (h + 1)) + 8
            coordX = gridOffsetX + (move[1] * (w + 1)) + 8

            pyautogui.click(coordX, coordY)

            # sleep(1)
            board = scan(board)
            move = getMove(board)
        print("Game over?")
    

main()