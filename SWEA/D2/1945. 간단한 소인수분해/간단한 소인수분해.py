# 간단한 소인수분해
# 0209
#import sys
#sys.stdin = open('input (3).txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 반복되는 작업을 함수로 정의
    # 소수의 몇 승인지 각각 계산 후 함수로 반환
    def prime_factorization(num, prime):
        count = 0
        while num % prime == 0:
            num = num // prime
            count += 1
        return count

    a = prime_factorization(N, 2)
    b = prime_factorization(N, 3)
    c = prime_factorization(N, 5)
    d = prime_factorization(N, 7)
    e = prime_factorization(N, 11)


    print(f'#{tc} {a} {b} {c} {d} {e}')
