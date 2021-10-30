p1 = (input("please enter player 1's choice: "))
print(p1)


p2=(input("please enter player 2's choice: "))
print(p2)


if p1=="rock" and  p2=="paper":
	print("p2 wins")


elif p1 =="scissor" and p2 == "rock":
	print("p2 wins")


elif p1 == "paper" and p2 == "scissor":
	print("p2 wins")

elif p1 == "rock" and p2 == "scissor":
	print("p1 wins")

elif p1== "scissor" and p2 == "paper":
	print("p1 wins")

elif p1== "paper" and p2 == "rock":
	print("p1 wins")

elif p1== "rock" and p2 == "rock":
	print("tie no one wins")

elif p1== "scissor" and p2 == "scissor":
	print("tie no one wins")

elif p1=="paper" and p2=="paper":
	print("tie no one wins")

