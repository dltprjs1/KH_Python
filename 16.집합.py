# add 123, "문자","True",("튜플")은 추가 가능
# [1,2,3],{key:value}은 추가 불가
week = {"월요일","화요일","수요일","목요일","금요일","토요일","일요일","월요일"} # 집합은 순서가 정해져 잇지 않음
week.add("화요일") # 중복된 값 출력 X
print(week)

a={0,"abs",1}
a.add(True) # 1=True와 같이 사용불가, 0=False와 같이 사용 불가
a.add(("일주일",))
a.update(["일주일"],{"한달":123})
print(a)

week=set(["월요일","화요일","수요일","목요일","금요일","토요일","일요일"])

print(week)


a = {1,2,3,4,5}
b = {3,4,5,6,7}

#합집합
print(a|b)

#교집합
print(a&b)

#차집합
print(a-b)

#원소삭제
a.remove(4)
print(a)