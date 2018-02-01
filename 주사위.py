import random

p1=input("주사위를 처음 던질 사람의 이름을 정하세요")
p2=input("주사위를 다음으로 던질 사람의 이름을 정하세요.")

p1_ju = int(random.randint(1, 6))
p2_ju = int(random.randint(1, 6))

if p1_ju > p2_ju :
    print(p1 +'의 주사위 숫자는'+ str(p1_ju)+' 으로 '+ p2 +'의 주사위 숫자' + str(p2_ju)
          +'보다 높아 '+p1+"가 이겼습니다")
elif p1_ju < p2_ju :
    print(p2 +'의 주사위 숫자는'+ str(p2_ju)+' 으로 '+ p1 +'의 주사위 숫자' + str(p1_ju)
          +'보다 높아 '+p2+"가 이겼습니다")
else :
    print(p2 +'의 주사위 숫자는'+ str(p2_ju)+' 로 '+ p1 +'의 주사위 숫자' + str(p1_ju)
          +'와 같습니다') 
