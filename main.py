# cp949 error 발생(유니코드 관련)
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')
#---------------------------------

# > python -m pip install requests
import requests

indeed_result = requests.get("https://kr.indeed.com/jobs?q=python&l=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C")
                # method (function inside of an object)
print(indeed_result) # Response [200] : 잘 됐다는 뜻

# print(indeed_result.text)

# 할 일 1. 페이지 번호 추출하기
    # Beautiful Soup설치
    # >pip install beautifulsoup4
from bs4 import BeautifulSoup
indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')
# print(indeed_soup)

pagination = indeed_soup.find("div",{"class":"pagination"})

#페이지 번호가 있는 곳 : div(class='pagination) > a > span
pages = pagination.find_all('a')

spans = []
for page in pages:
    # print(page.find("span"))
    spans.append(page.find("span"))
spans = (spans[:-1]) # spans리스트의 마지막 항목(-1번째)은 항상 ">"(next button)이므로 지워주어야 함
                  # -1번째 (=마지막)항목만 빼고 리스트의 모든 값을 가져와라.

print(spans)
