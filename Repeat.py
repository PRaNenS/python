# for 대기번호 1~5
for waitingNo in range(1, 6): # 1 2 3 4 5
    print("대기번호: {0}" .format(waitingNo))

starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다" .format(customer))

# while
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비되었습니다 {1}번 남았습니다" .format(customer, index))
    index -= 1

    if index == 0:
        print("커피 폐기처분")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다 {1}번 남았습니다" .format(customer, index))
#     index += 1
# 무한루프시 ctrl + c 로 탈출

# customer = "토르"
# person = "Unknown"

# while person != customer:
#     print("{0}, 커피 준비" .format(customer))
#     person = input("이름 >")

# continue & break
absent = [2, 5] #결석
noBook = [7]

for student in range(1, 11): # 1 2 3 4 5 6 7 8 9 10
    if student in absent:
        continue # 다음 반복 진행
    elif student in noBook:
        print("{0}는 교무실로" .format(student))
        break # 반복 종료

    print("{0}, 출석" .format(student))

# 출석번호가 1, 2, 3,... 앞에 100을 붙이기로 함 => 101, 102, 103,...
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생이름을 길이로 변환
students = ["Iron Man", "Thor", "Groot"]
students = [len(i) for i in students]
print(students)

# 학생이름을 대문자로 변환
students = ["Iron Man", "Thor", "Groot"]
students = [i.upper() for i in students]
print(students)

# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사입니다
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오

# 조건1: 승객별 운행 소요 시간은 5분~50분 사이의 난수로 정해집니다
# 조건2: 당신은 소요 시간 5분~15분 사이의 승객만 매칭해야 합니다

# (출력문 예제)
# [O] 1번째 손님 (소요시간: 15분)
# [ ] 2번째 손님 (소요시간: 50분)
# [O] 3번째 손님 (소요시간: 5분)
# ...
# [ ] 50번째 손님 (소요시간: 16분)

# 총 탑승 승객: 2명
from random import *
cnt = 0 # 총 탑승 승객 수
for i in range(1, 51): # 1~50
    time = randrange(5, 51) # 5~50분 소요시간
    if 5 <= time <= 15: # 매칭 성공
        print("[O] {0}번째 손님 (소요시간: {1}분)" .format(i, time))
        cnt += 1
    else: # 매칭 실패
        print("[ ] {0}번째 손님 (소요시간: {1}분)" .format(i, time))
print("총 탑승 승객: {0}" .format(cnt))