# pypi검색하여 원하는 pip(api)를 설치할 것
# 커맨드콘솔에 pip install ~~ 커맨드 복사 붙여넣어 실행할 것
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# 기존에 설치된 pip를 'pip install --upgrade ~~'를 통해 최신버전으로 업그레이드 가능
# 설치된 pip를 삭제하기위해 'pip uninstall ~~'를 실행