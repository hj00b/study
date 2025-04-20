from copy import deepcopy

def up(arr):
    arr = deepcopy(arr)
    for c in range(N):
        merged = [False] * N
        for r in range(1, N):
            if arr[r][c] == 0:
                continue
            nr = r
            while nr > 0 and arr[nr - 1][c] == 0:
                arr[nr - 1][c], arr[nr][c] = arr[nr][c], 0
                nr -= 1
            if nr > 0 and arr[nr - 1][c] == arr[nr][c] and not merged[nr - 1]:
                arr[nr - 1][c] *= 2
                arr[nr][c] = 0
                merged[nr - 1] = True
    return arr

def down(arr):
    arr = deepcopy(arr)
    for c in range(N):
        merged = [False] * N
        for r in range(N - 2, -1, -1):
            if arr[r][c] == 0:
                continue
            nr = r
            while nr < N - 1 and arr[nr + 1][c] == 0:
                arr[nr + 1][c], arr[nr][c] = arr[nr][c], 0
                nr += 1
            if nr < N - 1 and arr[nr + 1][c] == arr[nr][c] and not merged[nr + 1]:
                arr[nr + 1][c] *= 2
                arr[nr][c] = 0
                merged[nr + 1] = True
    return arr

def left(arr):
    arr = deepcopy(arr)
    for r in range(N):
        merged = [False] * N
        for c in range(1, N):
            if arr[r][c] == 0:
                continue
            nc = c
            while nc > 0 and arr[r][nc - 1] == 0:
                arr[r][nc - 1], arr[r][nc] = arr[r][nc], 0
                nc -= 1
            if nc > 0 and arr[r][nc - 1] == arr[r][nc] and not merged[nc - 1]:
                arr[r][nc - 1] *= 2
                arr[r][nc] = 0
                merged[nc - 1] = True
    return arr

def right(arr):
    arr = deepcopy(arr)
    for r in range(N):
        merged = [False] * N
        for c in range(N - 2, -1, -1):
            if arr[r][c] == 0:
                continue
            nc = c
            while nc < N - 1 and arr[r][nc + 1] == 0:
                arr[r][nc + 1], arr[r][nc] = arr[r][nc], 0
                nc += 1
            if nc < N - 1 and arr[r][nc + 1] == arr[r][nc] and not merged[nc + 1]:
                arr[r][nc + 1] *= 2
                arr[r][nc] = 0
                merged[nc + 1] = True
    return arr


def f2048(arr, cnt):
    global max_value
    if cnt == 5:
        max_value = max(max_value, max(map(max, arr)))
        return

    f2048(up(arr), cnt+1)
    f2048(down(arr), cnt+1)
    f2048(left(arr), cnt+1)
    f2048(right(arr), cnt+1)


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
max_value = 0
f2048(arr, 0)
print(max_value)