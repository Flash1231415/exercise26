# 연습문제 2-6: 1부터 100까지 소수만 출력
for n in range(2, 101):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{n}은 소수입니다")
