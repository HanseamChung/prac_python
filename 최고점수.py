def max_score(score) :
    max= 0
    for num in range(0,5,1):
        if int(score[num]) <= int(score[num+1]) :
            max = score[num+1]
        else :
            max = score[num]
    print(max)
    
