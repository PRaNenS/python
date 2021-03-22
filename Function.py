def openAccount():
    print("새로운 계좌 생성")

openAccount()

def deposit(balance, money): # 입금
    print("입금완료 (잔액: {0}원)" .format(balance + money))
    return balance + money

def withDraw(balance, money): # 출금
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금완료 (잔액: {0}원)" .format(balance - money))
        return balance - money
    else:
        print("출금불가 (잔액: {0}원)" .format(balance))

def withDrawNight(balance, money): # 저녁출금
    commission = 100 # 수수료
    print("출금완료 (잔액: {0}원, 수수료{1}원)" .format(balance - money - commission, commission))
    return commission, balance - money - commission

balance = 0 # 잔액
balance = deposit(balance, 1000)
balance = withDraw(balance, 500)
balance = deposit(balance, 2000)
balance = withDraw(balance, 1000)
commission, balance = withDrawNight(balance, 500)