import random
import string
import pyperclip
import time



def enhancer(line):
    for i in line:
        print(i, end="", flush=True)
        time.sleep(0.03)
    print()

MIN_STRONG_LENGTH = 12

enhancer("=== Secure Password Generator ===")
enhancer("")


while True:
    try:
        length = int(input("Enter password length: "))
        if length >= 4:
            break
        enhancer("Password length must be at least 4.")
    except ValueError:
        enhancer("Please enter a valid number.")


use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
use_numbers = input("Include numbers? (y/n): ").lower() == "y"
use_symbols = input("Include symbols? (y/n): ").lower() == "y"


password_list = []

# Lowercase is always included
password_list.append(random.choice(string.ascii_lowercase))

# Character pool
characters = string.ascii_lowercase

if use_upper:
    password_list.append(random.choice(string.ascii_uppercase))
    characters += string.ascii_uppercase

if use_numbers:
    password_list.append(random.choice(string.digits))
    characters += string.digits

if use_symbols:
    password_list.append(random.choice(string.punctuation))
    characters += string.punctuation


if length < len(password_list):
    enhancer(f"Password length must be at least {len(password_list)}.")
    exit()


while len(password_list) < length:
    password_list.append(random.choice(characters))


random.shuffle(password_list)


password = "".join(password_list)

enhancer("")
enhancer("Generated Password:")
enhancer(password)


pyperclip.copy(password)
enhancer("Password copied to clipboard!")



check_strength = input("Do you want to check the strength of your password? (y/n): ").lower()

if check_strength == "y":
    score = 0

    if length >= 8:
        score += 1
    if length >= MIN_STRONG_LENGTH:
        score += 1
    if use_upper:
        score += 1
    if use_numbers:
        score += 1
    if use_symbols:
        score += 1

    percentage = (score / 5) * 100

    enhancer("")
    enhancer("Password Strength:")
    enhancer(f"{percentage:.0f}%")

    if percentage <= 40:
        enhancer("Weak")
    elif percentage <= 80:
        enhancer("Medium")
    else:
        enhancer("Strong")
