# weather = input("오늘 날씨는 어때요?\n>") # 사용자의 입력을 받는 커맨드

# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else: 
#     print("준비물 필요없어요")

temp = int(input("기온: "))
if 30 <= temp:
    print("더움")
elif 10 <= temp and temp < 30:
    print("좋음")
elif 0 <= temp and temp < 10:
    print("쌀쌀함")
else:
    print("추움")