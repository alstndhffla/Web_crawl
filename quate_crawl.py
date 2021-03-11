# 정규식 모듈 re
import os, re

# URL 주소에 있는 내용을 요청할 때 사용하는 request
import requests
# urllib - 웹에서 얻은 데이터를 다룸. request - 웹 문서를 열어 데이터를 읽어오는 모듈
import urllib.request as ur

from bs4 import BeautifulSoup as bs

"""
1.  http://quotes.toscrape.com/
    뷰티플수프를 활용해 명언 사이트를 크롤링
    명언들이 태그별로 모여 있음. 명언들이 페이징되어있음.
    1. 페이지를 불러와 객체에 저장
    2. 브라우저에서 명언이 있는 위치 확인
    3. 각 태그에 맞는 명언을 찾아 출력.

2.  pip install beautifulsoup4
"""


# 접속하고 싶은 웹사이트 주소 입력. -> url 객체에는 단순히 문자열만 일단은 입력된 것
url = 'http://quotes.toscrape.com/'

# 주소에 해당하는 웹 사이트에 원하는 정보를 요청해 결과물을 반환하는 명령어 - urllib.request.urlopen('url')
# -> 실질적으로 웹사이트를 불러와 html 객체에 저장함.
html = ur.urlopen(url)
# html.read()[:100]     # html 형식으로 사이트 정보가 쭉 저장되어있다(100개까지 슬라이싱해 정보를 확인함)


# 뷰티플수프로 파싱하기 쉬운 형태로 변환 후 soup 객체에 저장 (파싱: 웹 문서에서 패턴이나 순서로 자료를 추출해 가공하는 것)
# soup 에는 <html> 시작부터 <head>, <body>, ... 등 전체 구성요소가 들어있다.
soup = bs(html.read(), 'html.parser')

# 위 3줄의 코드를 한 줄로 요약가능
# soup = bs(ur.urlopen('http://quotes.toscrape.com/').read(), 'html.parser')

"""
# find_all - 특정 태그로 둘러싸인 요소를 찾아내 리스트 형태로 반환. () 안에 '찾아낼 태그' 를 입력하면 된다.
# 명언들이 <span> 태그로 둘러싸여 있기 때문에 이를 조건으로 입력
# span 만 입력하면 명언의 앞뒤로 span 태그가 같이 붙여서 리스트화하기 때문에
"""
# # span 태그가 명언앞뒤로 붙어서 quote 에 저장됨.
# quote = soup.find_all('span')
# # html 상에서 span 태그 안에는 텍스트(명언)만 존재하기 때문에 .text 를 입력함으로써 그 안에 있는 text(명언)만 출력이 가능해짐.
# print(quote[0].text)

# 위 2줄 요약코드
print(soup.find_all('span')[0].text)

# quote 명언 하나 출력
# class 속성값이 quote 인 첫번째 <div> 태그 안에 들어있는 요소
# 해당 페이지 span 태그에는 텍스트 밖에 없지만, div 태그에는 명언이 들어간 span 태그 말고도 다른 태그들이 존재한다.
print(soup.find_all('div', {"class": "quote"})[0].text)

# 해당 페이지의 명언 모두 출력
for i in soup.find_all('div', {"class": "quote"}):
    print(i.text)



