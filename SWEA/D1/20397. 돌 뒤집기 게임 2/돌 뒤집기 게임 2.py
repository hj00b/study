T = int(input())
for tc in range(1, T + 1):
    lst_len, game_case = map(int, input().split())
    lst = list(map(int, input().split()))
    def turn_stone(center, range_num):
        global lst
        n1 = center + range_num
        n2 = center - range_num
        if 0<=n1<lst_len and 0<=n2<lst_len and lst[n1] == lst[n2]:
            lst[n1] = (lst[n1]+1)%2
            lst[n2] = (lst[n2]+1)%2

    for _ in range(game_case):
        i, j = map(int, input().split())
        i = i -1
        for n in range(1, j+1):
            turn_stone(i, n)


    print(f"#{tc}", end=" ")
    print(*lst)