text="www.GOOGLE.com"

#len()<<lengh의 약자
print(len(text))

#capitalize << 첫 글자를 대문자로 변경
txt_cap=text.capitalize()
print(txt_cap)

#upper << 문자 전체를 대문자로 변경
#lower << 문자 전체를 소문자로 변경
txt_up=text.upper()
txt_low=text.lower()
print(txt_up)
print(txt_low)

#count << 문자열에 내가 찾고자 하는 문자가 몇번 발생했는지
g_cnt=text.count('G')
print(g_cnt)

#find << g의 인덱스 번호를 반환
g_find=text.find('G')
print(g_find)
g_find=text.find('x') #-1반환
print(g_find)
g_find=text.find('G',5) #5번쨰부터 찾기 시작
print(g_find)

#index << g의 인덱스 번호를 반환
g_ind=text.index('G')
print(g_ind)

#g_ind=text.index('X') 에러 발생(find와의 차이점)
print(g_ind)

#replace << 문자열 치환
txt_rep=text.replace("GOOGLE","NAVER")
print(txt_rep)

#split <<문자열을 ,(콤마)로 분리 시켜줌
txt_spl=text.split('.')
print(txt_spl)

#strip <<맨 앞과 뒤 공백을 지워주는 함수,글자 사이사이으 공백은 지우지 못함
text="          www.GOOGLE.com          "
txt_strip=text.strip()
print(txt_strip)