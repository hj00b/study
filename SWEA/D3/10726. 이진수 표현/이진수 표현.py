T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    for i in range(N):
        if not M & (1 << i):
            print(f"#{tc} OFF")
            break
    else:
        print(f"#{tc} ON")
