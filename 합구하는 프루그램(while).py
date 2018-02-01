

num1=int(input("시작값 입력 : "))
num2=int(input("끝값 입력 :"))
num3=int(input("증가값 입력 :"))

i, hap =num1, 0

while i <= num2 :
    hap = i+ hap
    i = num3+i

print ("%d에서 %d까지 %d 씩 증가함 값의 합 : %d" %(num1,num2,num3, hap))
