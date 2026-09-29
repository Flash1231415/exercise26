
# 여러 개의 숫자와 연산 기호를 받아 계산하는 함수
def calc(*numbers, op):
    # 숫자가 없거나 +, * 이외의 연산 기호이면 오류 발생
    if not numbers or op not in ("+", "*"):
        raise ValueError("정수와 연산 부호(+, *)를 입력하세요.")

    # 덧셈은 0부터, 곱셈은 1부터 시작
    result = 0 if op == "+" else 1

    # 입력된 숫자를 하나씩 계산
    for number in numbers:
        result = result + number if op == "+" else result * number

    # 계산 결과 반환
    return result


# 1 + 1 + 4의 결과 출력
print(calc(1, 1, 4, op="+"))

# 1 * 2의 결과 출력
print(calc(1, 2, op="*"))
