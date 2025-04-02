
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c, vis):
    queue = deque()
    queue.append((r, c))
    now = arr[r][c]
    vis[r][c] = 1
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not vis[nr][nc] and arr[nr][nc]==1:
                if arr[nr][nc] == now:
                    vis[nr][nc] = 1
                    queue.append((nr, nc))
    return vis


T = int(input())
for tc in range(1,T+1):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    cnt = 0
    for k in range(K):
        c, r = map(int,input().split())
        arr[r][c] = 1

    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1 and not visited[r][c]:
                vis = bfs(r, c, visited)
                visited = vis
                cnt += 1
    print(cnt)
