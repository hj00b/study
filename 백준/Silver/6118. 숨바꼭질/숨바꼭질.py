from collections import deque

# 헛간의 수, 길의 수(간선 수)
N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)

queue = deque()
queue.append(1)
visited = [0] *(N+1)
visited[1] = 1
while queue:
    v = queue.popleft()

    for w in arr[v]:
        if not visited[w]:
            visited[w] = visited[v] + 1
            queue.append(w)

max_len = max(visited)

print(visited.index(max_len), max_len -1 , visited.count(max_len))