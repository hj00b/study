N, M, L = map(int, input().split())

arr = [0] * N
# 첫번째로 공 받음
arr[0] = 1
# 현재 공 위치
ball_idx = 0
# 횟수
cnt = 0
while max(arr) < M :
    if arr[ball_idx] % 2 == 0 : # 짝수번 공을 받음
        ball_idx = (N + ball_idx - L) % N
    else:
        ball_idx = (ball_idx + L) % N
    arr[ball_idx] = arr[ball_idx] + 1
    cnt += 1
print(cnt)