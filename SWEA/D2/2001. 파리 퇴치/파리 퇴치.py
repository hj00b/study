T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for r in range(n - m + 1):
        for c in range(n - m + 1):
            total = 0
            for k in range(m):
                for p in range(m):
                    total += arr[r + k][c + p]
            ans = max(ans, total)

    print(f"#{tc} {ans}")


