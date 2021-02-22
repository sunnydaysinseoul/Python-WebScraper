# cp949 error 발생(유니코드 관련)
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')
#---------------------------------
# > python -m pip install requests
# >pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup
LIMIT = 50 #한 페이지 공고 개수
URL=f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&l=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C&limit={LIMIT}&radius=25"
        #URL맨 뒤에 &start=50이 오면 50번째 글 부터 출력 되므로 페이지 2가 나옴. &start=100이면 페이지 3이 나오게 됨.

def extract_indeed_pages():
    result = requests.get(URL)
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
    

# page수 만큼 request하는 함수
def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
            #필요한 last_page는 main.py에서 지정해 줄 것임.
        result = requests.get(f"{URL}&start={0*LIMIT}") #URL뒤에 &start=50 이런 숫자를 붙여서 페이지마다 값 가져오기
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all("div",{"class":"jobsearch-SerpJobCard"}) # list
        # print(results)
        for result in results: #class="jobsearch-SerpJobCard"안에서 loop
            title = result.find("h2",{"class":"title"}).find("a")["title"] #results list의 각 값(result)에서 class="title"인 <h2>를 찾고, 거기에 포함되는 class="title"인 <a>를 찾아서 출력하기.
            # .find("a").string  #이렇게 하면 None이 포함되어 나옴
            
            # company = result.find("span",{"class":"company"}).find("a") #---> span태그 안에 <a>가 한번 더 있고 그 안에 회사명이 있는애도있고 span안에 바로있는 애도 발견! :(
            company_span = result.find("span",{"class":"company"})
            
            if company_span.find("a") is None: #company span이 <a>를 가지지 않을 때
                company = company_span.string
            else:
                company = company_span.find("a").string

                ## --- 만약에 가져온 .string값 앞뒤에 공백(whitespaec이 많이 나오면
                ## ---  -> .strip(s[, chars])를 사용하면 됨.
                ## --- .strip() = 빈칸 다 지우기 / .strip("F") = string에서 "F"를 다 지우기
            
            print(title,company)
    return jobs
