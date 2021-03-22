# 기본값
def profile(name, age=17, mainLang="파이썬"):
    print("이름: {0}\t나이: {1}\t사용언어: {2}"\
        .format(name, age, mainLang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 같은 학교, 같은 학년, 같은 반
profile("정형돈")

# 키워드값
def profileKeyword(name, age, mainLang):
    print(name, age, mainLang)

profileKeyword(name="유재석", mainLang="파이썬", age=20)

# Variable Factor 가변인자
def profileVariable(name, age, *language):
    print("이름: {0}\t나이: {1}\t" .format(name, age), end="")
    for lang in language:
        print(lang, end=" ")
    print()

profileVariable("유재석", 20, "파이썬", "Java", "C", "C++", "C#", "JavaScript")
profileVariable("김태호", 25, "코틀린", "스위프트")