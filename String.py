# 문자처리
sentence  = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """나는 소년이고,
파이썬은 쉬워요"""
print(sentence3)

jumin = "123456-1234567"
print("성별: " + jumin[7])
print("년: " + jumin[0:2]) # 0~2직전의 값(0,1)
print("월: " + jumin[2:4]) # 2~4직전의 값(2,3)
print("일: " + jumin[4:6]) # 4~6직전의 값(4,5)
print("생년월일: " + jumin[:6]) # 생년월일
print("뒤 7자리: " + jumin[7:]) # 뒤자리 
print("뒤 7자리(뒤에서): " + jumin[-7:]) # 뒤에서 세서 7번째 값부터(-14 ~ -1)

# 문자열 처리
python = "Python is Amazing"
print(python.lower) # 소문자
print(python.upper) # 대문자
print(python[0].isupper) # 대문자인지?
print(len(python)) # 문자길이
print(python.replace("Python", "Java")) # 문자변환
index = python.index("n")
print(index) # 문자위치
index = python.index("n", index + 1)
print(index)
print(python.find("Java")) # 값이 없음 -1
# print(python.index("Java")) # 해당글자 찾기(없으므로 에러)
print("hi")
print(python.count("n")) # 몇번 나오는지

#방법1
print("나는 %d살입니다" %20) # 정수
print("나는 %s을 좋아해요" %"파이썬") # 문자
print("Apple은 %c로 시작해요" %"A") # 글자
print("나는 %s과 %s을 좋아해요" %("파랑", "빨강"))

# 방법2
print("나는 {}살입니다" .format(20))
print("나는 {}색과 {}색을 좋아해요" .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요" .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요" .format("파란", "빨간"))

# 방법3
print("나는 {age}살이며 {color}색을 좋아해요" .format(age = 20, color = "빨간"))
print("나는 {age}살이며 {color}색을 좋아해요" .format(color = "빨간", age = 20))

# 방법4 (v3.6 이상)
age = 20
color = "빨간"
print(f"나는 {age}살이며 {color}색을 좋아해요")