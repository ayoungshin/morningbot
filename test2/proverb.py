# 파이썬 연습장입니다. 자유롭게 연습해보세요.
#from elice_utils import EliceUtils
import urllib.request #웹 페이지 여는데 이용하는 모듈
from bs4 import BeautifulSoup # 크롤링 하는데 이용하는 모듈

#elice_utils = EliceUtils()

import random

def proverb():
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=blMy&query=%EC%9D%B8%EC%83%9D%20%EB%AA%85%EC%96%B8'
    source = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(source, "html.parser")
    words = []
    for word in soup.find_all('p', class_='lngkr'):
        words.append(word.get_text())

    print(random.choice(words))
    return random.choice(words)