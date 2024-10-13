import random

# oop
class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = 0

    def generate_number(self):
        self.secret_number = random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        while True:
            try:
                game = int(input(f"please enter number between 1 to {self.difficulty} "))
                if 1 <= game <= self.difficulty:
                    print(f"Valid input: {game}")
                    return game
                else:
                    print("Input out of range. Please try again.")
            except ValueError:
                print(f"Invalid input. Please enter a valid number in range of 1 to {self.difficulty}")

    def compare_results(self,  guess_number):
        return self.secret_number == guess_number

    def play(self):
        self.generate_number()
        guess_number = self.get_guess_from_user()
        return self.compare_results(guess_number)

