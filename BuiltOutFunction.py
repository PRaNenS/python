# list of python modules 검색을 통해 외장함수 리스트를 확인할 수 있다

# glob: 경로내의 폴더/파일 목록 조회
import glob
print(glob.glob("*.py")) # 확장자가 py인 모든파일

# os: 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현재 디렉토리 표시

folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더")
    os.rmdir(folder)
    print(folder, "폴더를 삭제")
else:
    os.makedirs(folder) # 폴더생성
    print(folder, "폴더를 생성")

print(os.listdir())

# time: 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

# date: 날짜 관련 함수
import datetime
print("오늘 날짜는 ", datetime.date.today())

# timedelta: 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜
td = datetime.timedelta(days=100) # 100일 후
print("우리가 만난지 100일은 ", today + td) # 오늘로부터 100일 후

# Quiz) 프로젝트내에 나만의 시그니처를 남기는 모듈을 만드시오
# 조건: 모듈 파일명은 byme.py로 작성

# (모듈 사용 예제)
import byme
byme.sign()

# (출력예제)
# 이 프로그램은 kjs에 의해 만들어졌습니다
# 유튜브: http://youtube.com
# 이메일: kjs@gmail.com