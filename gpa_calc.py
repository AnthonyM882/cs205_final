#please enter a grade letter, letter has to be capitalized: D
#--> gpa is at 1.0

#please enter a grade letter, letter has to be capitalized: C
#--> gpa is at 1.5

#please enter a grade letter, letter has to be capitalized: B
#-->gpa is at 2.0







letter_grade= {
	'A': 4.0,
	'A-':3.7,
	'B+':3.3,
	'B':3.0,
	'B-':2.7,
	'C+':2.3,
	'C':2.0,
	'C-':1.7,
	'D+':1.3,
	'D':1.0,
	'F':0
}

check= []

letter= (input("please enter a grade letter, letter has to be capitalized: "))
counter=1


number= letter_grade.get(letter)



index=0
total=number

print(f"gpa is at {number}")

while index < len(letter):
	counter=counter+1
	letter= (input("please enter a grade letter, letter has to be capitalized: "))


	number=letter_grade.get(letter)


	total=total+number
	gpa= round(total/counter,1)


	check.append(letter_grade)

	print(f"gpa is at {gpa}")





