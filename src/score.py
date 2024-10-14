from utils import SCORES_FILE_NAME, BAD_RETURN_CODE
import os

def get_current_score():
    if os.path.isfile(SCORES_FILE_NAME):
        with open( SCORES_FILE_NAME) as file:
            return int(file.read())
    else:
        return BAD_RETURN_CODE

def add_score( difficulty, mode = 'w+'):
    point_of_winning = (difficulty * 3) + 5

    current_score = int(get_current_score())

    if current_score == BAD_RETURN_CODE:
        with open( SCORES_FILE_NAME, mode) as file:
            file.write(str(point_of_winning))
    else:
        with open( SCORES_FILE_NAME, mode) as file:
            file.write(str(current_score + point_of_winning))




