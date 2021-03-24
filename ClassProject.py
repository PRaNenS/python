# 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("'{0}'유닛 생성" .format(name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0}: '{1}'방향 이동 [속도: {2}]" .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0}: {1}데미지" .format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재체력 {1}" .format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}: 파괴" .format(self.name))

# 공격유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0}: '{1}'방향 공격 [공격력: {2}]" .format(self.name, location, self.damage))

class Flyable(Unit):
    def __init__(self, flyingSpeed):
        self.flyingSpeed = flyingSpeed

    def fly(self, name, location):
        print("{0}: '{1}'방향 공중이동 [속도: {2}]" .format(name, location, self.flyingSpeed))

# 공격공중유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flyingSpeed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flyingSpeed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# Marine유닛
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "Marine", 40, 1, 5)

    # StimPack
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0}: 스팀팩 사용 (-HP 10)" .format(self.name))
        else:
            print("{0}: 체력이 부족하여 스팀팩 사용 불가" .format(self.name))

# 탱크
class Tank(AttackUnit):
    seize_developed = False
    
    def __init__(self):
        AttackUnit.__init__(self, "Tank", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        if self.set_seize_mode == False:
            print("{0}: 시즈모드" .format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{0}: 시즈모드" .format(self.name))
            self.damage /= 2
            self.seize_mode = False

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "Wraith", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print("{0}: 클로킹 해제" .format(self.name))
            self.clocked = False
        else:
            print("{0}: 클로킹" .format(self.name))
            self.clocked = True

def gameStart():
    print("[Alert] 새 게임 시작")

def gameOver():
    print("Player: gg")
    print("[Player]님이 퇴장하였습니다")

# 실제 게임 진행
gameStart()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

# 유닛 일괄 관리
attackUnits = []
attackUnits.append(m1)
attackUnits.append(m2)
attackUnits.append(m3)
attackUnits.append(t1)
attackUnits.append(t2)
attackUnits.append(w1)

# 전군 이동
for unit in attackUnits:
    unit.move("1시")

# 시즈 모드 연구 완료
Tank.seize_developed = True
print("[Alert] 탱크 시즈 모드 연구 완료")

# 전군 공격 준비
for unit in attackUnits:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attackUnits:
    unit.attack("1시")

# 전군 피해
from random import *
for unit in attackUnits:
    unit.damaged(randint(5, 21))

# 게임오버
gameOver()