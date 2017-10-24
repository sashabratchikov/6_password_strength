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


def calculate_strength(password, max_strength):
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
    strength = int(len(password) / 2 * coeffitient)
    return max_strength if strength > max_strength else strength


def get_password_strength(password, dirpath, max_strength=10):
    if test_against_listings(password, dirpath):
        return 1
    return calculate_strength(password)


if __name__ == '__main__':
    while True:
        password = input('Enter password you wanna test: ')
        if len(password) == 0:
            print('Password should contain at least 1 character')
        else:
            break
    dirpath = argv[1] or './wordlists'
    print(get_password_strength(password, dirpath))
