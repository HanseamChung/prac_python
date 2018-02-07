import sys
import re

kname,idw,add,birth = '','','',''

r= re.compile("^[가-힣]{1,5}$" )##이름 정규식
while True : 
    str = input("한글이름 입력")
    if str =='q' :
        sys.exit(0)
    elif r.search(str) == None:
         print("잘못입력")
         continue
    else :
         kname=str
         print(str)
         break

r= re.compile(r"^\d{9}$"     )##학번 정규식
while True : 
    str = input("학번 입력")
    if str =='q' :
        sys.exit(0)
    elif r.search(str) == None or int(str[0:4])> 2017 or int(str[0:4]) < 1990 or int(str[7:9]) == 0 or int(str[7:9])> 10 :
         print("잘못입력")
         continue
    else :
         idw=str
         print(str)
         break

r= re.compile(r"^서울|대전|대구|부산|광주|인천|울산|경북|경남|충북|충남|제주|강원|전북|전남$[가-힣]{0,18}$"     )##주소 정규식
while True : 
    str = input("주소 입력")
    if str =='q' :
        sys.exit(0)
    elif r.search(str) == None:
         print("잘못입력")
         continue
    else :
         add=str
         print(str)
         break

r= re.compile(r"^\d{6}$"     )##생일 정규식
while True : 
    str = input("생일 입력")
    if str =='q' :
        sys.exit(0)
    elif r.search(str) == None:
         print("잘못입력")
         continue
    else :
         birth=str
         print(str)
         break 
