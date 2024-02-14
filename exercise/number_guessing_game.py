import random

def generate_number():
    return random.randint(1, 100)

def main():
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")

    target_number = generate_number()
    attempts = 0

    while True:
        guess = int(input("Enter your guess (1-100): "))
        attempts += 1

        if guess < target_number:
            print("Too low! Try guessing higher.")
        elif guess > target_number:
            print("Too high! Try guessing lower.")
        else:
            print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts!")
            break

if __name__ == "__main__":
    main()
