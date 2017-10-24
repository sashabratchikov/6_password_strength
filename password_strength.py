import os
import sys
import string


def load_data(filepath):
    with open(filepath, 'r') as text_file:
        return text_file.read()


def test_against_listings(password, dirpath):
    files_content = ''
    for path in filter(lambda path: not path.startswith('.'),
                       os.listdir(dirpath)):
        files_content = files_content + load_data(dirpath + '/' + path)
    if password in set(files_content.splitlines()):
        return True
    return False


def calculate_strength(password):
    coeffitient = 1
    if password.isdecimal():
        coeffitient = 0.2
    elif password.islower() or password.isupper():
        pass
    elif password.isalpha():
        coeffitient = 1.3
    elif password.isalnum():
        coeffitient = 1.5
    elif any(char in set(string.punctuation) for char in password):
        coeffitient = 2
    return int(len(password) / 2 * coeffitient)


def get_password_strength(password, dirpath, min_strength=1, max_strength=10):
    if test_against_listings(password, dirpath):
        return min_strength
    strength = calculate_strength(password)
    if strength < min_strength:
        strength = min_strength
    elif strength > max_strength:
        strength = max_strength
    return strength


if __name__ == '__main__':
    while True:
        password = input('Enter password you wanna test: ')
        if len(password) == 0:
            print('Password should contain at least 1 character')
        else:
            break
    try:
        dirpath = sys.argv[1]
    except IndexError:
        dirpath = 'wordlists'
    print('Password strength:', get_password_strength(password, dirpath))
