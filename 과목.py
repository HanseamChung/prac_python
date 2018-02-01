object_one=int(input('1과목 몇점?'))
object_two=int(input('2과목 몇점?'))
object_three=int(input('3과목 몇점?'))

if ((object_one>= 60 and object_two>= 60 and object_three>= 60)
    or (object_one + object_two + object_three)/3 >=70 ):
    print('자격증을 딸 수 있다')
else : print('자격증울 딸 수 없다')
