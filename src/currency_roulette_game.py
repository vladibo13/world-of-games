import requests
import random


def get_guess_from_user():
    while True:
        try:
            number_guess = int(input(f"please enter number between guess of value to a given amount of USD "))
            return number_guess
        except ValueError:
            print(f"Invalid input. Please enter a valid number")


class CurrencyRouletteGame:

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.url = 'https://api.exchangerate-api.com/v4/latest/USD'
        self.random_number = random.randint(1, 101)

    # for given difficulty d, and total value of money t the interval will be: (t - (5 - d), t + (5 - d))
    def get_money_interval(self):
        try:
            # Make a GET request to the given URL
            response = requests.get(self.url)
            # Check if the request was successful (status code 200)
            response.raise_for_status()
            # Process the JSON response (if applicable)
            data = response.json()  # Use response.text for non-JSON responses
            ils = data["rates"]["ILS"]
            total_value = ils * self.random_number
            return round(total_value - (5 - self.difficulty)), round(total_value + (5 - self.difficulty))
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # e.g., 404, 500
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")  # e.g., no internet
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")  # Request took too long
        except requests.exceptions.RequestException as req_err:
            print(f"An error occurred: {req_err}")  # Base exception for all others
        except ValueError as json_err:
            print(f"JSON decoding failed: {json_err}")  # Handle JSON errors
        # Return None in case of any failure
        return None

    def play(self):
        money_range = self.get_money_interval()
        print(money_range)
        money_range_user = get_guess_from_user()
        return money_range[0] <= money_range_user <= money_range[1]


