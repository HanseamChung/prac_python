apple=int(input('사과 몇개사니'))
grape=int(input('포도 몇개사니'))
boat=int(input('배 몇척사니'))
mandarine=int(input('귤 몇개사니'))
if grape >= 3 :
    price = (1000*apple + 3000*grape + 2000*boat + 500*mandarine)*0.9
else : price = (1000*apple + 3000*grape + 2000*boat + 500*mandarine)

print('총 금액은 %s 원 입니다' %price)
