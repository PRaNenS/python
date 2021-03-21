# Set(집합)
# 중복 안됨, 순서 없음
mySet = {1, 2, 3, 3, 3}
print(mySet)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (자바와 파이썬을 모두 할 수 있는 사람)
print(java & python)
print(java.intersection(python))

# 합집합 (자바나 파이썬을 할 수 있는 사람)
print(java | python)
print(java.union(python))

# 차집합 (자바는 할 수 있지만 파이썬을 할 줄 모르는 사람)
print(java - python)
print(java.difference(python))

# 추가
python.add("김태호")
print(python)

# 삭제
java.remove("김태호")
print(java)