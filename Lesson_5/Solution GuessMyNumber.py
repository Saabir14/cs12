#Guess my Number Game
#A classic program that uses a while loop

#Import the random number module
import random

#Display the title and rules
print("Guess the Number Game!")
print("**********************\n")
print("I am thinking of a number between 1 and 100.")
print("Try to guess what it is in as few attempts as possible.\n")

#Initialise the variables and generate a random number between 1 and 100
number = random.randint(1, 10)
guess = int(input("What is your first guess? "))
attempts = 1

#Create the loop
#!= means not equal to
while guess != number:
    if guess > number:
        print("Too high.")
    else:
        print("Too low.")
    guess = int(input("Guess again...: "))
    attempts = attempts + 1

print("Well done! You took",attempts,"attempts to guess it was number",number,)

#Wait for the user to exit the program
#\n creates a blank line
input("\n\nPress ENTER to exit")
