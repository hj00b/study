T = int(input())
for tc in range(1, T+1):
    num = int(input())
    total = 0
    v = 0
    for n in range(num):
        command = list(map(int, input().split()))

        if len(command) != 1:
            if command[0] == 1:
                v += command[1]
            else:
                if v >0:
                    v -= command[1]
        total += v

    print(f"#{tc} {total}")
