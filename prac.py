# tuple (값 변경 불가)
t_days = ('Mon','Tue','Wed','Thur','Fri')
print(type(t_days))

# list
l_days = ['Mon','Tue','Wed','Thur','Fri']
print(type(l_days))

# dictionary {key:value}
youngsun = {
    "name" : "Youngsun",
    "age" : 25,
    "Korean":True,
    "fav_food":["ttoekbokki","steak"]
}
print(youngsun)
youngsun["Handsome"] = True #Boolean value 추가하기
print(youngsun["age"])

#-----function() -행동(기능)의 반복
#Built-in functions
print(len("adfjerqiqjksjdfidfhgqew"))

age="18"
print(type(age))
n_age= int(age) #str을 int로 바꾸기
print(n_age)
print(type(n_age))

# HOW TO Define a function (Indentation is important!)
def say_hello(who):
    print("Hello",who)

say_hello("Sunny")
#--- 함수에서 필요한 인자만큼 꼭 입력해줘야함
def plus(a,b):
    print(a+b)

plus(2,7)
#---
def minus(a,b=1): # b : default value
    print(a-b)

minus(4) # a에만 입력값이 들어가서 a-b가 계산됨
#---
def say_hi(name = "anonymous"):
    print("hello",name)
say_hi() #입력할 값이 없으면 deault value가 입력되어 실행됨.
say_hi("Sunny")

# print와 return의 비교
def p_plus(a,b):
    print(a+b)

def r_plus(a,b):
    return(a+b) # return은 함수를 종료시킴

p_result = p_plus(2,3) # print하면 함수 호출시 값이 한번만 '출력'됨. 저장은 X, 그냥 나에게 보여지는 것.
r_result = r_plus(2,3) # return을 주면 함수 호출시 그 값이 저장됨
print(p_result,r_result) # 결과 : None, 5

# keyword argument vs positional argument
k_result = r_plus(b=30, a=1) # a와 b의 순서가 중요X
p_result = r_plus(1,30) # a와 b의 순서가 중요O

# format"string{function}string"
def helllllo(name,age):
    return f"Hello {name}, You are {age} years old."

hello = helllllo(age = "25",name = "sunnysunny") # keyword argument사용 (argument가 여러개 일 때 유용)
print(hello)

# ----------Code Challenge! --> "calc.py"

# if, else
def type_plus(a,b):
    if type(b) is int or type(b) is float:
        return a+b
    else:
        return None

print(type_plus(12,"7")) #b가 int나 float(소수점)이 아닐 때 -> None
print(type_plus(12,7))

# if else and or
def age_check(age):
    print(f"You are {age} years old.")
    if age < 18:
        print("You can't drink.")
    elif age == 18 or age == 19:
        print("Congrats! You are new to this!")
    elif age > 20 and age <25:
        print("Oh, You are still kinda young!")
    else:
        print("Enjoy your drink!")

age_check(13)
age_check(18)
age_check(22)
age_check(41)

# for in (tuple/list의 값을 하나씩 엔터치며 출력가능!)
fi_days = ("Mon","Tue","Wed","Thu","Fri")

for x in fi_days: #여기서 'x'는 작업이 시작되면 생김! x는 배열의 item을 가리킴
    print(x)

#<< the "for" statement is used to iterate over the elements of a sequence
#   (such as a "string", (tuple) or [list])
#   or other literable object >>


    #-- How to stop the For loop?
for day in fi_days:
    if day is "Wed":
        break
    else:
        print(day) #결과 Mon
                   #     Tue





