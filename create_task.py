import random
print("The purpose of my function is to let the user guess the capitals of European  countries.")

countries = ["France", "Italy", "Spain", "Poland", "Germany", "Netherlands", "United Kingdom", "Norway", "Sweden", "Greece"]
capitals = ["Paris", "Rome", "Madrid", "Warsaw", "Berlin", "Amsterdam", "London", "Oslo", "Stockholm", "Athens"]
capital_temp = ["Paris", "Rome", "Madrid", "Warsaw", "Berlin", "Amsterdam", "London", "Oslo", "Stockholm", "Athens"]
count1 = 0
score = 0

def numbers(count1, capital, score):
	while count1 < 10:
		country = (countries[count1])
		capital = (capitals[count1])
		random.shuffle(capital_temp)
		print("What is the capital of", country,"? Here are your options:" "\n", capital_temp)
		if input() == capital:
			score +=1
			print("Very good! Your score is", score,"out of 10!","\n")
		else:
			print("Not very good! Your score is still", score,"out of 10!","\n","The answer was", capital,".","\n")
		count1 +=1
	if score >= 7:
		if score == 10:
			print("Excellent! You passed the test with a perfect score of", score,"out of 10!")
		else:
			print("Very good! You passed the test with a score of", score,"out of 10! Try again for a perfect score!")
	else:
		print("Not very good! You failed with a score of", score,"out of 10. Try again for a better score!")
print("Type 'start' to begin the capitals quiz. Be sure to capitalize your answers correctly!")
if input() == "start":
    numbers(count1, capitals, score)
	