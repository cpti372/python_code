def score_average() :
	print("Enter your scores. i will calculate your average score.")

	count = 0
	total = 0

	while True :
		score = input("score : ")
		while not score.isdigit() : 
			score = input("input again : ")
		while not(int(score) >= 0 and int(score) <= 100) :
			score = input("input again : ")
		if(int(score) >= 60 and int(score) <= 100) :
			count = count + 1
			total = int(total) + int(score)
		elif(int(score) < 60 and int(score) > 0) :
			count = count + 1
			total = int(total) + int(score)
		else :
			break

	if (count == 0) :
		print("There is no score.")
	else :
		print("Your average score of", count, "subject(s) is", round(total / count, 1))

score_average()