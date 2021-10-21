import random   
input("First Choose your Range for Number guessing\nlike 1 to 20\nEnter To Start Game For Number Guess ")
lower_range =int(input("Enter Your Lower Range To Start Guessing Game: \n"))
upper_range =int(input("Enter Your Upper Range To Start Guessing Game: \n"))

ran_num = random.randint(lower_range,upper_range) 

num = int(input("Please Enter Your Guess Number :\n"))
while True:
	if num == ran_num: 
		print("You Guess Right Number")
		break
	else:
		print("Your Guess Was Wrong")
		break
print("The Real Number Was {}".format (ran_num))
