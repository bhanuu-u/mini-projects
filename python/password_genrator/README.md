# Password Generator

A secure password generator built with **Python** that creates strong, randomized passwords based on user preferences. The program guarantees that every selected character type (uppercase letters, numbers, and symbols) is included in the final password, copies the password to the clipboard, and provides a simple password strength analysis.

## Features

* Generate passwords of any length
* Include uppercase letters
* Include numbers
* Include special symbols
* Guaranteed inclusion of every selected character type
* Randomized password order using `random.shuffle()`
* Automatic copy-to-clipboard support
* Password strength checker (Weak / Medium / Strong)
* Animated terminal output using a custom typing effect

## Example

```text
=== Secure Password Generator ===

Enter password length: 12
Include uppercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): y

Generated Password:
A9!kQ2#mLp@7

Password copied to clipboard!

Do you want to check the strength of your password? (y/n): y

Password Strength:
100%
Strong
```

## Technologies Used

* Python
* `random`
* `string`
* `time`
* `pyperclip`

## Project Structure

```text
password-generator/
│
├── password_generator.py
└── README.md
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/password-generator.git
```

2. Navigate to the project folder:

```bash
cd password-generator
```

3. Install the required dependency:

```bash
pip install pyperclip
```

4. Run the program:

```bash
python password_generator.py
```

## What I Learned

While building this project, I practiced:

* Working with strings and lists
* Random password generation
* Conditional logic
* Loops and input validation
* Clipboard handling with `pyperclip`
* Basic security concepts
* Improving user experience with terminal animations

## Future Improvements

* CustomTkinter GUI version
* Password history
* Save generated passwords to a secure encrypted file
* Advanced entropy-based strength calculation
* Option to exclude similar-looking characters (O, 0, I, l)

## Author

**Revanth Bhanu**

A Python mini-project created as part of my programming and software development learning journey.
