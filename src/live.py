def welcome(name):
    print(f"""
        Hello {name} and welcome to the World of Games (WoG).
        Here you can find many cool games to play.
        """)

def load_game():
    while True:
        try:
            game = int(input(
                """
                Please choose a game to play:
                1. Memory Game - a sequence of numbers will appear for 1 second and you have to
                guess it back
                2. Guess Game - guess a number and see if you chose like the computer
                3. Currency Roulette - try and guess the value of a random amount of USD in ILS \n
                """
            ))
            if 1 <= game <= 3:
                print(f"Valid input: {game}")
                break
            else:
                print("Input out of range. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number(1, 2, 3).")

    while True:
        try:
            game_difficulty = int(input("Please choose game difficulty from 1 to 5: "))
            if 1 <= game_difficulty <= 5:
                print(f"Valid input: {game_difficulty}")
                break
            else:
                print("Input out of range. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number(1, 2, 3, 4, 5).")