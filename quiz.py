odd = input("웹사이트 주소를 입력해주세요 >")

odd1 = odd.split(".")

if odd1[-1] == "kr":
    print("한국사이트 입니다.")
elif odd1[-1] == "uk":
    print("영국사이트 입니다.")
elif odd1[-1] == "org":
    print("기관 사이트 입니다.")
elif odd1[-1] == "com":
    print("기업용 사이트 입니다.")
else:
    print("알수없는 사이트 입니다")

print(odd)