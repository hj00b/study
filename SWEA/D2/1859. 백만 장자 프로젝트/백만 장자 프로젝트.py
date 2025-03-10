T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    day = list(map(int, input().split()))

    max_profit = 0
    profit = 0
    for i in range(N-1, -1, -1):
        if max_profit < day[i]:
            max_profit = day[i]
        profit += max_profit - day[i]

    print(f"#{tc} {profit}")