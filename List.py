# 리스트[]
subway = [10, 20, 30]
print(subway)

subway = ["재석", "세호", "명수"]
print(subway)

# 세호가 몇번째칸에 타고 있는지?
print(subway.index("세호"))

# 다음 정류장에서 하하가 추가?
subway.append("하하")
print(subway)

# 형돈이가 재석과 세호 사이에 추가
subway.insert(1, "형돈")
print(subway)

# 지하철에 있는 사람을 뒤에서 한명씩 꺼냄
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇명?
subway.append("재석")
print(subway)
print(subway.count("재석"))

# 정렬
numList = [5, 4, 3, 2, 1]
numList.sort()
print(numList)

# 순서 뒤집기
numList.reverse()
print(numList)

# 모두 지우기
numList.clear()
print(numList)

# 다양한 자료형 함께 사용
mixList = ["조세호", 20, True]
numList = [5, 4, 3, 2, 1]
numList.extend(mixList)
print(numList)