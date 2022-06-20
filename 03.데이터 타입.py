##데이터 타입

#int (정수)형

from operator import truediv


a=5
b=-5
c=0

print(type(a),type(b),type(c)) #데이터 타입 확인하기

#fluat(실수)형

d=5.5
e=-5.5
f=0.0

print(type(d),type(e),type(f)) #데이터 타입 확인하기

#과학적 표기법

g=1.234567e5

print(g)

#문자열 데이터

text = "String Date Type"
text1 = 'String "Data" Type'
text2 = 'String \"Data\" Type'

print(text)
print(text1)
print(text2)

#탈출문자
#\' , \" , \\ , \n , \r , \t

text3 = "python \'Is \"Easy"
text4 = "pyton \\Is\\ Easy"
text5 = "Python \nIs easy"
text6 = "Java \r Python Is Easy" #덮어쓰기
text7 = "Python Is \tEasy"
print(text3)
print(text4)
print(text5)
print(text6)
print(text7)

a=10
b=20
print(a, b,)
print(a, b,sep='')
print(a, b,sep='   ')
print(a, b,sep='!')
print(a, b,end='\t') #end는 밑에 있는 print와 연결시켜주는 함수
print("3번쨰 라인")

is_true = True
is_false = False

print(is_true)

#false로 판별되는 값 
#1. false인 경우
#2. 0에 해당하는 값
#3. 빈 문자
#4. [],(),{}