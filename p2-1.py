# 연습문제 2-1: 같은 크기의 리스트 내적
a = [1, 0, 1]
b = [1, 1, 2]
result = sum(x * y for x, y in zip(a, b))
print(f"{a}* {b} = {result}")
