# Hangman

A polished **command-line Hangman game built in Python** with animated text, multiple genres, a scoring system, and a hint mechanic that makes every round a little more strategic.

Unlike a basic Hangman implementation, this version includes **genre selection, animated gameplay, score tracking, limited hints, and replay-friendly design**, making it a great beginner-to-intermediate Python project.

## Gameplay

1. Choose a genre.
2. Guess letters one by one or attempt the whole word.
3. Use **hints** carefully because each hint costs points.
4. Win by revealing the entire word before your score reaches zero.

## Features

* **4 genres:** Animals, Sports, Movies, and Technology
* **Animated text effects** for a more engaging terminal experience
* **Scoring system** starting at 50 points
* **Limited hints** (5 per game)
* **Whole-word guessing**
* **Tracks total words guessed correctly**
* **Cross-platform terminal support** (Windows and macOS/Linux)

## Demo

```text
==================================================
WELCOME TO THE HANGMAN GAME
==================================================

Choose a genre:
1. Animals
2. Sports
3. Movies
4. Technology

Genre: Movies
Word:
_ _ _ _ _ _ _

Enter a letter, guess the whole word, or type 'hint':
```

## Project Structure

```text
hangman/
├── hangman.py
└── README.md
```

## How to Run

Make sure Python 3 is installed, then run:

```bash
python hangman.py
```

## What I Practiced

This project helped me practice:

* Python functions
* Loops and conditionals
* Lists and dictionaries
* Random selection
* String manipulation
* Global state management
* User input handling
* Building a complete terminal application

## Tech Stack

* **Python 3**
* Standard libraries: `random`, `time`, `os`

---

If you enjoyed this project, feel free to star the repository or fork it and add your own genres and game modes.
