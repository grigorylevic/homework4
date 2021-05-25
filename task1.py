"""
The Guessing Game.

Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated. The result should be sent back to the user via a print statement.

"""


import random

user_number = int(input("Enter your number: "))
random_number = random.randint(1, 10)
if user_number == random_number: print("You win! Number: ",str(random_number))
else: print("You lose ):! Number: ",str(random_number))
