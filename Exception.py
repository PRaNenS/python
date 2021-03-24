try:
    print("나누기 전용 계산기")
    nums = []
    nums.append(int(input("첫번째 숫자 >")))
    nums.append(int(input("두번째 숫자 >")))
    nums.append(int(nums[0]/nums[1]))
    print("{0} / {1} = {2}" .format(nums[0], nums[1], nums[2]))
except ValueError: # 값 에러(나누기 처리에 숫자가 아닌 글자 입력 시)
    print("에러발생")
except ZeroDivisionError as err: # 0을 나누려고 할 시
    print(err)
except Exception as err:
    print("알 수 없는 에러 발생")
    print(err)