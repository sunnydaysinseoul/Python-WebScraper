# cp949 error 발생(유니코드 관련)
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')
#---------------------------------
# > python -m pip install requests
# >pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup

INDEED_URL="https://kr.indeed.com/jobs?q=python&l=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C"

def extract_indeed_pages():
    result = requests.get(INDEED_URL)
    soup = BeautifulSoup(result.text, 'html.parser')

    pagination = soup.find("div",{"class":"pagination"})
    
    #페이지 번호가 있는 곳 : div(class='pagination) > a > span
    links = pagination.find_all('a') #모든 a태그를 '리스트'로 가져오기

    pages = []
    for link in links[0:-1]: #처음부터 link(a 태그)의 마지막거 (next button)은 제외하고 각 값마다 loop돌리기
        pages.append(int(link.string)) #페이지번호가 string으로 가져와지니까 integer로 변환해주기

    max_page = pages[-1] #마지막 페이지번호 찾기
    # print(max_page) #확인용
    return max_page
    

# extract_indeed_pages() #확인용