import random
import time


def game_win(user, computer):
    if user == computer:
        return None
    elif user == "rock":
        return computer == "scissors"
    elif user == "paper":
        return computer == "rock"
    elif user == "scissors":
        return computer == "paper"


print("=" * 45)
print("      ROCK PAPER SCISSORS")
print("=" * 45)

user_score = 0
computer_score = 0
ties = 0

while True:

    print("\nType rock, paper, scissors")
    print("Type 'exit' to quit.")

    user = input("\nYour choice: ").lower().strip()

    if user == "exit":
        break

    if user not in ["rock", "paper", "scissors"]:
        print("❌ Invalid choice! Please try again.")
        continue

    computer = random.choice(["rock", "paper", "scissors"])

    print("\nRock...")
    time.sleep(0.2)

    print("Paper...")
    time.sleep(0.2)

    print("Scissors...")
    time.sleep(0.2)

    print("Shoot!")
    time.sleep(0.3)

    print("\nComputer chose:", computer)
    time.sleep(0.2)

    print("You chose:", user)
    time.sleep(0.2)

    result = game_win(user, computer)

    if result is None:
        print("\n🤝 It's a Tie!")
        ties += 1

    elif result:
        print("\n🎉 You Win This Round!")
        user_score += 1

    else:
        print("\n💻 Computer Wins This Round!")
        computer_score += 1

    time.sleep(0.2)

    print("\n" + "-" * 30)
    print("         SCOREBOARD")
    print("-" * 30)
    print(f"You       : {user_score}")
    print(f"Computer  : {computer_score}")
    print(f"Ties      : {ties}")
    print("-" * 30)

print("\nThanks for playing!")

print("\n========== FINAL SCORE ==========")
print(f"You       : {user_score}")
print(f"Computer  : {computer_score}")
print(f"Ties      : {ties}")

if user_score > computer_score:
    print("\n🏆 Congratulations! You won the match!")
elif computer_score > user_score:
    print("\n💻 Computer wins the match!")
else:
    print("\n🤝 The match ends in a draw!")

print("\nGoodbye!")