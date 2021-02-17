# -----Code Challenge! 7가지 계산함수 만들기(user의 입력오류도 고려)
def cal_plus(a,b):
    try : return int(a)+int(b)
    except : print("숫자를 입력해 주세요")
# cal_plus = cal_plus("3",4) ##이거때문에 다른파일에서 calc를 import할 때 오류 발생했음 :(
# print(cal_plus)

def cal_minus(a,b):
    try : return int(a)-int(b)
    except : print("숫자를 입력해 주세요")
# cal_minus = cal_minus(1,"5")
# print(cal_minus)

def cal_times(a,b):
    try : return int(a)*int(b)
    except : print("숫자를 입력해 주세요")
# cal_times = cal_times("3",2)
# print(cal_times)

def cal_division(a,b):
    try : return int(a)/int(b)
    except : print("숫자를 입력해 주세요")
# cal_division = cal_division("3",2)
# print(cal_division)

def cal_negation(a):
    try : return -int(a)
    except : print("숫자를 입력해 주세요")
# cal_negation = cal_negation('10')
# print(cal_negation)

def cal_power(a,b):
    try : return pow(int(a),int(b))
    except : print("숫자를 입력해 주세요")
# cal_power = cal_power(5,'3')
# print(cal_power)

def cal_remainder(a,b): #나머지구하기
    try : return int(a) % int(b)
    except : print("숫자를 입력해 주세요")
# cal_remainder = cal_remainder(5,"김치")
# print(cal_remainder)


# 다른사람방법 (if사용)
def change(a, b, math):
    a = int(a)
    b = int(b)
    try:
        if math == "+": #이게 True일 때 return.
            return a + b
        elif math == "-":
            return a - b
        elif math == "*":
            return a * b
        elif math == "/":
            return a / b
        elif math == "**":
            return a ** b
    except:
        return "Please enter a number."


def plus(a, b):
    return change(a, b, "+")

def mius(a, b):
    return change(a, b, "-")

def times(a, b):
    return change(a, b, "*")

def division(a, b):
    return change(a, b, "/")

def negation(a):
    if a.isdecimal(): # a 가 숫자이면
        a = int(a)
        return a * -1
    else :
        return "Please enter a number."

def power(a, b):
    return change(a, b, "**")

# print(plus(4, 7))
# print(mius("4", 7))
# print(times("4", "7"))
# print(division("4", "7"))
# print(negation("4"))
# print(power("4", "7"))
# print(plus("a",4))
# print(negation("haha"))
