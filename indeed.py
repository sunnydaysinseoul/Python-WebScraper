# cp949 error 발생(유니코드 관련)
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')
#---------------------------------

import requests
from bs4 import BeautifulSoup

INDEED_URL="https://kr.indeed.com/jobs?q=python&l=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C"

def extract_indeed_pages():
    result = requests.get(INDEED_URL)
    soup = BeautifulSoup(result.text, 'html.parser')

    pagination = soup.find("div",{"class":"pagination"})

    links = pagination.find_all('a') 

    pages = []
    for link in links[0:-1]: 
        pages.append(int(link.string)) 

    max_page = pages[-1] 
    # print(max_page) #확인용
    return max_page
    

# extract_indeed_pages() #확인용