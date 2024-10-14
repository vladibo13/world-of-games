import os

SCORES_FILE_NAME = 'files/Scores.txt'
BAD_RETURN_CODE = -1

def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    elif 'TERM' in os.environ:  # Unix
        os.environ['TERM'] = 'xterm'
        os.system('clear')