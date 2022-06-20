#비교연산자

a=10
b=20

print(a<b)
print(a<=b)
print(a>b)
print(a>=b)
print(a==b)
print(a!=b)

#논리형 자료

is_true = True
is_false = False

print(is_true > is_false)
print(is_true < is_false)

#문자형 자료

print("Python" > "python")
print("12345" > "123444")
print("12.33" > "12.44")

#복합 대입 연산자 = += , -= , *= , **=

today = 1230
today = today+1
print(today)

today+= 1
print(today)

#논리 연산자 = and , or

print(True and True)
print(False and True)
print(10>3 and 3>5)
print(10==1 and 10==10)

print(True or True)
print(True or False)
print(False or False)

print("a" and 10>3 and 0)
print("a" and 10>3 and True and False) ##맨 뒤 값이 출력

print("a" or 10>3 or 0)
print("오아" or 10>3 or True or False)##맨 앞 값이 출력

print(True or False and "참")##맨 앞 값 출력
print(True and False or "참")##맨 뒤 값 출력
print((True or False) and "참")##맨 뒤 값 출력

