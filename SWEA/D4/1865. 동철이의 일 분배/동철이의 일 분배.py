def recur(row, total):
    global max_total
    if row == N:
        max_total = max(max_total, total)
        return

    if max_total > total:
        return

    for col in range(N):
        if not visited[col] and arr[row][col] != 0 :
            visited[col] = 1
            recur(row+1, total * arr[row][col])
            visited[col] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(lambda x:int(x)/100, input().split())) for _ in range(N)]
    # arr.sort(key=lambda x:sum(x), reverse=True)

    max_total = 0

    visited = [0] * (N + 1)
    recur(0, 1)
    print(f"#{tc} {max_total*100:6f}")