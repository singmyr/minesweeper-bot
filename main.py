from game import Game

def main():
    game = Game()
    game.init(16, 16, 32, 0)
    game.start()

if __name__ == "__main__":
    main()