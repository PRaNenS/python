try:
    print("한자리 숫자 나누기")
    num1 = int(input("숫자1 >"))
    num2 = int(input("숫자2 >"))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print("{0} / {1} = {2}" .format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값 입력! 한 자리만 입력")