T = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, T + 1):
    n = int(input())
    arr = [[0] * n for i in range(n)]
    nr = 0
    nc = 0
    num = 1
    d = 0
    while True:
        if num > n ** 2:
            break
        if 0 <= nr < n and 0 <= nc < n and not arr[nr][nc]:
            arr[nr][nc] = num
            num += 1

        else:
            nr = nr - dr[d]
            nc = nc - dc[d]
            d = (d + 1) % 4
        nr = nr + dr[d]
        nc = nc + dc[d]

    print(f"#{tc}")
    for row in arr:
        print(*row)
