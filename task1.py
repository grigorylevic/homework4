import random

user_number = int(input("Enter your number: "))
random_number = random.randint(1, 10)
if user_number == random_number: print("You win! Number: ",str(random_number))
else: print("You lose ):! Number: ",str(random_number))