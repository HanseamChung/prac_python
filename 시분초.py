def cal_time(time) :
    h = (time//3600)
    m = (time%(3600)//60)
    s = (time%(3600)%60)
    if time < 24*60*60 :
        print('%s 시 %s 분 %s 초' %(h,m,s))
    else : print('입력시간이 하루를 초과합니다')

# %는 나머지 // 는 몫
