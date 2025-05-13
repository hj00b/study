# 정점수/간선수/시작정점
from collections import deque
N, M, V = map(int, input().split())
nodes = [[] for i in range(N+1)]

for i in range(M):
    v, w = map(int, input().split())
    nodes[v].append(w)
    nodes[w].append(v)

# 작은 순서대로 방문할 수 있도록 정렬
nodes = list(map(sorted, nodes))


def dfs():
    v = V
    visited = [0] * (N + 1)
    stack = []
    visited[V] = 1
    print(V, end=" ")
    while True:
        for node in nodes[v]:
            if not visited[node]:
                stack.append(v)
                print(node, end=" ")
                visited[node] = 1
                v = node
                break

        else:
            # 다음 갈 곳이 없었다
            if stack:
                # 돌아갈 곳이 있음
                v = stack.pop()

            else:
                # 돌아갈 곳 없음. 끝
                break


def bfs():
    visited = [0]*(N+1)
    queue = deque()
    queue.append(V)
    visited[V] = 1
    print(V, end=" ")
    while queue:
        v = queue.popleft()
        for node in nodes[v]:
            if not visited[node]:
                queue.append(node)
                print(node, end=" ")
                visited[node] = 1


dfs()
print("")
bfs()

