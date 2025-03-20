from heapq import heappop, heappush


def prim(start_node):
    pq = [(0, start_node)]
    MST = [0] * N

    min_cost = 0

    while pq:
        cost, node = heappop(pq)
        if MST[node]:
            continue
        MST[node] = 1
        min_cost += cost
        # 갈 수 있는 곳 확인
        for idx in range(N):
            if arr[node][idx] == 0:
                continue
            if MST[idx]:
                continue
            heappush(pq, (arr[node][idx], idx))
    return min_cost



# 모든 간선의 경우를 다 살펴야하므로? 프림
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    tax = float(input())
    arr = [[0] * N for _ in range(N)]
    for r in range(N - 1):
        for c in range(r + 1, N):
            cost = ((x[r] - x[c]) ** 2 + (y[r] - y[c]) ** 2) * tax
            arr[r][c] = cost
            arr[c][r] = cost

    ans = prim(0)
    ans = round(ans)
    print(f"#{tc} {ans}")