import random
import os
from time import sleep

def is_list_equal(list_generated_sequence, list_from_user_input):
    return list_generated_sequence == list_from_user_input

class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def generate_sequence(self):
        return [random.randint(1, 101) for _ in range(self.difficulty)]

    def get_list_from_user(self):
        numbers = []
        while True:
            if len(numbers) == self.difficulty:
                break  # Exit the loop when len numbers equals to difficulty
            else:
                user_input = input(f"Enter {self.difficulty} numbers one by one ").strip().lower()
            try:
                number = int(user_input)  # Validate if input is a number
                numbers.append(number)
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        return numbers

    def play(self):
        list_sequence = self.generate_sequence()
        print(list_sequence)
        sleep(0.7)
        print('*' * 30)
        list_user_input = self.get_list_from_user()
        return is_list_equal(list_sequence, list_user_input)

