# 예시 그림은 누워있지만 일반 2차원 배열로 생각해서 풀이해도 무관
# 평범한 달팽이 문제

R, C = map(int, input().split())
K = int(input())

visited = [[0] * C for _ in range(R)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

r = 0
c = 0
d = 0
visited[r][c] = 1
flag = True
if R*C < K:
    flag = False

while flag:
    nr = r + dr[d]
    nc = c + dc[d]
    if nr >= R or nr < 0 or nc >=C or nc < 0:
        d = (d+1)%4
        continue
    now = visited[r][c]
    if now == K:
        break

    if not visited[nr][nc]:
        visited[nr][nc] = now + 1
        r = nr
        c = nc

    else:
        d = (d + 1) % 4
if flag:
    print(r+1, c+1)
else:
    print(0)
