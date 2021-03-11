import os, re
import urllib.request as ur
from bs4 import BeautifulSoup as bs

"""
다음에서 뉴스 크롤링
"""
# 파일 저장 경로 설정
os.chdir(r'C:\Users\alstn\PycharmProjects\Web_crawl')

# 사이트 문자열을 객체에 저장
url = 'https://media.daum.net/'

# quate_crqwl.py 에서 사용한 한줄요약 코드
soup = bs(ur.urlopen(url).read(),'html.parser')

# 특정 클래스 속성을 출력하기 - 헤드라인제목들을 가져오기 위함
print(soup.find_all('div', {"class": "item_issue"}))

# a 태그 5개만 출력해보기 - a 태그는 하이퍼링크가 달리는 태그다.
print(soup.find_all('a')[:5])

# 시험 삼아 a 태그의 링크 5개만 출력
for i in soup.find_all('a')[:5]:
    print(i.get('href'))

# 특정기사 본문 저장하기
article1 ='https://www.fnnews.com/news/202102021648045539'

# soup2 객체로 열기
soup2 = bs(ur.urlopen(article1).read(), 'html.parser')

# 특정기사 본문 출력하기
for i in soup2.find_all('p'):
    print(i.text)

# 'links.txt"라는 제목의 쓰기 전용 파일을 열어줍니다.
f = open('links.txt', 'w')

# 링크 파일만 모으기
# 태그 안에 특정 속성값을 찾아낼 때 get 을 사용한다. -> 여기서는 하이퍼링크 값인 href 속성을 가져옴
# href 속성값만 추출한 이유는 해당 주소로 자동으로 다시 접속하기 위함이다.
for i in soup.find_all('div', {"class": "item_issue"}):
    f.write(i.find_all('a')[0].get('href')+'\n')
f.close()

# 기사 모으기
url = 'https://news.daum.net/'
soup = bs(ur.urlopen(url).read(), 'html.parser')
f = open('article_total.txt', 'w')
for i in soup.find_all('div', {"class": "item_issue"}):
    try:

        # 각 명령어를 실행하다가 중단되더라도 마지막까지 실행되도록 하기 위해서
        f.write(i.text+'\n')
        # 제목을 추출. '\n' 로 제목이 끝난 후 한 줄을 띄워주기
        f.write(i.find_all('a')[0].get('href') + '\n')
        # 각 영역(div) 안에서 'a' 태그를 추출, 그 안에서 하이퍼링크('href') 주소를 얻는다.
        # 그리고 바로 파일로 저장하고, 한 칸 띄워준다.
        soup2 = bs(ur.urlopen(i.find_all('a')[0].get('href')).read(), 'html.parser')

        # 위에서 얻어낸 하이퍼링크 주소를 뷰티풀소프 객체로 다시 저장
        for j in soup2.find_all('p'):
            # 다시 문단만 추출. 기사 본문을 모을 수 있다.
            f.write(j.text)
            # 추출한 문단을 파일로 저장합니다.
    except:
        pass
f.close()
