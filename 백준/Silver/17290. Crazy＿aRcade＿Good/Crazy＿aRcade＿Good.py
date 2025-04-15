r, c = map(int, input().split())
r = r - 1
c = c - 1
arr = [list(input()) for _ in range(10)]

pop = [[0] * 10 for _ in range(10)]

for i in range(10):
    for j in range(10):
        if arr[i][j] == "o":
            pop[i][j] = 1
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                for k in range(10):
                    nr = i + dr * k
                    nc = j + dc * k
                    if 0 <= nr < 10 and 0 <= nc < 10:
                        pop[nr][nc] = 1
                    else:
                        break
min_dist = 100
for m in range(10):
    for n in range(10):
        if pop[m][n] == 0:
            dist = abs(m - r) + abs(n - c)
            min_dist = min(dist, min_dist)

print(min_dist)
