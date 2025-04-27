from copy import deepcopy

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cctv_model = {
    1:[[0],[1],[2],[3]],
    2:[[0,2], [1,3]],
    3:[[0,1],[1,2],[2,3],[3,0]],
    4:[[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    5:[[0,1,2,3]]
}


max_value = 0
cctvs = []
visited = [[0]*M for _ in range(N)]
for r in range(N):
    for c in range(M):
        if arr[r][c] != 0 and arr[r][c]!=6:
            cctvs.append((r,c))
            visited[r][c] = 1
        elif arr[r][c] == 6:
            visited[r][c] = 1

# recursion 호출 전에 한 번만 실행
ray_map = {}
for r, c in cctvs:
    ray_map[(r,c)] = {}
    for d in range(4):
        cells = []
        k = 1
        while True:
            nr, nc = r + dr[d]*k, c + dc[d]*k
            if not (0 <= nr < N and 0 <= nc < M) or arr[nr][nc] == 6:
                break
            cells.append((nr, nc))
            k += 1
        ray_map[(r,c)][d] = cells


def dfs(idx, covered):
    global max_value
    if idx == len(cctvs):
        max_value = max(max_value, covered)
        return

    r, c = cctvs[idx]
    for case in cctv_model[arr[r][c]]:
        marked = []
        for d in case:
            for nr, nc in ray_map[(r,c)][d]:
                if not visited[nr][nc]:
                    visited[nr][nc] = 1
                    marked.append((nr, nc))
        dfs(idx+1, covered + len(marked))
        for nr, nc in marked:
            visited[nr][nc] = 0


# 초기 visited 셋업 후
init_covered = sum(sum(row) for row in visited)
dfs(0, init_covered)
print(N*M - max_value)
