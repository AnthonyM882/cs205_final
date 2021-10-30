p1 = (input ("please enter player 1's choice: "))
print(p1)
#player 1 decides which to pick out of rock, paper, scissor

p2 = (input("please enter player 2's choice: "))
print(p2)
#player 2 decides which to pick out of rock, paper, scissor

if p1 =="rock" and p2 =="paper" or  p1 =="scissor" and p2 =="rock" or p1 =="paper" and p2 =="scissor":
	print("player 2 wins")
#player 2 chose rock hence player 1 lost
#player 2 chose scissor hence player 1 lost
##player 2 chose paper hence player 1 lost


elif p1 =="rock" and p2 =="scissor" or p1 =="scissor" and p2 =="rock" or p1 =="paper" and p2 =="rock" :
	print("player 1 wins")
#player 1 chose rock hence player 2 lost
#player 1 chose scissor hence player 2 lost
##player 1 chose paper hence player 2 lost


elif p1 =="rock" and p2 =="rock" or p1 =="scissor" and p2 =="scissor" or p1 =="paper" and p2 =="paper":
	print("tie no one wins")

#both players chose the same no one loses

else:
	print ("no one wins")

