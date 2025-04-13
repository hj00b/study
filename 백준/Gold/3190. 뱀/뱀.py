from collections import deque

# 입력
N = int(input())
K = int(input())
apple = set(tuple(map(lambda x: int(x)-1, input().split())) for _ in range(K))
L = int(input())
head_dir = {int(t): c for t, c in (input().split() for _ in range(L))}

# 동(0), 남(1), 서(2), 북(3)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def snack():
    board = [[0]*N for _ in range(N)]
    snake = deque([(0, 0)])
    board[0][0] = 1
    direction = 0
    time = 0

    while True:
        time += 1
        r, c = snake[-1]
        nr, nc = r + dr[direction], c + dc[direction]

        # 1) 벽 충돌
        if not (0 <= nr < N and 0 <= nc < N):
            return time
        # 2) 자기 몸 충돌 (꼬리 제거 전이므로, 꼬리 칸도 충돌로 처리)
        if board[nr][nc] == 1:
            return time

        # 3) 머리 이동
        snake.append((nr, nc))
        board[nr][nc] = 1

        # 4) 사과 여부
        if (nr, nc) in apple:
            apple.remove((nr, nc))
        else:
            # 사과 없으면 꼬리 제거
            tr, tc = snake.popleft()
            board[tr][tc] = 0

        # 5) 방향 전환
        if time in head_dir:
            if head_dir[time] == 'D':
                direction = (direction + 1) % 4
            else:  # 'L'
                direction = (direction - 1) % 4

print(snack())
