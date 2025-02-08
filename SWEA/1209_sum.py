# 02월 08일 SWEA 1209번 Sum
import sys
sys.stdin = open('sum_input.txt', 'r')

while True:
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 최대값을 비교하기 위한 변수 목록
    row_max = 0
    col_max = 0
    cross_sum = 0
    reverse_cross_sum = 0
    max_result = 0
    # 각 행의 합 계산
    for row in arr:
        row_sum = 0
        for col in row:
            row_sum += col
        if row_max < row_sum:
            row_max = row_sum
    # 각 열의 합 계산
    for col in range(len(arr)):
        col_sum = 0
        for row in range(len(arr)):
            col_sum += arr[row][col]
        if col_max < col_sum:
            col_max = col_sum
    # 왼쪽 위에서 오른쪽 아래로 향하는 대각선 합 계산
    for i in range(len(arr)):
        cross_sum += arr[i][i]
    # 오른쪽 위에서 왼쪽 아래로 향하는 대각선 합 계산
    for j in range(len(arr)):
        reverse_cross_sum += arr[j][len(arr) - 1 - j]

    # max값 비교 후 최대값 max_result에 저장
    if row_max > max_result:
        max_result = row_max

    if col_max > max_result:
        max_result = col_max

    if cross_sum > max_result:
        max_result = cross_sum

    if reverse_cross_sum > max_result:
        max_result = reverse_cross_sum

    print(f'#{tc} {max_result}')

    if tc == 10:
        break