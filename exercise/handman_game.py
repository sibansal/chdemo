import random

def choose_word():
    words = ["python", "programming", "hangman", "computer", "science", "algorithm", "opensource", "developer"]
    return random.choice(worfs)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def main():
    print("Welcome to Hangman!")
    print("Try to guess the word. You have 6 attempts.")

    word = choose_word()
    guessed_letters = []
    attempts = 6

    while True:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha()
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word. You have {attempts} attempts left.")
        
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            break

    if attempts == 0:
        print("You ran out of attempts. The word was:", word)

if __name__ == "__main__":
    main()
