# 숫자, 알파벳, 한글

numbers=[1,50,100,75,1000, 200,5000]

#sort << 오름차순 정렬
numbers.sort()
print(numbers)

#reverse << 리스트를 반대로 출력(내림차순 X)
numbers.reverse()
print(numbers)

#sort(reverse=True) << 내림차순 정렬
numbers.sort(reverse = True)
print(numbers)

names=["홍길동","김개똥","이승철"]
names.sort(reverse=True)
print(names)

# in연산자와 not in 연산자
print(50 in numbers)
print("c" in numbers)
print("Jave script" in numbers)
print("Jave script" not in numbers)