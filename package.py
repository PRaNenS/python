import travel.thailand # travel패키지의 thailand삽입
trip_to = travel.thailand.ThailandPackage() # trip_to를 ThailandPackage클래스로 정의
trip_to.detail()

from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from travel import * # travel패키지의 __init__파일의 공개여부를 통해 import
trip_to = vietnam.VietnamPackage()
trip_to.detail()
# trip_th = thailand.ThailandPackage
# trip_th.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(vietnam))