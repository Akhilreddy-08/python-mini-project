import random

def main():
    print("Welcome to the Number Guessing Game!")
    print("Select a range by entering two integers (X and Y).")
    X, Y = map(int, input("Enter the lower and upper bounds (X Y): ").split())

    # Generate a random number within the specified range
    secret_number = random.randint(X, Y)
    attempts = 0

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")


main()
