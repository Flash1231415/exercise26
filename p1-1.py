# 연습문제 1-1: input() 한 번/두 번, f-string/format() 방식
def print_results(a, b, use_fstring):
    if use_fstring:
        print(f"{a} + {b} = {a + b}")
        print(f"{a} - {b} = {a - b}")
        print(f"{a} x {b} = {a * b}")
        if b != 0:
            print(f"{a} / {b} = {a / b}")
        else:
            print(f"{a} / {b} = 0으로 나눌 수 없습니다")
    else:
        print("{} + {} = {}".format(a, b, a + b))
        print("{} - {} = {}".format(a, b, a - b))
        print("{} x {} = {}".format(a, b, a * b))
        if b != 0:
            print("{} / {} = {}".format(a, b, a / b))
        else:
            print("{} / {} = 0으로 나눌 수 없습니다".format(a, b))

if __name__ == '__main__':
    a, b = map(int, input("두 정수를 공백으로 구분하여 입력하세요: ").split())
    print("[input 한 번 / f-string]")
    print_results(a, b, True)
    print("[input 한 번 / format]")
    print_results(a, b, False)
    a = int(input("첫 번째 정수: "))
    b = int(input("두 번째 정수: "))
    print("[input 두 번 / f-string]")
    print_results(a, b, True)
    print("[input 두 번 / format]")
    print_results(a, b, False)
