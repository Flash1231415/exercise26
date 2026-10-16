# 연습문제 2-3: 1부터 100까지 홀수/짝수 판별
for n in range(1, 101):
    if n % 2 == 0:
        print(f"{n}은 짝수입니다")
    else:
        print(f"{n}은 홀수입니다")
