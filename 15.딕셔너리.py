people = {
    "name":"김개똥",
    "phone":"010-1111-2222"
}

print(people["name"],people["phone"])

books={"daniel pink":["파는 것이 인간이다.","언제 할 것인가"],
"eric schidt":"새로운 디지털 시대"}

print(books["daniel pink"])

coffee={"java":2500,"americano":2500,"latte":3000}
coffee["java"]=3000
coffee["moca"]=3000

print(coffee["java"])# << 바뀐 값 출력
print(coffee) # << 전체 커피 값 출력

del coffee["java"]
print(coffee)
print(coffee.keys()) 
print(coffee.values())