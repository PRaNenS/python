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
    def __init__(self, name, hp): # 클래스 생성시 자동으로 실행되는 부분(인스턴스, 생성자)
        self.name = name # self.name == 멤버변수
        self.hp = hp

class AttackUnit(Unit): # 자식클래스(상속: inheritance)
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
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
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flyingSpeed)

marine1 = AttackUnit("Marine", 40, 5)
marine2 = AttackUnit("Marine", 40, 5)
tank1 = AttackUnit("Tank", 150, 35)
wraith1 = AttackUnit("Wraith", 80, 5)
print("유닛이름: {0}, 공격력: {1}" .format(wraith1.name, wraith1.damage))

wraith2 = AttackUnit("Wraith", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태" .format(wraith2.name))

firebat1 = AttackUnit("Firebat", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)

valkyrie1 = FlyableAttackUnit("Valkyrie", 200, 6, 5)
valkyrie1.fly(valkyrie1.name, "3시")
valkyrie1.attack("2시")
valkyrie1.damaged(10)