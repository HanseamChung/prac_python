wd_1 =int(input('원하는 숫자 1개 골라라'))
wd_2 =int(input('두 번째 원하는 숫자 1개 골라라'))
sum1 = 0
for k in range(wd_1, wd_2+1) :
    sum1 = k + sum1
print('두 수 간의 모든 수를 더하면 %s 가 나온다' %sum1)
