from heapq import heappop, heappush

INF = int(21e8)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dijkstra(start_r, start_c):
    pq = [(0, start_r, start_c)]
    costs = [[INF] * N for _ in range(N)]
    costs[start_r][start_c] = 0

    while pq:
        cost, r, c = heappop(pq)

        if costs[r][c] < cost:
            continue

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                next_cost = cost + abs(int(arr[0][0]) - int(arr[nr][nc]))
                if costs[nr][nc] <= next_cost:
                    continue
                costs[nr][nc] = next_cost
                heappush(pq, (next_cost, nr, nc))

    return costs


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]
    result = dijkstra(0, 0)

    print(f"#{tc} {result[N - 1][N - 1]}")