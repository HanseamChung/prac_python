import os
import urllib.parse
import urllib.request
import re
import time
import random

from bs4 import BeautifulSoup

url1 = 'http://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code='
url2= '&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAllready=false&isMileageSubscriptionReject=false&page='
hdr= {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537. 36 (KHTML, like Gecko) Chrome/46.0.2490.84 Safari/537.36',
    'Hose' : 'movie.naver.com',
    'connection' : 'keep-alive',
    'referer' : 'http://m.naver.com'
    }

def split_url():
    url = input('url을 입력하시오: ')
    code_str = re.search('code=[0-9]*',url).group() #url에서 정규식 'code=[0-9]*'에 해당한 문자열을 리턴한다
    code = re.search('[0-9]+', code_str).group() #code_str에서 정규식 숫자열을 반환한다.

    return code

def fetch_score_result(URL):
    print(URL) #입력받았던 URL을 산출한다
    result = {} #result를 딕셔너리로
    result_list = [] #result_list를 리시트형으로 만든다

    res = urllib.request.Request(URL, headers=hdr) #URL에서 headers값이 hdr인 값을 요청해서 res에 대입
    response = urllib.request.urlopen(res) #res에 입력된 url을 입력
    html = response. read()

    soup = BeautifulSoup(html, 'html.parser')

    score_result = soup.find('div', class_='score_result').find('ul')#'ul'이 있는 부분에서 'div'부분을 찾고 클래스를 score_result로 설정
    lis= score_result.find_all('li')#li로 되어있는 값을 모두 lis에 입력

    for li in lis :
        score = li.find('div', class_='star_score').find('em').get_text() #lis내 리스트에서 'em'이 들어간 단어 중 'div를 찾은 후 score 산출
        
        spectator = li.find('div', class_='score_reple').find('span').get_text() #lis내 리스트에서 'span'이 들어간 단어 중 'div를 찾은 후 spectator에 산출
        review = li.find('div', class_='score_reple').find('p').get_text() #lis내 리스트에서 'p'가 들어간 단어 중 'div를 찾은 후 review 산출

        if spectator =='관람객': # spectator가 관람객일 때 
            review = review[3:] #review는 review 3~끝까지 산출

        result['score'] =score #result 딕셔너리의 'score'의 value값은 score
        result['review'] =review #result 딕셔너리의 'review'의 value값은 review

        result_list.append({'score' : score,
                            'review' : review}) #result_list에 해당 값을 추가

        return result_list

def input_save_path() :
    save_path = str(input('input save path: ')) #input save path 에 path를 입력하면 save_path에 저장됨 
    save_path = save_path.replace('\\','/') # save_path에서 '\\'를 '/'로 바꿈
    if not os.path.isdir(os.path.split(save_path)[0]) : # save_path의 0번째 리스트에서 디렉토리가 존재하지 않으면
        os.mkdir(os.path.split(save_path)[0]) #경로를 생성함
    return save_path

def fetch_reviews():
    code = split_url()
    f= open(input_save_path(), 'w', encoding = 'utf-8')
    page = 1
    while True:
        count = int(input('게시물의 검색 개수를 입력하시오(10단위) : '))
        if count %10 ==0: # count에서 입력받은 값의 10으로 나눈 나머지가 0이라면 루프를 종료한다
            break
    l_count = 1 # l_count에 1을 대입한다
    isLoop = True #isLoop가 True값일때까지 반복한다
    while isLoop:
        URL = url1 + code + url2 + str(page) #미리 선언한 url1, url2, split_url()함수에서 가져온 code값을 합친다
        result_list = fetch_score_result(URL) 

        for r in result_list: #result_list의 수만큼 반복

            f.write('=='* 40 + '\n')
            f.write('영화 평점: ' + r['score'] +'\n')
            f.write('리뷰 내용: ' + r['review'] +'\n')
            f.write('=='* 40 + '\n')
            l_count += 1
            if l_count > count:
               isLoop = False
               break
        page += 1
        if not isLoop or l_count == count :
            isLoop = False
            break

        sleepTime = random.randint(4, 10) #4~10초 사이의 무작위 값을 sleepTime으로 설정
        time.sleep(sleepTime) # 값을 받아 슬립타임으로
        print(str(sleepTime) + '초 기다렸습니다.') #기다린 값을 산출
    f.close()
fetch_reviews()
