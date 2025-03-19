N = int(input())

arr = list(range(N+1))


def eraser():
    visited = [0]*(N+1)
    time = 1
    while visited.count(0) != 2:
        for i in range(1, N+1, 2):
            if i*time < N+1:
                visited[i*time] += 1
        time += 1
    visited[0] = None
    return visited.index(0)


print(arr[eraser()])