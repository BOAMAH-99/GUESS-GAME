import time
import random

print("Welcome To The Number Guessing Game!")
time.sleep(2)

print("I am thinking of a number between 1 - 100. Guess the exact number in your selected difficulty number of tries")
time.sleep(4)

print("Please select your difficulty level.")
print("Easy : 10 Tries - 1" )
print("Medium : 5 Tries - 2" )
print("Difficult : 3 Tries - 3" )
time.sleep(3)

pick = input("Enter your choice: " )

if pick == "1":
    print("Great! You have succesfully selcted easy mode. You have 10  tries to guess the correct number")
    Tries = 10
elif pick == "2":
    print("Great! You have succesfully selcted medium mode. You have 5 tries to guess the correct number")
    Tries = 5
elif pick == "3":
    print("Great! You have succesfully selcted difficult mode. You have 3 tries to guess the correct number")
    Tries = 3
else:
    print("Invalid Input")
        
time.sleep(1)

print("Loading...")
time.sleep(1)

print("Loading..")
time.sleep(1)

print("Loading.")
time.sleep(1)

print("Let us start the game")
time.sleep(2)

answer = random.randint(0,100)

def game(Tries):
    for attempt in range (1,Tries + 1):
        guess = int(input("Enter your guess: "))

        if guess > answer:
            print(f"Incorrect! The number is less than {guess}")
        elif guess < answer:
            print(f"Incorrect! The number is greater than {guess}")
        elif guess == answer:
            print(f"Congratulations! You guessed the right number, you are the man!!")

            break
    else:        
        print(f"Sorry! You have exhausted all your chances,The correct number was {answer}")

game(Tries)