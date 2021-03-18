#숫자
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

#문자열
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)

#참/거짓
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))

#애완동물
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

# 주석
# 설정

print("우리집 " + animal + "의 이름은 " + name + "예요")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요?" + str(is_adult))

# Quiz
# 변수명 : station
# 변수값 : "사당", "신도림", "인천공항"
# 출력문장 : "XX행 열차가 들어오고 있습니다"

station = "인천공항"
print(station+ "행 열차가 들어오고 있습니다")

# 연산자
print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2
print(2**3) # 2^3 = 8
print(5%3) # 나머지구하기 2
print(5//3) # 몫구하기 1
print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True
print(3 == 3) # True
print(4 == 2) # False
print(3 + 4 == 7) # True
print(1 != 3) # True
print(not(1 != 3)) # False
print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True
print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5))
print(5 > 4 > 3) # True
print(5 > 4 > 7) # False
print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20
number = 2 + 3 * 4 # 14
print(number)
number += 2 # 16
print(number)
number -= 2 # 14
print(number)
number *= 2 # 28
print(number)
number /= 2 # 14
print(number)
number %= 2 # 0
print(number)
print(abs(-5)) # 절대값 5
print(pow(4, 2)) # 4^2 = 4*4 = 16
print(max(5, 12)) # 12
print(min(5, 12)) # 5
print(round(3.14)) # 3
print(round(4.99)) # 5

from math import * # math라이브러리의 모든걸 임포트
print(floor(4.99)) # 내림 4
print(ceil(3.14)) # 올림 4
print(sqrt(16)) # 제곱근 4

from random import *
print(int(random() * 45) + 1) # 1 ~ 45 미만의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 45 미만의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성

# Quiz 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오

# 조건1: 랜덤으로 날짜를 뽑아야 함
# 조건2: 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건3: 매월 1~3일은 스터디 준비를 해야 하므로 제외

# 출력문: 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다

print("오프라인 스터디 모임 날짜는 매월 " + str(randint(4, 28)) + "일로 선정되었습니다")

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