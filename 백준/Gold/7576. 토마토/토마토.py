# 접근 방법
# -1로 둘러쌓인 부분에 대해서 BFS만으로 판단하기 어려우므로
# 1을 만나면 DFS로 방문할 수 있는 곳을 visited배열로 먼저 기록하고
# 방문 가능한 곳만 BFS로 방문
# 모든 방문을 끝내고 방문하지 못한 0이 있다면 -1 아니라면 
# 최대값을 출력

from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

stack = [0] * 1000000
top = -1
queue = deque()
visited = [[-2]*M for _ in range(N)]


dr = [-1,1,0,0]
dc = [0,0,-1,1]

for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            queue.append((r,c))
            visited[r][c] = 1
            while True:
                # r, c에서 시작하는 dfs
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < N and 0 <= nc < M and visited[nr][nc]==-2 and arr[nr][nc] != -1:
                        visited[nr][nc] = 0
                        top += 1
                        stack[top] = (r, c)
                        r, c= nr, nc
                        break
                else:
                    # 더 이상 갈 곳이 없음
                    if top != -1:
                        r, c = stack[top]
                        top -= 1
                    else:
                        break

while queue:
    r, c = queue.popleft()
    vis = visited[r][c]
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0<= nr < N and 0<= nc <M and not visited[nr][nc]:
            visited[nr][nc] = vis + 1
            if arr[nr][nc] == -1:
                visited[nr][nc] = -1
                continue
            queue.append((nr,nc))
flag = True
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and visited[i][j] == -2:
            flag = False
            break
if flag:
    print(max(map(max, visited)) -1)
else:
    print(-1)