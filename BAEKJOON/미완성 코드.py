N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def rotate(arr):

    top = 0
    left = 0
    bottom = N - 1
    right = M - 1
    rotate_arr = [[0] * M for _ in range(N)]
    for _ in range(R):
        for r in range(bottom, top):
            rotate_arr[r+1][left] = arr[r][left]
            rotate_arr[N - r - 2][right] = arr[N - r - 1][right]
        left += 1
        right -= 1
        for c in range(left, right):
            rotate_arr[top][M-c-2] = arr[top][M-c-1]
            rotate_arr[bottom][c+1] = arr[top][c]
        top += 1
        bottom -= 1
    return rotate_arr

print(*rotate(arr))
