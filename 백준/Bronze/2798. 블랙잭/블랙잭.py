N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 정답을 저장할 변수

def find_ans():
    ans = 0
    i2 = i3 = 0
    for i in range(N-2):
        i1 = arr[i]
        for j in range(i+1, N-1):
            i2 = arr[j]
            for k in range(j+1, N):
                i3 = arr[k]
                if ans < i1 + i2 + i3 <= M:
                    ans = i1 + i2 + i3
                    if ans == M :
                        return ans
    return ans

print(find_ans())