import run
gameRun = False


def main():
    if run.game():  # Runs the game and returns True when it's done to rerun main and open the menu again
        main()


if __name__ == '__main__':
    main()