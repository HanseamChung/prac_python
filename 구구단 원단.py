wd_1 =int(input('원하는 단수를 입력하세요'))


i, k = 0, 0

for i in range(2, wd_1) :
    for k in range(1, 10) :
        print('%s X %s = %s' %(i, k, i*k))

print('*'*50)
    
x, y = 2, 1 

while x <= wd_1 :
    y=1
    while y <= 9 :
        print('%s X %s = %s' %(x, y, x*y))
        y+= 1
    x+= 1
    
