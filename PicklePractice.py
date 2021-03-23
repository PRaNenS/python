# profile.pickle이란 파일 작성
# profile에 각 바이너리 값을 저장하고 출력
# pickle로 profile정보를 profileFile에 저장후, 파일 닫기
import pickle
profileFile = open("profile.pickle", "wb") # wb에서 b는 바이너리
profile = {"이름": "박명수", "나이": 30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profileFile) # 프로필정보를 파일에 저장
profileFile.close()

# profile.pickle파일을 profileFile이란 이름으로 열고
# profile이란 변수에 profileFile값을 저장
# profile출력 후, 닫기
profileFile = open("profile.pickle", "rb")
profile = pickle.load(profileFile)
print(profile)
profileFile.close()

# with 파일 자동 열고 닫기
# profile.pickle을 profileFile이란 이름으로 열기
# with는 자동으로 연 파일을 닫음
with open("profile.pickle", "rb") as profileFile:
    print(pickle.load(profileFile))

with open("study.txt", "w", encoding="utf8") as studyFile:
    studyFile.write("파이썬 공부")

with open("study.txt", "r", encoding="utf8") as studyFile:
    print(studyFile.read())

# Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다

# - X주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오

# 조건: 파일명은 '1주차.txt', '2주차.txt',... 와 같이 만듭니다

for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as reportFile:
        reportFile.write("- {0}주차 주간보고 -" .format(i))
        reportFile.write("\n부서: ")
        reportFile.write("\n이름: ")
        reportFile.write("\n업무 요약:")