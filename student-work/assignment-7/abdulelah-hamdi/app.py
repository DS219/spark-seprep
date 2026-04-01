import datetime
import random

def main():
    quotes = [
        "First, solve the problem. Then, write the code.",
        "Code is like humor. When you have to explain it, it’s bad.",
        "Fix the cause, not the symptom.",
        "Simplicity is the soul of efficiency.",
        "Before software can be reusable it first has to be usable."
    ]

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print("="*40)
    print(f"STATUS REPORT: {now}")
    print("="*40)
    print(f"Message of the day: {random.choice(quotes)}")
    print("="*40)
    print("Container execution successful. Have a great day!")

if __name__ == "__main__":
    main()
