N = int(input())
arr = list(map(int, input().split()))
used = [0] * N

for i in range(N):
    k = arr[i]
    num = 0
    while True:
        if not used[num]:
            if k == 0:
                break
            k -= 1
        num += 1
    used[num] = i + 1
    # print(used)

print(*used)