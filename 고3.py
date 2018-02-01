go3=input('학년을 입력해라')
coat=int(input('코트 몇개살꺼니'))

if go3 == '3' :
    price = 3300*coat*0.9
else : price = 3300*coat

print('총 금액은 %s 원 입니다' %price)
