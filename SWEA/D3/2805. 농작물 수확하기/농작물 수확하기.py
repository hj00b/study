T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    k = 1
    cost = 0
    for i in range(N):
        if i < N//2 + 1:
            for j in range(N//2-i, N//2+i+1):
                cost += arr[i][j]
        elif i == N-1:
            cost += arr[i][N//2]
        else:
            for j in range(k, N - k ):
                cost += arr[i][j]
            k = k + 1
    print(f'#{tc} {cost}')