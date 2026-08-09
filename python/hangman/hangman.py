import random
import time
import os

genres = {
    "Animals": [
        "elephant", "tiger", "monkey", "dolphin", "giraffe",
        "kangaroo", "zebra", "panda"
    ],
    "Sports": [
        "cricket", "football", "tennis", "hockey", "badminton",
        "volleyball", "boxing", "archery"
    ],
    "Movies": [
        "avatar", "inception", "gladiator", "frozen", "titanic",
        "joker", "interstellar", "matrix"
    ],
    "Technology": [
        "python", "computer", "algorithm", "database", "network",
        "software", "keyboard", "processor"
    ]
}

score = 50
display = []
rand_word = ""
hints_left = 5
words_guessed = 0


# -------------------- Animations -------------------- #

def animate_text(text, delay=0.04):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def show_word(display):
    for ch in display:
        print(ch, end=" ", flush=True)
        time.sleep(0.08)
    print()


# -------------------- Utility Functions -------------------- #

def points():
    print(f"Current Score: {score}")


# -------------------- Hint Function -------------------- #

def get_hint():
    global score, display, rand_word, hints_left

    if hints_left == 0:
        animate_text("No hints left!")
        return

    hidden_indexes = []

    for i in range(len(display)):
        if display[i] == "_":
            hidden_indexes.append(i)

    if hidden_indexes:
        hint_index = random.choice(hidden_indexes)
        display[hint_index] = rand_word[hint_index]

        score -= 10
        hints_left -= 1

        if score <= 0:
            animate_text("Game Over! You have no points left.")
            animate_text(f"The correct word was: {rand_word.upper()}")
            return

        animate_text("Hint revealed!")
        print(f"Hints left: {hints_left}")
        print(f"Score: {score}")
        print("Word:")
        show_word(display)

    else:
        animate_text("No more letters to reveal!")


# -------------------- Genre Selection -------------------- #

def choose_genre():
    genre_names = list(genres.keys())

    animate_text("Choose a genre:")
    for i, genre in enumerate(genre_names, start=1):
        print(f"{i}. {genre}")

    while True:
        choice = input("Enter your choice: ").strip()

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(genre_names):
                return genre_names[choice - 1]

        animate_text("Invalid choice. Please select a valid genre.")


# -------------------- Game Function -------------------- #

def start_game():
    global display, rand_word, score, words_guessed, hints_left

    os.system("cls" if os.name == "nt" else "clear")

    score = 50
    hints_left = 5

    selected_genre = choose_genre()

    rand_word = random.choice(genres[selected_genre])
    display = ["_"] * len(rand_word)

    print()
    animate_text(f"Genre: {selected_genre}")
    animate_text("A new word has been chosen!")
    print("Word:")
    show_word(display)

    while True:
        user = input("Enter a letter, guess the whole word, or type 'hint': ").strip().lower()

        if user == "hint":
            get_hint()

            if score <= 0:
                break

        elif user == rand_word:
            animate_text("Excellent! You guessed the whole word!")
            print(f"Your score is: {score}")
            words_guessed += 1
            break

        else:
            found = False

            for i in range(len(rand_word)):
                if rand_word[i] == user:
                    display[i] = user
                    found = True

            if found:
                animate_text("Correct guess!")
                print("Word:")
                show_word(display)

                if "_" not in display:
                    animate_text("Perfect guess! You completed the word!")
                    print(f"Your score is: {score}")
                    words_guessed += 1
                    break

            else:
                animate_text("Wrong guess, try again!")
                score -= 10
                print(f"Score: {score}")

                if score <= 0:
                    animate_text("Game Over! You have exhausted all your points.")
                    animate_text(f"The correct word was: {rand_word.upper()}")
                    break


# -------------------- Main Menu -------------------- #

print("=" * 50)
animate_text("WELCOME TO THE HANGMAN GAME", 0.05)
print("=" * 50)
time.sleep(0.5)

while True:
    print()
    print("1. Start Game")
    print("2. Show Current Score")
    print("3. Show Total Correct Guesses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        start_game()

    elif choice == "2":
        points()

    elif choice == "3":
        print(f"Total correct words guessed: {words_guessed}")

    elif choice == "4":
        animate_text("Thanks for playing!")
        break

    else:
        animate_text("Invalid choice. Please try again.")