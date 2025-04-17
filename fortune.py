# fortune.py

# Display a welcome message with name and admission number
print("Welcome to Spandan Kundu's Fortune Teller (21JE0937)") 
mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()
if mood == "happy":
    print("\n😊 Your joy is contagious. Keep spreading happiness!")
elif mood == "sad":
    print("\n💙 Tough times never last, but tough people like you do.")
elif mood == "neutral":
    print("\n😐 Balance is a strength. Spandan Kundu believes you'll find your way!")
else:
    print("\n🤔 Mood not recognized. Just remember: every day is a new chance to shine!")

