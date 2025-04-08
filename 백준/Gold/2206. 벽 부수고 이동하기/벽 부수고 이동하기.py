from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    queue = deque()
    visited = [[[0]*M for _ in range(N)] for _ in range(2)]
    queue.append((1,0,0))
    visited[1][0][0] = 1
    while queue:
        chance, r, c = queue.popleft()
        if r == N-1 and c == M - 1:
            return visited[chance][r][c]
        vis = visited[chance][r][c]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0<=nr<N and 0<=nc<M:
                if not visited[chance][nr][nc] and map_arr[nr][nc] != 1:
                    visited[chance][nr][nc] = vis + 1
                    queue.append((chance, nr, nc))
                elif chance == 1 and map_arr[nr][nc] == 1 and not visited[0][nr][nc]:
                    visited[0][nr][nc] = vis + 1
                    queue.append((0, nr, nc))
    return -1


N, M = map(int, input().split())

map_arr = [list(map(int, input())) for _ in range(N)]
ans = bfs()
print(ans)