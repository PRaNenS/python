# 표준입출력

# 표준출력
# sep="" => 구별출력 1, 2, 3
# end="" => 끝출력 123,,,
print("Python", "Java", "JavaScript", sep=" vs ", end="?")

import sys
print("Python", "Java", "JavaScript", file=sys.stdout) # 표준출력
print("Python", "Java", "JavaScript", file=sys.stderr) # 표준에러

# 출력형식
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":") # 수학      :   0

# 대기 순번표 (001, 002, 003,...)
for num in range(1, 21):
    print("대기번호: " + str(num).zfill(3)) # 3의 공간확보하여 빈곳을 0으로 채움 => 001

# 표준입력
answer = input("아무 값이나 입력하세요: ")
print("입력값: " + answer)