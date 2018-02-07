print('현재 템포는 0입니다. 템포 조정은 0부터 5 까지 가능합니다.')
num= int(input('조정하고자 하는 만큼의 크기를 입력 : '))
if num <0 or num >5 :
     print('잘못된 점수입니다')
else : print('조정한 후의 템포는 %d 입니다.' %num)
