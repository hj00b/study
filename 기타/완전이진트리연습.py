def in_order(n):
    global i
    if n <= N:
        in_order(n*2)
        arr[n] = i
        i += 1
        in_order(n*2+1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [0] * (N+1)
    i = 1
    in_order(1)
    print(f"#{tc} {arr[1]} {arr[N//2]}")
