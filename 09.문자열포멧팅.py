#포멧팅

weather="맑음"
temporature=20
chance_shower=33.5

print("오늘의 날씨는",weather,"기온은",temporature,"도 입니다")

print("오늘의 날씨는 %s 기온은 %d도 비가 내릴 확률은 %f%% 입니다"%(weather, temporature,chance_shower))
print("오늘의 날씨는 %s 기온은 %d도 비가 내릴 확률은 %.1f%% 입니다"%(weather, temporature,chance_shower))


print("오늘의 날씨는 {} 기온은 {}도 비가 내릴 확률은 {}%입니다".format(weather,temporature,chance_shower))
print("오늘의 날씨는 {0} 기온은 {2}도 비가 내릴 확률은 {1}%입니다".format(weather,temporature,chance_shower))
print("오늘의 날씨는 {2} 기온은 {1}도 비가 내릴 확률은 {0}%입니다".format(weather,temporature,chance_shower))
print("오늘의 날씨는 {1:f} 기온은 {1:o}도 비가 내릴 확률은 {1:x}%입니다".format(weather,temporature,chance_shower))

'''
o << 8진수
x << 16진수
'''

#f-string
print(f"오늘의 날씨는 {weather}이며, 기온은 {temporature} 비가내릴 확률은 {chance_shower}입니다")