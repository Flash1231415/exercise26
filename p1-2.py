# 연습문제 1-2: 변수 스코프와 실행 결과
x = 10

def test_local():
    x = 20
    print(x)

def test_global_read():
    print(x)

def outer():
    x = 20
    def inner():
        x = 30
        print("A:", x)
    inner()
    print("B:", x)

def test_error():
    # 함수 안에 x 대입이 있으므로 x는 지역 변수로 판단된다.
    # 값이 대입되기 전에 읽으면 UnboundLocalError가 발생한다.
    print(x)
    x = 20

def test_fixed():
    global x
    print(x)
    x = 20

if __name__ == '__main__':
    print("[1: 20, 10]")
    test_local()
    print(x)
    print("[2: 10, 10]")
    test_global_read()
    print(x)
    print("[3: A: 30, B: 20, C: 10]")
    outer()
    print("C:", x)
    print("[4: 오류 이유]")
    try:
        test_error()
    except UnboundLocalError:
        print("지역 변수 x에 값을 대입하기 전에 읽어서 오류가 발생합니다.")
    print("[4 수정: 10, 20]")
    test_fixed()
    print(x)
