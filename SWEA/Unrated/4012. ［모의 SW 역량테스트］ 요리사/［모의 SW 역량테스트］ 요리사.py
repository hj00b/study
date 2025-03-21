def comb(idx, cnt, group):
    if cnt == N//2 - 1:
        cook(group)
        return

    if cnt + (N-idx) < N//2 -1:
        return

    if idx == N:
        return

    comb(idx+1, cnt+1, group + [idx])
    comb(idx+1, cnt, group)


def cook(group):
    global min_diff
    t1 = 0
    t2 = 0
    for i in range(N-1):
        if i in group:
            for j in range(i+1, N):
                if j in group:
                    t1 += taste[i][j] + taste[j][i]
        else:
            for j in range(i+1, N):
                if j not in group:
                    t2 += taste[i][j] + taste[j][i]
    diff = abs(t1-t2)
    if min_diff > diff:
        min_diff = diff


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    taste = [list(map(int, input().split())) for _ in range(N)]
    min_diff = int(21e8)
    comb(1, 0, [0])
    print(f"#{tc} {min_diff}")