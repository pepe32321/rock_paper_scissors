print("====ROCK===PAPER===SCISSORS====")
p1 = input("Player 1 write \"rock\", \"paper\" or \"scissors\" ")
p2 = input("Player 2 write \"rock\", \"paper\" or \"scissors\" ")
if p1 != "rock" and p1 != "paper" and p1 != "scissors":
	p1 = None
	print("Wrong input Player 1")
if p2 != "rock" and p2 != "paper" and p2 != "scissors":
	p2 = None
	print("Wrong input Player 2")
if not p2 and p1:
	print("Player 1 wins!")
elif not p1 and p2:
	print("Player 2 wins!")
elif not p1 and not p2:
	print("No one wins!")
elif p1 == p2:
	print("It\'s a tie!")
elif p1 == "rock" and p2 == "scissors":
	print("Player 1 wins!")
elif p1 == "paper" and p2 == "rock":
	print("Player 1 wins!")
elif p1 == "scissors" and p2 == "paper":
	print("Player 1 wins!")
else:
	print("Player 2 wins!")
print("Play again?")