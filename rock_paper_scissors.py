import random 

user_wins=0
computer_wins=0

options = ["rock", "paper", "scissors"] 

while True: 
	user_input = input("Rock, Paper, Scissors or q(Quit) ").lower()  
	if user_input == "q": 
		break 

	if user_input not in ["rock", "paper", "scissors"]: 
		continue 

	random_numer = random.randint(0, 2) 
	# 0 is rock, 1 is paper, 2 is paper 
	computer_guess = options [random_number] 
	print("Computer picked", computer_pick + ".") 

	if user_input == "rock" and computer_guess == "scissors"
		print("You win!") 
		user_winds += 1

	elif user_input == "paper" and computer_guess == "rock" 
		print("You Win!") 
		user_wins +=1 

	elif user_input == "scissors" and computer_guess == "paper" 
		print("You win!") 
		user_wins +=1
	else: 
		Print ("You lose :(") 
		computer_wins += 1


print ("Your wins ", user_wins, ".", " Computer wins ", computer_wins, ".")
print("Good Game!") 




