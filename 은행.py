bank=input('은행 이름이뭐니')
method=input('통장이니 카드니으로 할거니')
money=input('돈이니 수표니')

if bank== '파이' and method =='카드' or method =='통장' and money =='돈' :
    print('입금가능')
else : print('입금불가능')
