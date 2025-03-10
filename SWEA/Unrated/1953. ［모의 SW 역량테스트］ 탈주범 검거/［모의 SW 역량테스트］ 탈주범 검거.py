dr = [[],
      [-1, 1, 0, 0],
      [-1, 1],
      [0, 0],
      [-1, 0],
      [1, 0],
      [1, 0],
      [-1, 0]]

dc = [[],
      [0, 0, -1, 1],
      [0, 0],
      [-1, 1],
      [0, 1],
      [0, 1],
      [0, -1],
      [0, -1]
      ]


def time_cnt(v, t):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if 0 < v[i][j] <= t:
                cnt += 1
    return cnt


def bfs(sr, sc):
    queque = [0] * (N * M + 1)
    top = rear = -1
    visited = [[0] * M for _ in range(N)]

    rear += 1
    queque[rear] = (sr, sc)
    visited[sr][sc] = 1

    while top != rear:
        top += 1
        r, c = queque[top]

        now_pipe = arr[r][c]
        for i in range(len(dr[now_pipe])):
            nr = r + dr[now_pipe][i]
            nc = c + dc[now_pipe][i]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] and not visited[nr][nc]:
                n_vis = [0] * 4
                next_pipe = arr[nr][nc]
                for j in range(len(dr[next_pipe])):
                    # 내가 nr, nc 에서 r, c로 갈 수 있나 == nr, nc 에서 r,c에 갈 수 있나
                    # 방문할 것이 아니니까 범위 체크 안 해도 괜찮나?
                    cr, cc = (nr + dr[next_pipe][j], nc + dc[next_pipe][j])
                    if cr == r and cc == c:
                        rear += 1
                        queque[rear] = (nr, nc)
                        visited[nr][nc] = visited[r][c] + 1
                        break # for j (다음 칸으로 갈 수 있었다면 종료)
    return time_cnt(visited,time)


T = int(input())
for tc in range(1, T + 1):
    # 세로, 가로, 시작점(r,c), 시간
    N, M, start_r, start_c, time = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = bfs(start_r, start_c)
    print(f"#{tc} {ans}")
