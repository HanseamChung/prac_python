e_c= int(input('전기차의 현재 전기 용량을 입력하시오'))
e_a= 28

if e_c < 28 *0.3 :
    print('전체 전기 총량의 30%보다 현재 전기량이 적으니 휘발유로 주행해야함')
else :
    print('전기로 주행해요')
