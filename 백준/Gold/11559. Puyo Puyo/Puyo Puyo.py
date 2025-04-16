from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

# bfs : 터지는 자리인지 확인
def bfs(r, c, target):
    queue = deque()
    visited = [[0]*12 for _ in range(6)]
    queue.append((r, c))
    visited[r][c] = 1

    while queue:
        r, c = queue.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0<=nr<6 and 0<=nc<12 and not visited[nr][nc] and arr[nr][nc] == target:
                visited[nr][nc] = 1
                queue.append((nr, nc))

    if sum(map(sum,visited)) >= 4:
        return visited, True

    else:
        return visited, False

arr = [list(input()) for _ in range(12)]
# 방향이 확인이 어려워 행 방향으로 이동시키기 위해 전치
arr = list(map(list, zip(*arr)))

color = "RGBPY"
pop_cnt = 0

while True:
    now_turn_puyo = False
    to_pop = [[0]*12 for _ in range(6)]
    for r in range(6):
        for c in range(12):
            if arr[r][c] in color:
                visited, is_pop = bfs(r, c, arr[r][c])
                if is_pop:
                    # 4개 이상 모여 있음
                    now_turn_puyo = True
                    # 터트리고 빈자리로 표시
                    for n in range(6):
                        for m in range(12):
                            if visited[n][m]:
                                to_pop[n][m] = True

    if not now_turn_puyo:
        break
    pop_cnt += 1

    # 2) 한꺼번에 삭제
    for r in range(6):
        for c in range(12):
            if to_pop[r][c]:
                arr[r][c] = "."

    # 3) 중력 적용 (무조건 갱신)
    for r in range(6):
        new_row = [arr[r][c] for c in range(12) if arr[r][c] != "."]
        arr[r] = ["." for _ in range(12 - len(new_row))] + new_row


print(pop_cnt)




