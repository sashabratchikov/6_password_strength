# Password Strength Calculator

## Description  

Password strength can be measured by time which takes for cracking software to guess it. Passwords which are considered to be the weakest are those from lists of most commonly used passwords, vocabulary words and passwords which have previously been leaked.

This python script tests your password against english vocabulary, list of 10000 most commonly used passwords and list of passwords which have been leaked from myspace. It also tests such params as password length, usage of digits, special symbols and letters of different case.

All used lists are in `/wordlists` folder. You can find more password security lists here:
https://github.com/danielmiessler/SecLists/tree/master/Passwords

## Repository structure  

`password_strength.py` contains several functions:
`load_data(filepath)` – to load text files content  
`test_against_listings(password, dirpath)` – tests if some of the listings in `dirpath` folder contains given `password`  
`calculate_strength(password)` – calculates password strength. It takes into consideration password length and symbols password contains: e.g long passwords with different cased letters, digits and special symbols are much stronger than short numeric passwords.  
`get_password_strength(password, dirpath, min_strength=1, max_strength=10)` – accumulator function which returns password strength based on the result of `test_against_listings` and `calculate_strength`

`wordlists` folder contains security listings you want to test your password against. You can put more listings there or provide a path to directory with listings as a command line argument (see Usage section).

## Usage  

```bash
python password_strength.py <path to folder with security lists>
```

If you won't provide path to folder script will look for files in `/wordlists` folder.
Then you'll be asked to input password you wanna test, fill it (it should be at least one character):

```bash
Enter password you wanna test: qwerty
```

Result:

```bash
Password strength: 1
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
