import math

def recur(num_idx, total):
    global max_ans
    global min_ans

    if num_idx == N:
        if max_ans < total:
            max_ans = total
        if min_ans > total:
            min_ans = total
        return

    # now_opers = "".join(map(str, opers))
    # if now_opers in memo:
    #     return
    # memo.add(now_opers)

    for i in range(4):
        if opers[i]:
            opers[i] -= 1
            recur(num_idx+1, calc(i, total, nums[num_idx]))
            opers[i] += 1


def calc(oper, x ,y):
    if oper == 0:
        return x + y
    elif oper == 1:
        return x - y
    elif oper == 2:
        return x * y
    else:
        result = x/y
        if result >= 0:
            return x//y
        else:
            return math.ceil(result)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    opers = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    min_ans = 100000000
    max_ans = -100000000

    memo = set()

    recur(1, nums[0])
    print(f"#{tc} {max_ans-min_ans}")