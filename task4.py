import random

random_expression = random.randint(1, 2)
random_num_1 = random.randint(-10, 10)
random_num_2 = random.randint(-10, 10)
random_answer = None

if random_expression == 1:	
	random_answer = random_num_1 - random_num_2
	print("How much will: ", str(random_num_1), " - ", str(random_num_2),"?")
else:  
	random_answer = random_num_1 + random_num_2
	print("How much will: ", str(random_num_1), " + ", str(random_num_2),"?")


user_num = int(input("Enter answer: "))
if user_num != random_answer: print("You are not right. Correct answer: ", str(random_answer))
else: print("You are right! Correct answer!")
