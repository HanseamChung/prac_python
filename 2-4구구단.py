i, k = 0, 0

for i in range(2, 5) :
    for k in range(1, 10) :
        print('%s X %s = %s' %(i, k, i*k))

print('*'*50)
    
x, y = 2, 1 

while x <= 4 :
    y=1
    while y <= 9 :
        print('%s X %s = %s' %(x, y, x*y))
        y+= 1
    x+= 1
    
