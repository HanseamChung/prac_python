import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

s_1= str(input('검색분류를 입력하세요 1-뉴스, 2-블로그, 3-카페'))
if s_1 =='1' :
    s_2 = 'https://openapi.naver.com/v1/search/news.xml?'
    s_3 = '뉴스제목'
   
elif s_1 == '2' :
    s_2 = 'https://openapi.naver.com/v1/search/blog.xml?'
    s_3 = '블로그 제목'
    
elif s_1 == '3' :
    s_2 ='https://openapi.naver.com/v1/search/cafearticle.xml?'
    s_3 = '카페 제목'
    
else : print('1,2,3중에 한가지를 고르세요')

b = str(input('검색어를 입력하세요'))
c= str(input('파일명을 입력하세요'))
defaultURL =(s_2)
sort ='sort=sim'
start = '&start=1'
display = '&display=100'
query = '&query='+urllib.parse.quote_plus(b)
fullURL = defaultURL + sort + start + display + query
print(fullURL)
file= open(('C:\\python36\\%s'%c),'w',encoding='utf-8')
headers={
    'Host': 'openapi.naver.com',
    'User=Agent' : 'curl/7.43.0',
    'Accept':'*/*',
    'Content-Type':'application/xml',
    'X-Naver-Client-Id' : 'uaHf_SWPNTET2f06ND31' ,
    'X-Naver-Client-Secret' : 'rWlphqrb2C'
    }
req = urllib.request.Request(fullURL,headers=headers)
f=urllib.request.urlopen(req)
resultXML = f.read()
xmlsoup = BeautifulSoup(resultXML,'html.parser')
items = xmlsoup.find_all('item')

if s_1 =='1' :
    for item in items :
        file.write('------------------------------\n')
        file.write(s_3 + item.title.get_text(strip=True) + '\n')
        file.write('요약 내용 :' + item.description.get_text(strip=True) + '\n')
        file.write('뉴스 주소 :' + item.originallink.get_text(strip=True) + '\n')
elif s_1 == '2' :
     for item in items :
        file.write('------------------------------\n')
        file.write(s_3 + item.title.get_text(strip=True) + '\n')
        file.write('요약 내용 :' + item.description.get_text(strip=True) + '\n')
        file.write('블로그 주소 :' + item.link.get_text(strip=True) + '\n')
elif s_1 == '3' :
     for item in items :
        file.write('------------------------------\n')
        file.write(s_3 + item.title.get_text(strip=True) + '\n')
        file.write('요약 내용 :' + item.description.get_text(strip=True) + '\n')
        file.write('카페 주소 :' + item.link.get_text(strip=True) + '\n')
    
file.write('\n')
print(items[2])      
file.close()
