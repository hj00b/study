N = int(input())
ans = 0

for diff in range(0, 10*len((str(N)))):
    # diff = 각 자리 수의 합
    # diff는 자리수 * 10 보다 큰 수 일 수 없음
    num = N - diff
    if num < 0:  # num이 음수가 되면 검사할 필요 없음
        break
    sum_each_digit = 0 # 자리 수 합을 저장할 변수
    for _ in range(len(str(num))):
        sum_each_digit += num % 10
        num //= 10
    if diff == sum_each_digit:
        ans = N - diff

print(ans)