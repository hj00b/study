from heapq import heappop, heappush


def prim(start_node):
    # 우선순위 큐를 사용해서 현재 노드에서 가장 가중치가 작은 것 선택
    pq = [(0, start_node)]
    MST = [0] * (V+1)

    min_w = 0

    while pq:
        node_w, node = heappop(pq)
        if MST[node]:
            continue
        MST[node] = 1
        min_w += node_w

        # 이동한 자리에서 방문 가능한 노드 찾기
        for next_node in graph[node]:
            if MST[next_node[1]]:
                continue
            heappush(pq, next_node)
    return min_w


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))
        graph[e].append((w, s))
    ans = prim(1)
    print(f"#{tc} {ans}")