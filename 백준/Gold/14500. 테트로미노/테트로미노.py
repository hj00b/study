# 상하 좌우 대각선 (2시 5시 7시 10시 방향)
dr = [-1, 1, 0, 0, -1, 1, 1, -1]
dc = [0, 0, -1, 1, 1, 1, -1, -1]
# 이동 방향 정의 (상:0, 하:1, 좌:2, 우:3)

tetro = [[1, 1, 1], [3, 3, 3], # 1자
         [3, 1, 2], # ㅁ
         [1, 1, 3], [0, 3, 3], [3, 1, 1], [3, 3, 0], # ㄴ
         [1, 1, 2], [1, 3, 3], [0,0,3], [3, 3, 1], # ㄴ
         [1, 3, 1], [3, 0, 3], # ㄹ
         [1, 2, 1], [3, 1, 3], # ㄹ
         [3, 3, 6], [1, 1, 7], [3, 3, 7], [1, 1, 4]] # ㅏ


N, M = map(int, input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

ans = 0
for row in range(N):
    for col in range(M):
        for t in tetro:
            r = row
            c = col
            total = arr[r][c]
            for d in t:
                nr = r+ dr[d]
                nc = c + dc[d]
                if 0<=nr<N and 0<=nc<M:
                    total += arr[nr][nc]
                    r = nr
                    c = nc
                else:
                    break
            else:
                ans = max(ans, total)
print(ans)