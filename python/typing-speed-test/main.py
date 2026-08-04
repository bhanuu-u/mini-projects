import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "This is the way for us to reference the object of the class."
]


def calculate_accuracy(original, typed):
    original_words = original.split()
    typed_words = typed.split()

    correct = 0

    for o, t in zip(original_words, typed_words):
        if o == t:
            correct += 1

    accuracy = (correct / len(original_words)) * 100

    mistakes = (
        len(original_words) - correct
        + abs(len(original_words) - len(typed_words))
    )

    return accuracy, mistakes


def typing_test():

    sentence = random.choice(sentences)

    print("=" * 60)
    print("             ⌨️  PYTHON TYPING SPEED TEST")
    print("=" * 60)

    print("\nType the following sentence exactly as shown:\n")
    print(sentence)

    input("\nPress Enter when you're ready...")

    print("\nStarting in...")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

    print("\nGO!\n")

    start = time.time()

    user_input = input()

    end = time.time()

    time_taken = end - start

    word_count = len(sentence.split())

    wpm = word_count / (time_taken / 60)

    accuracy, mistakes = calculate_accuracy(sentence, user_input)

    print("\n" + "=" * 60)
    print("                    RESULTS")
    print("=" * 60)

    print(f"Time Taken : {time_taken:.2f} seconds")
    print(f"Words      : {word_count}")
    print(f"WPM        : {wpm:.2f}")
    print(f"Accuracy   : {accuracy:.2f}%")
    print(f"Mistakes   : {mistakes}")

    if accuracy == 100:
        print("\n🏆 Perfect typing!")
    elif accuracy >= 90:
        print("\n🎉 Excellent!")
    elif accuracy >= 75:
        print("\n👍 Good job!")
    else:
        print("\n💪 Keep practicing!")

    print("=" * 60)


typing_test()