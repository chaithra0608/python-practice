import random

def play():
    symbols = ['🍒', '🍇', '🍉', '7️⃣']
    results = random.choices(symbols, k=3)

    print(" | ".join(results))

    if results==['7️⃣','7️⃣','7️⃣']
        print("Jackpot! 💰")
    else:
        print("Thanks for playing!")

while True:
    play()
    choice = input("Play again? (Y/N): ").upper()

    if choice == 'N':
        print("Goodbye 👋")
        break
