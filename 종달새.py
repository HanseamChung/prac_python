import random

time=int(random.randint(1, 24))
wet=random.randint(0,1)

if 6 <= time <= 9 and wet == 0 :
    print("현재 시간은 %d시 이고 날씨는 맑아 종달새가 노래를 합니다." %time)
else :
    print("시간이 6-9시가 아니거나 날씨가맑지 않아 노래를 안부릅니다" )
