# 연습문제 3-2: 최솟값과 최댓값을 튜플로 반환
def min_max(numbers):
    if not numbers:
        raise ValueError("정수를 한 개 이상 입력하세요.")
    return min(numbers), max(numbers)

if __name__ == '__main__':
    try:
        numbers = list(map(int, input("정수들을 입력하세요: ").split()))
        minimum, maximum = min_max(numbers)
        print("min =", minimum)
        print("max =", maximum)
    except ValueError as error:
        print(error)
