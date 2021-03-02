#가상환경 만들기 (참고: https://flask.palletsprojects.com/en/1.1.x/installation/#install-virtualenv)
# >py -3 -m venv venv
# >venv\Scripts\activate
# >pip install Flask
from flask import Flask

app = Flask("SuperScrapper")

#----- "@" : "Decorater" : 바로아래의 함수를 찾아서 실행해준다.
@app.route("/") #localhost:5000/ 주소를 불렀을때 아래 함수를 실행하겠다
def home():
    return "Hello! Welcome to mi casa!"

@app.route("/contact") # == http://127.0.0.1:5000/contact
def phone():
    return "Contact me! ☎010-9679-5614"

app.run(host="127.0.0.1")