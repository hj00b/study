from collections import deque
N, K = map(int, input().split())

def hideAndSeek():
    queue = deque()
    queue.append(N)
    LIMIT = max(N, K) * 2 + 1
    visited = [0] * LIMIT

    while queue:
        num = queue.popleft()
        if num ==K:
            return visited[num]


        for nn in (num - 1, num + 1, num * 2):
            if 0<=nn<LIMIT and not visited[nn]:
                visited[nn] = visited[num] +1
                queue.append(nn)

ans = hideAndSeek()
print(ans)