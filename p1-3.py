# 연습문제 1-3: PDF에 제시된 다섯 수식 계산
import math

a, b, c = 3, 4, 5
print("1 / (1 + a / b + c) =", 1 / (1 + a / b + c))
a, b, c = 1, 1, -6
d = b * b - 4 * a * c
print("두 근 =", (-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a))
r = 5
print("원의 면적 =", math.pi * r * r)
beta, g = 2.0, 3.2
print("beta * exp(-g) =", beta * math.exp(-g))
x, mu, rho = 0, 1.5, 2.0
# PDF의 표기 그대로: 분모 sqrt(2*pi*rho), 양의 지수 (x-mu)^2/(2*rho^2)
value = math.exp((x - mu) ** 2 / (2 * rho ** 2)) / math.sqrt(2 * math.pi * rho)
print("마지막 수식 =", value)
