#--- Module : Sets of functionality -import required (웹에서 이미 만들어진 코드, 내가 만든 파일의 함수 등)
# -- https://docs.python.org/3/py-modindex.html --

# import math                   #math module의 모든 기능을 import
# print (math.ceil(1.2))
# print (math.fabs(-2.3))

# from math import ceil, fsum    # math의 두가지 기능만 import
# print(ceil(1.2))
# print(fsum([1,2,3,4,5,6,7]))

from math import fsum as go_sum #math에서 fsum을 import하면서 별명지어주기
print(go_sum([1,4,1,3,2]))

from calc import cal_plus, cal_division  # calc.py에서 함수 가져오기 ()
print(cal_plus(4,2), cal_division(8,2))
