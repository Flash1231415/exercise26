def min_max(numbers):
    # 리스트의 최솟값과 최댓값을 튜플로 반환
    return min(numbers), max(numbers)


# 사용자에게 정수들을 입력받아 리스트로 변환
numbers = list(map(int, input("정수들을 입력하세요: ").split()))

# min_max 함수를 이용해 최솟값과 최댓값 출력
minimum, maximum = min_max(numbers)
print("min =", minimum)
print("max =", maximum)