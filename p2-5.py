year = int(input("년도를 입력하세요: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    # 400으로 나누어 떨어지는 해는 윤년
    # 100으로 나누어 떨어지는 해는 평년
    # 4로 나누어 떨어지는 해는 윤년
    print(f"{year}년은 윤년입니다")
else:
    print(f"{year}년은 윤년이 아닙니다")