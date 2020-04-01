def score_average():
    print("Enter your scores.")
    count=0
    total=0
    while True:
        score=int(input("score: "))
        while not score.isdigit():
            score=input("input agian")
            if int(score)<0 and int(score)>100:
                score=intput("score again: ")
            elif int(score)>0 and int(score)<=100:
                count+=1
                total+=int(score)
            else:
                break
        if count==0:
            average=int(total/score)
            print("Your average score of"+count+"subject(s)"+"is"+average)
               

print(score_average())


        



