T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    line = []
    cnt = 0
    for i in range(N):
        s, e = map(int, input().split())
        line.append((s, e))

    for i in range(N):
        for j in range(i + 1, N):
            l1, r1 = line[i]
            l2, r2 = line[j]

            if (l1 < l2 and r2 < r1) or (l1 > l2 and r1 < r2):
                cnt += 1

    print(f'#{tc} {cnt}')