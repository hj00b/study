N = int(input())
arr = [[0] * 100 for _ in range(100)]
for _ in range(N):
    sr, sc = map(int, input().split())
    
    for r in range(sr, sr + 10):
        for c in range(sc, sc + 10):
            arr[r][c] = 1

ans = sum(list(map(sum, arr)))
print(ans)