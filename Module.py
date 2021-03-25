import theater_module as mv # theater_module를 mv란 변수명으로 정의
mv.price(3) # 3명 일반가격
mv.price_morning(4) # 4명 조조할인
mv.price_soldier(5) # 5명 군인할인

from theater_module import *
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price, price_morning
price(5)
price_morning(6)
# price_soldier를 import하지 않았기때문에 사용 불가

from theater_module import price_soldier as ps # theater_module의 price_soldier를 ps라 정의
ps(5)