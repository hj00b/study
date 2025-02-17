N = int(input())
def dp(i):
    global memo
    if i >= 2:
        memo[i] = memo[i-2] - memo[i-1]
    if memo[i] < 0:
        memo[i] = 0
        return
    return memo[i]


memo = [0] * 30000
memo[0] = N

max_cnt = 0
max_num = 0
for i in range(1, 30000):
    memo[1] = i
    cnt = 2
    for j in range(2, 30000):
        ans = dp(j)
        if ans is None:
            break
        cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt
        max_num = i
print(max_cnt)
memo[1] = max_num
for j in range(2, 30000):
    ans = dp(j)
    if ans is None:
        break
print(*memo[:max_cnt])

