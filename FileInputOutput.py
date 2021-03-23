scoreFile = open("score.txt", "w", encoding="utf8") # 파일이름="score.txt", "w"=쓰기
print("수학 : 0", file=scoreFile)
print("영어 : 50", file=scoreFile)
scoreFile.close()

scoreFile = open("score.txt", "a", encoding="utf8") # "a"=append(추가)
scoreFile.write("과학 : 80")
scoreFile.write("\n코딩 : 100")
scoreFile.close()

scoreFile = open("score.txt", "r", encoding="utf8") # "r"=읽기
print(scoreFile.read())
scoreFile.close()

scoreFile = open("score.txt", "r", encoding="utf8")
print(scoreFile.readline(), end="") # 한줄씩 읽기
print(scoreFile.readline(), end="")
print(scoreFile.readline(), end="")
print(scoreFile.readline())
scoreFile.close()

# 가져올 파일이 몇줄인지 모를때
scoreFile = open("score.txt", "r", encoding="utf8")
while True:
    line = scoreFile.readline()
    if not line:
        break
    print(line, end="")
scoreFile.close()

scoreFile = open("score.txt", "r", encoding="utf8")
lines = scoreFile.readlines()
for line in lines:
    print(line, end="")
scoreFile.close()