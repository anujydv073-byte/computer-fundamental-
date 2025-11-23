import random
import os

# Load high scores from file
def load_high_scores():
    if not os.path.exists("highscores.txt"):
        return {"Easy": None, "Medium": None, "Hard": None}

    with open("highscores.txt", "r") as file:
        lines = file.readlines()

    scores = {}
    for line in lines:
        level, score = line.strip().split(":")
        scores[level] = int(score) if score != "None" else None
    return scores

# Save high scores to file
def save_high_scores(scores):
    with open("highscores.txt", "w") as file:
        for level, score in scores.items():
            file.write(f"{level}:{score}\n")

# Difficulty mapping
difficulty_map = {
    "1": ("Easy", 50),
    "2": ("Medium", 100),
    "3": ("Hard", 200)
}

# Main game loop
while True:
    print("🎯 Guess the Number Game!")
    print("Choose a difficulty level:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")

    choice = input("Enter 1, 2, or 3: ")

    if choice in difficulty_map:
        difficulty, max_range = difficulty_map[choice]
    else:
        print("Invalid choice! Defaulting to Medium.")
        difficulty, max_range = "Medium", 100

    high_scores = load_high_scores()

    print(f"\n🏆 Best Attempts for {difficulty}: {high_scores[difficulty] if high_scores[difficulty] else 'No record yet'}")

    secret_number = random.randint(1, max_range)
    attempts = 0
    guess = None

    print(f"\nI'm thinking of a number between 1 and {max_range}.")

    # Game loop
    while guess != secret_number:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess > secret_number:
            print("Too high! Try again.\n")
        elif guess < secret_number:
            print("Too low! Try again.\n")
        else:
            print(f"🎉 Correct! The number was {secret_number}.")
            print(f"You guessed it in {attempts} attempts.")

    # Update high score if it's a new record
    if high_scores[difficulty] is None or attempts < high_scores[difficulty]:
        print("🏅 NEW HIGH SCORE! Congratulations!")
        high_scores[difficulty] = attempts
        save_high_scores(high_scores)

    # Restart option
    restart = input("\nDo you want to play again? (Y/N): ").strip().lower()
    if restart != "y":
        print("Thanks for playing! Goodbye 👋")
        break
