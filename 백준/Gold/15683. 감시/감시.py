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


def recursion(visited, idx):
    global max_value
    if idx == len(cctvs):
        max_value = max(max_value, sum(map(sum,visited)))
        return

    r, c = cctvs[idx]

    for case in cctv_model[arr[r][c]]:
        for_use = deepcopy(visited)
        for d in case:
            k = 1
            while True:
                nr, nc = r + dr[d]*k, c + dc[d]*k
                if 0 <= nr < N and 0 <= nc < M:
                    k += 1
                    if arr[nr][nc] == 6:
                        break
                    if not for_use[nr][nc]:
                        for_use[nr][nc] = 1
                else:
                    break
        recursion(for_use, idx+1)

recursion(visited, 0)
print(N*M - max_value)