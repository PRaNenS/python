# 전역변수와 지역변수
gun = 10 # 전역변수

def checkPoint(soldiers):
    global gun # 전역변수
    # gun = 20 # 지역변수
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}" .format(gun))

def checkPointReturn(gun, soldiers):
    gun -= soldiers
    print("[함수 내] 남은 총: {0}" .format(gun))
    return gun

print("전체 총: {0}" .format(gun))
checkPoint(2) # 2명
gun = checkPointReturn(gun, 2)
print("남은 총: {0}" .format(gun))

# Quiz) 표준 체중을 구하는 프로그램을 작성하시오
# * 표준체중: 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자: 키(m) * 키(m) * 22
# 남자: 키(m) * 키(m) * 21

# 조건1: 표준 체중을 별도의 함수 내에서 계산
#         * 함수명: stdWeight
#         * 전달값: 키(height), 성별(gender)
# 조건2: 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg입니다
def stdWeight(height, gender): # 키(m단위)
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175 # cm단위
gender = "남자"
weight = round(stdWeight(height/100, gender), 2)
print("키 {0}cm ({1}) 표준 체중: {2}kg" .format(height, gender, weight))