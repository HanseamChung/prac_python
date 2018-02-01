list_ex1=['risk','issue','test','maintenance','maturity']
list_ex2=['security','plan','design','systematic','safety']
list_ex3=['maintenance','verification','validation']
list_ex=[list_ex1,list_ex2,list_ex3]
for i in range(0, 3) :
    if 'maintenance' in list_ex[i] and len(list_ex[i]) >=5 :
        print('list_ex'+str(int(list_ex.index(list_ex[i]))+1)+
              '는 시험문제로 쓰일 수 있습니다.')
    else : print('list_ex'+str(int(list_ex.index(list_ex[i]))+1)+
                 '는시험문제로 쓰일 수 없습니다.')
