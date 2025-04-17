# fortune.py

print("Welcome to Spandan Kundu's Fortune Teller (21JE0937)") 

mood = input("How are you feeling today? (happy/sad/neutral/angry/excited): ").strip().lower()

if mood == "happy":
    print("\n😊 Your joy is contagious. Keep spreading happiness!")
elif mood == "sad":
    print("\n💙 Tough times never last, but tough people like you do.")
elif mood == "neutral":
    print("\n😐 Balance is a strength. Spandan Kundu believes you'll find your way!")
elif mood == "angry":
    print("\n😡 Take a deep breath. Even volcanoes cool down eventually.")
elif mood == "excited":
    print("\n🎉 The universe is vibing with your energy! Go conquer the day!")
else:
    print("\n🤔 Mood not recognized. Just remember: every day is a new chance to shine!")
