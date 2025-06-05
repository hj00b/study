T = int(input())

ans = 0

def recursion(cnt, v):
    if cnt == N:
        return 0
    if (cnt, v) in dp:
        return dp[(cnt, v)]

    take = 0
    if v + arr[cnt][0] <= K:
        take = arr[cnt][1] + recursion(cnt + 1, v + arr[cnt][0])
    skip = recursion(cnt + 1, v)

    dp[(cnt, v)] = max(take, skip)
    return dp[(cnt, v)]


for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    
    dp = {}
    print(f"#{tc} {recursion(0, 0)}")
