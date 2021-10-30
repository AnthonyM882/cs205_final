#example run
sides= int(input ("please enter your sides of the shape")) 
if sides==3:
	print ("triangle")
#A triangle is what we get if we enter 3


elif sides==4:
	print("square")
#A square is what we get if we enter 4

elif sides==5:
	print("pentagon")
#A pentagon is what we get if we enter 5

elif sides==6:
	print("hexagon")
#A hexagon is what we get if we enter 6

elif sides==7:
	print("heptagon")
#A heptagon is what we get when we enter 7

elif sides==8:
	print("octogon")
#An octogon is what we get when we enter 8

elif sides==9:
	print("nanogon")
#A nanogon is what we get when we enter 9

elif sides==10:
	print("decagon")
#A decagon is what we get if we enter 10

else:
	print("out of range")
#It out of range if it is not 3-10
