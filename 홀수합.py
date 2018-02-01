k, sum1 = 0, 0
for k in range(1, 1002, 2) :
    sum1 = k + sum1
    if sum1 > 1000 :
         break

print('1부터 100의 홀수의 합에서 최초로 1000이 넘는 위치 :'+str(k))
