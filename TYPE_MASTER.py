import random
import time

easy_texts = [
    "The quick brown fox jumps over the lazy dog.",
    "Simplicity is the ultimate sophistication.",
    "Life is what happens when you're busy making other plans.",
    "All that glitters is not gold.",
    "A penny for your thoughts.",
    "Actions speak louder than words.",
    "Barking up the wrong tree.",
    "Beauty is in the eye of the beholder.",
    "Better late than never.",
    "Don't count your chickens before they hatch."
]

medium_texts = [
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.",
    "In three words I can sum up everything I've learned about life: it goes on.",
    "The only limit to our realization of tomorrow will be our doubts of today.",
    "Life is really simple, but we insist on making it complicated.",
    "The journey of a thousand miles begins with a single step.",
    "Time flies over us, but leaves its shadow behind.",
    "Our lives begin to end the day we become silent about things that matter.",
    "You miss 100% of the shots you don't take.",
    "The best revenge is massive success.",
    "Success is not the key to happiness. Happiness is the key to success."
]

hard_texts = [
    "The only way to do great work is to love what you do.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "The greatest glory in living lies not in never falling, but in rising every time we fall.",
    "I have not failed. I've just found 10,000 ways that won't work.",
    "You can't blame gravity for falling in love.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "It always seems impossible until it's done.",
    "If you can dream it, you can do it.",
    "Hardships often prepare ordinary people for an extraordinary destiny.",
    "The only person you are destined to become is the person you decide to be."
]

all_texts = easy_texts + medium_texts + hard_texts

def get_text(difficulty):
    return random.choice(all_texts)

def typing_speed_test():
    print("Select typing style:")
    print("1. Touch Typing")
    print("2. Hunt-and-Peck")
    style_choice = input("Enter your choice (1/2): ")

    if style_choice == "1":
        typing_style = "Touch Typing"
    elif style_choice == "2":
        typing_style = "Hunt-and-Peck"
    else:
        print("Invalid choice. Exiting.")
        return

    print("Select difficulty level: ")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    level_choice = input("Enter your choice (1/2/3): ")

    if level_choice == "1":
        difficulty = "easy"
    elif level_choice == "2":
        difficulty = "medium"
    elif level_choice == "3":
        difficulty = "hard"
    else:
        print("Invalid choice. Exiting.")
        return

    chosen_text = get_text(difficulty)

    print("Type the following:")
    print(chosen_text)

    input("Press Enter when you're ready...")

    start_time = time.time()

    user_input = input("Start typing: ")

    end_time = time.time()

    time_taken = end_time - start_time
    words_typed = len(user_input.split())
    characters_typed = len(user_input)

    wpm = (characters_typed / 5) / (time_taken / 60)
    accuracy = (sum(1 for c1, c2 in zip(chosen_text, user_input) if c1 == c2) / len(chosen_text)) * 100

    mistakes = sum(1 for c1, c2 in zip(chosen_text, user_input) if c1 != c2)

    if accuracy >= 0 and accuracy < 20:
        stars = 1
    elif accuracy >= 20 and accuracy < 40:
        stars = 2
    elif accuracy >= 40 and accuracy < 60:
        stars = 3
    elif accuracy >= 60 and accuracy < 80:
        stars = 4
    else:
        stars = 5

    stars_display = "★" * stars + "☆" * (5 - stars)
    
    print("\n\n")
    print(f"Your typing speed: {wpm:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Mistakes: {mistakes}")
    print(f"Ranking: {stars_display}")
    print(f"Typing Style: {typing_style}")

    if typing_style == "Touch Typing":
        print("Tips: Focus on using the correct fingers for each key. Maintain a steady rhythm and avoid looking at the keyboard.")
    elif typing_style == "Hunt-and-Peck":
        print("Tips: Try to improve your typing accuracy by practicing more. Consider learning touch typing for better efficiency.")
    
    print("\n\n")  

    restart = input("Do you want to restart? (yes/no): ")
    if restart.lower() == "yes":
        typing_speed_test()

typing_speed_test()
