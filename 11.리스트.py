#리스트

list_a=[1,2,3,4]
list_b=["a","b","c","d"]
list_c=[True,False]
list_d=[1,"a",True]
print(list_a)
print(list_b)
print(list_c)
print(list_d)

numbers=[0,1,2,3,4,5,6,7]
print(numbers[0]) # 인덱싱
print(numbers[3:5]) # 슬라이싱

list_lan=["java","c","python","go"]
print(list_lan[0][0])
list_lan[1]="c++"
print(list_lan)
list_lan[1:3]=["c#","python3"]
print(list_lan)

print(len(list_lan))

# append() << 리스트 맨 뒤에 제일 마지막 인덱스 생성
list_lan.append("ruby")
print(list_lan)

list_a=[1,2,3]
list_lan.append(list_a) # 리스트를 삽입
print(list_a)

#extend() << 리스트의 요소들을 생성
list_lan.extend(list_a) # 리스트의 요소들을 삽입
print(list_lan)

#insert(index,값)
list_lan.insert(0,"r")
print(list_lan)

#pop() << 마지막 인덱스 삭제 후 반환
print(list_lan.pop())

#remove() << 인덱스를 지정해서 삭제
list_lan.remove("python3")
print(list_lan)

#del << 인덱스 번호를 지정해서 삭제
del list_lan[1]
print(list_lan)

