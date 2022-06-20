#기본 연산자= + , _ , * , /
#목을 구하는 연산자= //
#나머지를 구하는 연산자= %
#제곱을 구하는 연산자= **

print(10+2)
print(10-2)
print(10*2)
print(10/2)

print(type(10/10))#정수형의 나눗셈 결과는 무조건 실수형으로 표현

print(10 // 3)
print(10 % 3)

#데이터 타입 변환 함수
#실수형,논리형,문자열

print(int(123.928712837))
print(int(True))
print(int(False))
print(type(int("23555")))
#print(int("1232ㅁㄴㅇ"))<<< 오류
#print(int("123.233"))<<< 오류

print(float(200))
print(float(False))
print(float(True))
print(float("23.12412"))
print(float("2344"))

print(str(1234213))
print(str(2434.3444))
print(str(True))
print(str(False))

#bool()
#모든 자료형
'''
#False
print(bool(0))
print(bool(0.0))
print(bool(""))

#True
print(bool(1))
print(bool(1.0))
print(bool("str"))
print(bool("1234"))
'''