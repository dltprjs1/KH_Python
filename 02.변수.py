'''

a,b=100,200
a,b=b,a+b
a+b의 우선순위가 높아서 a=300 
print(a,b) 

'''



'''
text="Welcom to python!!!"

#print(text)

print((text+"\n")*10)

'''



'''
name="이세건"
phone="010-7724-7848"
address="서울_특별시_동대문구"
#변수의 이름은 문자,숫자, 밑줄(_)을 포함할 수 있다. ex)!,@ 등 특수 기호는 포함 될 수 없다
#변수의 이름은 숫자로 시작할 수 없다. ex)1apple 불가능
#공백을 포함할 수 있다.
#예약어는 사용할 수 없다.

print(name)
print(phone)
print(address)



#올바른 예

from http.client import INSUFFICIENT_STORAGE
from locale import format_string


apple="사과"
apples="사과들"
apple3="사과3개"
app3le="사3과"
red_apple="빨간 사과"
very_dilicious_red_apple="아주 맛있는 빨간 사과"

print(red_apple)
print(very_dilicious_red_apple)

#잘못된 예

3apple = "3개의 사과"
red apple = "빨간 사과"
apple! = "사과!"
apple$ = "사과$"
apple& = "사과&"
'''