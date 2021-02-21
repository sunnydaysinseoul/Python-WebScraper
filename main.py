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
links = pagination.find_all('a') #모든 a태그를 '리스트'로 가져오기

    # pages = []
    # for link in links: # a리스트의 각 값마다 span찾는 loop돌리기
    #     # print(page.find("span"))
    #     pages.append(link.find("span").string) #span태그 안에있는 string(text)값만 가져오기
    # pages = (pages[0:-1]) # spans리스트의 마지막 항목(-1번째)은 항상 ">"(next button)이므로 지워주어야 함
    #                 # -1번째 (=마지막)항목만 빼고 리스트의 모든 값을 가져와라.

    # print(pages)

# 더 간단하게 : <a>안에 바로 <span>만 있고 그 안에 string(페이지번호숫자)가 있으므로
#               그냥 <a>에서 .string 을 해주어도 무관함!
pages = []
for link in links[0:-1]: #처음부터 link(a 태그)의 마지막거 (next button)은 제외하기
    pages.append(int(link.string)) #페이지번호가 string으로 가져와지니까 integer로 변화해주기
# print(pages) 

max_page = pages[-1] #마지막 페이지번호 찾기

print(range(max_page)) # range(n): create a sequence of numbers from 0 to n

for n in range(max_page):
    print(f"start={n*50}")