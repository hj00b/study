T = int(input())
nums = list(map(int, input().split()))

cnt = 0
for num in nums:
    i = 2
    flag = True
    if num == 1:
        flag = False
    while i < num:
        if num % i == 0 :
            flag = False
            break
        i += 1
    if flag:
        cnt += 1
print(cnt)