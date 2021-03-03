#가상환경 만들기 (참고: https://flask.palletsprojects.com/en/1.1.x/installation/#install-virtualenv)
# >py -3 -m venv venv
# >venv\Scripts\activate
# >pip install Flask
#파일 실행하기(현재폴더에서) : >py main.py
from flask import Flask, render_template, request, redirect
from scrapper import get_jobs
app = Flask("SuperScrapper")


#검색시마다 페이지들 스크래핑해오느라 시간이 한참걸리니 fake db를 만들어주자. 
# ->한번만 검색하면 db dictionary에 이미 저장된 값을 가져오면 되니 훨씬 빠름
#db가 route안에 들어가있으면 실행시마다 초기화되서 big No
db = {}

#----- "@" : "Decorater" : 바로아래의 함수를 찾아서 실행해준다.
@app.route("/") #host:5000/ 주소를 불렀을때 아래 함수를 실행하겠다
def home():
    return render_template('home.html') # import와 함께 사용

@app.route("/report") #검색할 때 올 페이지
def report(): #사용자가 찾으려고하는 단어 (parameter=value에서 value) 가져오기
    word = request.args.get('word') # = user가 입력한 검색값(주소에서 가져옴)
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs: #db에 입력된 word사전이 존재하면.
            jobs = existingJobs
        else:
            jobs = get_jobs(word) #scrapper의 get_jobs함수에 user가 입력한 word를 입력(입력한 단어를 주소에넣어서 scrapping)
            db[word] = jobs
    else: #주소에서 user가 입력한 word가 없을 때 home으로 redirect.
        return redirect("/")
    
    return render_template("report.html",
                            searchingBy=word,
                            resultsNumber=len(jobs),
                            jobs = jobs #html에서 for문으로 job하나씩 가져올 것임
                            )
    #이렇게 값(word)을 받아와서 html의 '{{searchingBy}}'자리에 대체해주는 것을 "RENDERING "렌더링이라고함

# @app.route("/<username>") # 여러가지 url을 관리하는 방법! ex. instagram.com/ssuny.me <<- 요거
# def name(username):
#     return f"Hello your name is {username}!"

app.run(host="127.0.0.1")