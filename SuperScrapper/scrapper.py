# stackoverflow job scrapping
# step 1 : get the page
# step 2 : make the requests
# step 3 : extract data

#>pip install requests
#>pip install beautifulsoup4
from warnings import resetwarnings
import requests
from bs4 import BeautifulSoup

#여기서는 python만이아니라 다양한 주소를 검색하고 싶기 때문에 URL를 미리 선언하지않고 
# 유저 입력값(word)을 받아서 첫 get_jobs()함수 안에서 URL을 만들어줌.

def get_last_page(URL):  # 가져와야할 총 페이지수 구하기
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pages = soup.find("div", {"class": "s-pagination"}
                      ).find_all("a")  # 모든 a태그를 '리스트'로 가져오기
    # print(pages)
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)  # extract_jobs()에서 range쓰기 위해


def extract_job(html):
    title = html.find("a")["title"]
    link = html.find("a")["href"]
    company = html.find("span").get_text(strip=True)
    location = html.find(
        "span", {"class": "fc-black-500"}).get_text(strip=True)
    # print(title,link,company,location)
    return {'title': title,
            'company': company,
            'location': location,
            'link': f"https://stackoverflow.com{link}"}


def extract_jobs(last_page,URL):
    jobs = []
    for page in range(last_page):
        # print(page + 1) #페이지수 뽑아보기
        print(f"Now scrapping... StackOverflow page {page+1}")
        result = requests.get(f"{URL}&pg={page+1}")
        # print(result.status_code) #구동확인
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "grid--cell fl1"})
        for result in results:
            # 각각의 div를 하나씩 돌면서 extract_job을 돌려줌. ->여기서 나오는 return값을 job변수에 저장하기.
            job = extract_job(result)
            jobs.append(job)  # 위에서 저장한 job변수를 jobs 리스트에 넣기.
    return jobs


def get_jobs(word):
    url = f"https://stackoverflow.com/jobs?q={word}" #get_last_page(), extract_jobs에 넣어줄 URL
    last_page = get_last_page(url)  # 함수에서 return된 값을 받아와서 새로운 변수에 저장
    jobs = extract_jobs(last_page,url)
    return jobs
