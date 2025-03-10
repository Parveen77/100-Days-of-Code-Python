import random

print("Welcome to the number guessing game")
print("I'm thinking between 1 to 100")
level = input("Choose the level as easy or hard :").lower()

if level == "easy":
    print("You have 10 attempts")
    number_of_attempts = 10
elif level == "hard":
    print("You have 5 attempts")
    number_of_attempts = 5
else:
    print("Invalid input")

number = random.choice(range(1,101))
print(number)

game_over =  False

while not game_over:
    guess_the_number = int(input("Make a guess: "))
    if guess_the_number == number:
        print("Correct guess. You won")
        game_over = True
    elif guess_the_number < number:
        print("Too low \nGuess again")
        number_of_attempts -=1
        print(f"You have {number_of_attempts} attempts to guess the number")
    elif guess_the_number > number:
        print("Too high \nGuess again")
        number_of_attempts -=1
        print(f"You have {number_of_attempts} attempts to guess the number")
    else:
        print("Invalid input /nGuess again")
        number_of_attempts -=1
        print(f"You have {number_of_attempts} attempts to guess the number")
        
    if number_of_attempts == 0:
        game_over =True