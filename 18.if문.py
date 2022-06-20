if True:
    print("실행할 문장입니다")

weather = "비"

if weather == "비":
    print("우산을 챙겨주세요.")

study_time = int(input("오늘의 공부시간을 입력해주세요 >"))

#만약에 오늘 공부할 시간이 3시간 이상이라면 파이썬 공부를 한다

# if 6>= study_time <=3: <<정상적으로 출력 
if study_time >= 3 and 6 >= study_time:
    print("오늘은 파이썬 공부를 합시다!")

#만약에 오늘 공부할 시간이 3시간 미만이라면 놀자
if study_time < 3:
    print("오늘은 시간이 별로 없으니까 운동이나 하자!")

odd = int(input("정수를 입력해주세요 >"))

# if odd[-1] == "1" or odd[-1] == "3" or odd[-1] == 5 or odd[-1] == 7 or odd[-1] == 9:
if odd % 2 == 1:
    print("입력하신 정수는 홀수 입니다.")
else:
    print("입력하신 정수는 짝수 입니다.")

number = input("주민번호를 입력해 주세요 >")
odd = int(number[7])

if odd %2 == 0:
    print("여성입니다")
else:
    print("남성입니다")

lunch = input("점심메뉴를 골라주세요(제육덮밥,돈까스,김밥) >")

if lunch=="제육덮밥":
    print("제육덮밥을 먹는다")
elif lunch=="돈까스":
    print("돈까스를 먹는다")
elif lunch=="김밥":
    print("김밥을 먹는다")
else:
    print("굶는다")


number = int(input("정수를 입력해주세요"))
if number % 3 == 0 and number % 2 == 0:
    print("3의 배수이면서 짝수 입니다.")
elif number % 3==0:
    print("3의 배수 입니다.")
elif number % 3!=0:
    print("3의 배수가 아닙니다.")
elif number % 2 ==0:
    print("짝수 입니다.")
elif number % 2 !=0:
    print("짝수가 아닙니다.")
else:
    print("3의 배수 이면서 짝수가 아닙니다")