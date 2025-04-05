
from collections import deque
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(r, c):
    queue = deque()
    visited = [[0]*M for _ in range(N)]
    queue.append((r,c))
    visited[r][c] = 1
    while queue:
        r, c = queue.popleft()
        vis = visited[r][c]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0<=nr<N and 0<=nc<M and not visited[nr][nc] and arr[nr][nc] != "W":
                visited[nr][nc] = vis +1
                queue.append((nr, nc))
    result = max(map(max, visited))
    return result



N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == "L":
            result = bfs(i, j)
            if ans < result:
                ans = result
print(ans -1)