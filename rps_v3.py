import random
print("====ROCK===PAPER===SCISSORS====")
p1 = input("Write down \"rock\", \"paper\" or \"scissors\" ").lower()
print("You chose " + p1)
p2 = random.randint(1, 3)
if p2 == 1:
	p2 = "rock"
elif p2 == 2:
	p2 = "paper"
else:
	p2 = "scissors"
print("AI chose " + p2)
if p1 != "rock" and p1 != "paper" and p1 != "scissors":
	print("Wrong input!")
	print("You lose!")
elif p1 == p2:
	print("It\'s a tie!")
elif p1 == "rock" and p2 == "scissors":
	print("You win!")
elif p1 == "paper" and p2 == "rock":
	print("You win!")
elif p1 == "scissors" and p2 == "paper":
	print("You win!")
else:
	print("You lose!")
print("Play again?")