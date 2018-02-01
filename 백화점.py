t_t=int(input('티셔츠의 구매 갯수를 입력하시오'))
s_t=int(input('스웨터의 구매 갯수를 입력하시오'))
total=int(10000*t_t + 30000*s_t)

if total <= 100000 :
    price = 0.95*total
else : price = 0.85*total

print('총 금액은 %s 원 입니다' %price)
