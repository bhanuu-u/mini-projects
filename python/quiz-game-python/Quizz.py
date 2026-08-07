import os
import time

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def type_print(text, speed=0.03):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(speed)
    print()

def loading(msg="Loading"):
    print(msg, end="", flush=True)
    for _ in range(5):
        time.sleep(0.35)
        print(".", end="", flush=True)
    print("\n")

QUESTIONS = [
    {"question":"What is the capital of France?","options":["A) Berlin","B) Madrid","C) Paris","D) Rome"],"answer":"C"},
    {"question":"Which planet is called the Red Planet?","options":["A) Venus","B) Mars","C) Jupiter","D) Saturn"],"answer":"B"},
    {"question":"2 + 8 = ?","options":["A) 8","B) 9","C) 10","D) 12"],"answer":"C"},
    {"question":"Which language is popular for Data Science?","options":["A) Python","B) HTML","C) CSS","D) XML"],"answer":"A"},
    {"question":"How many days are in a week?","options":["A) 5","B) 6","C) 7","D) 8"],"answer":"C"},
    {"question":"Largest ocean?","options":["A) Indian","B) Atlantic","C) Pacific","D) Arctic"],"answer":"C"},
    {"question":"King of the Jungle?","options":["A) Tiger","B) Lion","C) Elephant","D) Bear"],"answer":"B"},
    {"question":"How many continents are there?","options":["A) 5","B) 6","C) 7","D) 8"],"answer":"C"},
    {"question":"Which gas do humans breathe?","options":["A) Oxygen","B) Hydrogen","C) Nitrogen","D) Helium"],"answer":"A"},
    {"question":"Who developed Python?","options":["A) Elon Musk","B) Guido van Rossum","C) Bill Gates","D) Dennis Ritchie"],"answer":"B"},
]

def progress_bar(current,total):
    done = int((current/total)*20)
    return "█"*done + "░"*(20-done)

def run_quiz():
    while True:
        clear()
        print("="*60)
        type_print("🎯 WELCOME TO THE GENERAL KNOWLEDGE QUIZ 🎯",0.04)
        print("="*60)
        type_print("📚 Test your knowledge and have fun!")
        loading()

        type_print("⏳ Starting in...")
        for i in range(3,0,-1):
            print(f"   {i}")
            time.sleep(1)

        score = 0
        total = len(QUESTIONS)

        for i,q in enumerate(QUESTIONS,1):
            clear()
            print("="*60)
            print(f"📖 Question {i}/{total}")
            print(progress_bar(i-1,total))
            print("="*60)
            time.sleep(0.3)

            type_print(q["question"],0.03)
            print()

            for option in q["options"]:
                type_print(option,0.015)
                time.sleep(0.15)

            ans = input("\n👉 Your answer (A/B/C/D): ").strip().upper()

            print("\n🔍 Checking",end="",flush=True)
            for _ in range(3):
                time.sleep(0.5)
                print(".",end="",flush=True)
            print()

            if ans == q["answer"]:
                type_print("✅ Correct! Great job! 🎉")
                score += 1
            else:
                correct = next(op for op in q["options"] if op.startswith(q["answer"]))
                type_print("❌ Wrong!")
                type_print(f"✅ Correct Answer: {correct}")

            print(f"\n⭐ Current Score: {score}/{i}")
            time.sleep(2)

        clear()
        percent = score/total*100

        type_print("🏁 QUIZ FINISHED!",0.05)
        loading("📊 Calculating Result")

        print("🌟"*score)
        print()
        type_print(f"🎯 Final Score : {score}/{total}")
        type_print(f"📈 Percentage : {percent:.1f}%")

        if percent == 100:
            type_print("🏆 Outstanding! Perfect Score!")
        elif percent >= 80:
            type_print("🥇 Excellent!")
        elif percent >= 60:
            type_print("🥈 Good Job!")
        elif percent >= 40:
            type_print("🙂 Keep Practicing!")
        else:
            type_print("📚 Don't Give Up!")

        again = input("\n🔄 Play Again? (Y/N): ").strip().upper()
        if again != "Y":
            type_print("\n🙏 Thanks for playing. Have a great day! ❤️")
            break

if __name__ == "__main__":
    run_quiz()