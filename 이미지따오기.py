import urllib.parse
import urllib.request
import re

def input_query():
    q=urllib.parse.quote_plus(str(input("검색할 단어를 입력하세요:")))
    return "&query=" + q

def bind_url() :
    defalult_url = 'https://openapi.naver.com/v1/search/image.xml?' #개발자 방향지시서
    start = '&start=1'
    sort ='sort=sim'
    display = '&display=10'
    query = '&query='+urllib.parse.quote_plus(str(input('검색어를 입력하세요.'))) #qute_plus 는 검색어 입력 받은 것을 컴퓨터 언어로 변환 
    full_url = defalult_url + sort + start + display + query 
    #print(full_url)
    return full_url

def fetch_cotents_from_url():
    url = bind_url()
    #full_url이 url에 담김
    headers={
    'Host': 'openapi.naver.com',
    'User=Agent' : 'curl/7.43.0',
    'Accept':'*/*',
    'Content-Type':'application/xml',
    'X-Naver-Client-Id' : 'uaHf_SWPNTET2f06ND31' ,
    'X-Naver-Client-Secret' : 'rWlphqrb2C'
    }
    r = urllib.request.Request(url,headers=headers) # 해당 사이트를 치고, 인증을해줌
    m=urllib.request.urlopen(r)
    html=m.read() # 가져 온 것을 read -> html에 넣음
    #print(html)
    return html

def extract_text_in_tags(tags,tagname ='title') :
    txt = []
    reg = '[^<' +tagname +'>][^<]+'
    for tag in tags :
        txt.append(re.search(reg,tag).group())
    return txt

def get_contents_from_html() :
    html = fetch_cotents_from_url()
    #print(html)
    title_tags = re.findall('<title>[^<]+</title>',html.decode('utf-8')) #utf-8로 디코드 후 양식에 맞춰 검색(title테그)
    link_tags = re.findall('<link>[^<]+</link>',html.decode('utf-8')) #utf-8로 디코드 후 양식에 맞춰 검색(link테그)
    #print(title_tags)
    #print('\n')
    #print(link_tags)
    titles = extract_text_in_tags(title_tags,tagname='title')
    links = extract_text_in_tags(link_tags,tagname='link')
    f = open('image.html','w')
    f.write('<html><body>')
    for i in range(1,len(titles)) :
        f.write('<p>'+titles[i]+'</p>')
        f.write('<img src ='+links[i]+'/>')
    f.write("</body></html>")
    f.close()

get_contents_from_html()
    
