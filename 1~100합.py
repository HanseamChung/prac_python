hap, i = 0, 0

for i in range(1,101) :
     hap+=i

     if hap >=1000 :
         break

print('1~100의 합에서 최초로 100이 넘는 위치 :' +str(i))
