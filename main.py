import art
import random

print(art.logo)

print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100 ")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty=="easy":
    attempts=10
else:
    attempts=5
rand_number=random.randint(1,100)
while(attempts > 0):
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess=int(input("Make a guess: "))
    if guess == rand_number:
        print(f"You got it! The answer was {rand_number}")
        break
    elif guess > rand_number:
        print("Too High!")
    elif guess < rand_number:
        print("Too Low!")
    attempts-=1
if attempts == 0:
    print("You have run out of guesses. Refresh the page to run again")
else:
    print("Refresh the page to run again")
