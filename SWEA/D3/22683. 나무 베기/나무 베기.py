from collections import deque

T = int(input())
# 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs():
    queue = deque()
    # 좌표, 벤 횟수, 방향
    queue.append((sr, sc, K, 0))
    # visited[r][c][베기][방향]
    visited = [[[[0] * 4 for _ in range(K+1)] for _ in range(N)] for _ in range(N)]

    while queue:
        r, c, k, d = queue.popleft()
        vis = visited[r][c][k][d]

        if r == er and c == ec:
            return vis

        # 직진
        nr, nc = r+dr[d], c+dc[d]

        if 0 <= nr < N and 0 <= nc < N :
            nk = k
            # 나무 베기 체크
            if arr[nr][nc] == 'T':
                if k > 0:
                    nk -= 1
                else:
                    nk = -1
            # 아직 벨 수 있으면
            if nk >= 0 and not visited[nr][nc][nk][d]:
                visited[nr][nc][nk][d] = vis + 1
                queue.append((nr,nc,nk,d))

        # 오른쪽 회전
        nd = (d+1)%4
        if not visited[r][c][k][nd]:
            visited[r][c][k][nd] = vis + 1
            queue.append((r,c,k,nd))

        # 왼쪽 회전
        nd = (d+3)%4
        if not visited[r][c][k][nd]:
            visited[r][c][k][nd] = vis + 1
            queue.append((r, c, k, nd))
    return -1




for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    sr, sc, er, ec = 0, 0, 0, 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == "X":
                sr, sc = r, c
            elif arr[r][c] == "Y":
                er, ec = r, c

    print(f'#{tc} {bfs()}')
