# input: 사용자 입력을 받는 함수
language = input("무슨 언어를 좋아하세요?> ")
print("{0}는 좋은 언어입니다" .format(language))

# dir: 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
import random # 외장 함수(외부에서 따로 import)
print(dir()) # 내장함수(따로 import하지 않고도 사용가능)

lst = [1,2,3]
print(dir(lst))

name = "Jim"
print(dir(name))