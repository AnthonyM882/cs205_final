#Sample run
level=int(input("please enter a decibel level :"))
if level== 130:
	print("it is a jackhammer")
#it is a jackhammer if we enter 130


elif level== 106:
	print("it is a gas lawnmower")
#it is a gas lawnmower if we enter 106

elif level== 70:
	print("it is an alarm clock")
#it is an alarm clock if we enter 70

elif level== 40:
	print("it is a quiet room")
#it is a quiet room if we enter 40

elif level<40:
	print ("it is quieter than a quiet room")
#it is queiter than a quiet room if we enter a number less than 40

elif level >130:
	print("it is louder than a jackhammer")
#it is louder than a jackhammer if we enter a number greater than 130

elif level >106<130:
	print("it is louder than a gas lawnmower but quieter than a jackhammer")
#it is louder than a gas lawnmower but quieter than a jackhammer if we enter any number in bewteen 106 and 130

elif level >70<106:
	print("it is louder than an alarm clock but quieter than a gas lawnmower")
#it is louder than an alarm clock but quieter than a gas lawnmower if we enter any number in betwenn 70 and 106

elif level >40<70:
	print("it is louder than a queit room but quieter than an alarm clock")
#it is louder than a quiet room but quiter than an alarm clock if we enter any number in between 40 and 70
