# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

# 문자열 내에 ""과 ''은 그대로 나옴
print("저는 '나도코딩'입니다")

# 문자열내 특수문자는 \를 통해 Escape처리가 이루어짐
print("저는 \"나도코딩\"입니다")

# \\ : \
print("C:\\user") # C:\user

# \r : 커서를 맨앞으로
print("Red Apple\rPine") # Red Apple > 커서 앞으로 > PineApple

# \b : 백스페이스(한글자 삭제)
print("Redd\bApple") # RedApple

# \t : 탭
print("Red\tApple") # Red   Apple

# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# ex) http://naver.com
# 규칙1 : http:// 부분은 제외
# 규칙2 : 처음 만나는 점(.)이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
url = "http://naver.com"
myStr = url.replace("http://", "") # 규칙1
print(myStr)
myStr = myStr[:myStr.index(".")] # myStr의 문자열에서 처음부터 .의 자리직전까지(== myStr[0:5])
print(myStr)
password = myStr[:3] + str(len(myStr)) + str(myStr.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다" .format(url, password))