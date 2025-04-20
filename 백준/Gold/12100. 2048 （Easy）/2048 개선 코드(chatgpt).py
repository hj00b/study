from copy import deepcopy

def rotate(board, times):
    # 90도 회전 (times: 1=시계방향, -1=반시계, 2=180도)
    for _ in range(times % 4):
        board = [list(row) for row in zip(*board[::-1])]
    return board

def compress_and_merge(row):
    # 0 제거 후 병합
    new_row = [x for x in row if x != 0]
    result = []
    skip = False
    i = 0
    while i < len(new_row):
        if i + 1 < len(new_row) and new_row[i] == new_row[i + 1]:
            result.append(new_row[i] * 2)
            i += 2
        else:
            result.append(new_row[i])
            i += 1
    result += [0] * (N - len(result))
    return result

def move(board, direction):
    # direction: 0=up, 1=down, 2=left, 3=right
    # 회전 후 왼쪽으로 처리한 뒤, 다시 원래 방향으로 회전 복원
    rotated = rotate(board, direction)
    moved = [compress_and_merge(row) for row in rotated]
    return rotate(moved, -direction)

def f2048(board, cnt):
    global max_value
    if cnt == 5:
        max_value = max(max_value, max(map(max, board)))
        return
    for d in range(4):
        new_board = move(deepcopy(board), d)
        f2048(new_board, cnt + 1)

# 입력 처리
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_value = 0

f2048(arr, 0)
print(max_value)
