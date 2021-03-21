# Java의 HashMap과 비슷
cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
# print(cabinet[5]) = 잘못된 키값으로 불려오려고 할경우 에러와 함께 프로그램이 종료
print(cabinet.get(5)) # 잘못된 키값으로 불려오려고 할경우 None으로 표시
print(cabinet.get(5, "사용 가능")) # 해당 키의 값을 가져오되, 없을 경우 지정된 값을 가져옴

print(3 in cabinet) # True => cabinet에 3이라는 키값이 있는지
print(5 in cabinet) # False => cabinet에 5라는 키값이 있는지

cabinet = {"A-3": "유재석", "B-100": "김태호"}

# 값 새로 설정 및 추가
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 해당 키값 삭제
del cabinet["A-3"]
print(cabinet)

# 키만 출력
print(cabinet.keys())

# 값만 출력
print(cabinet.values())

# 키, 값 모두 출력
print(cabinet.items())

# 모두 삭제
cabinet.clear()
print(cabinet)