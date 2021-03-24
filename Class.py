# marineName = "Marine"
# marineHp = 40
# marineDamage = 5

# print("'{0}'유닛생성" .format(marineName))
# print("체력: {0}, 공격력: {1}\n" .format(marineHp, marineDamage))

# tankName = "Tank"
# tankHp = 150
# tankDamage = 35

# print("'{0}'유닛생성" .format(tankName))
# print("체력: {0}, 공격력: {1}\n" .format(tankHp, tankDamage))

# def attack(name, location, damage):
#     print("{0} : {1}방향으로 공격 [공격력: {2}]" .format(name, location, damage))

# attack(marineName, "1시", marineDamage)
# attack(tankName, "1시", tankDamage)

# 클래스 선언
class Unit: # 부모클래스
    def __init__(self, name, hp, speed): # 클래스 생성시 자동으로 실행되는 부분(인스턴스, 생성자)
        self.name = name # self.name == 멤버변수
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상유닛이동] {0}: {1} 방향으로 이동 [속도: {2}]" .format(self.name, location, self.speed))

class AttackUnit(Unit): # 자식클래스(상속: inheritance)
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location): # 메소드
        print("{0}: {1}방향으로 공격 [공격력: {2}]" .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0}: {1}데미지" .format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 hp = {1}" .format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}: 파괴" .format(self.name))

class Flyable:
    def __init__(self, flyingSpeed):
        self.flyingSpeed = flyingSpeed

    def fly(self, name, location):
        print("{0}: {1}방향으로 날아감 [속도: {2}]" .format(name, location, self.flyingSpeed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flyingSpeed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flyingSpeed)

    def move(self, location):
        print("[공중유닛이동]")
        self.fly(self.name, location) # 오버로딩

# class Unit:
#     def __init__(self):
#         print("Unit 생성자")

# class Flyable:
#     def __init__(self):
#         print("Flyable 생성자")

# class FlyableUnit(Unit, Flyable):
#     def __init__(self):
#         # super().__init__() # 다중상속의 경우 super가 적용되지 않기때문에 일일이 지정할 필요가 있음
#         Unit.__init__(self)
#         Flyable.__init__(self)

marine1 = AttackUnit("Marine", 40, 3, 5)
marine2 = AttackUnit("Marine", 40, 3, 5)
tank1 = AttackUnit("Tank", 150, 4, 35)
wraith1 = AttackUnit("Wraith", 80, 7, 5)
print("유닛이름: {0}, 공격력: {1}" .format(wraith1.name, wraith1.damage))

wraith2 = AttackUnit("Wraith", 80, 7, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태" .format(wraith2.name))

firebat1 = AttackUnit("Firebat", 50, 3, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)

valkyrie1 = FlyableAttackUnit("Valkyrie", 200, 6, 5)
valkyrie1.fly(valkyrie1.name, "3시")
valkyrie1.attack("2시")
valkyrie1.damaged(10)

vulture1 = AttackUnit("Vulture", 80, 10, 20)
battleCruiser1 = FlyableAttackUnit("BattleCruiser", 500, 25, 3)

valkyrie1.move("11시")
battleCruiser1.move("9시")

# Pass 해당 기능을 실행하지않고 넘어감
# Super 부모클래스의 인스턴스를 가져옴
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        super().__init__(name, hp, 0) # Unit클래스의 __init__생성
        pass

supplyDepot1 = BuildingUnit("SupplyDepot", 500, "7시")

def gameStart():
    print("[Alert] 게임 시작")

def gameOver():
    pass

gameStart()
gameOver()

# Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오
# (출력예제)
# 총 3대의 매물이 있습니다
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# [코드]
class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")
houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다" .format(len(houses)))
for house in houses:
    house.show_detail()