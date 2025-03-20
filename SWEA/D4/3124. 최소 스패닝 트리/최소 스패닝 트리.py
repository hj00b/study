def find_set(x):
    if p[x] == x:
        return x
    p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    x_boss = find_set(x)
    y_boss = find_set(y)

    if x_boss == y_boss:
        return

    if x_boss > y_boss:
        p[y_boss] = x_boss
    else:
        p[x_boss] = y_boss


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edges = []
    p = list(range(V + 1))
    for _ in range(E):
        s, e, w = map(int, input().split())
        edges.append((w, s, e))

    cnt = 0
    result = 0
    edges.sort(key=lambda x:x[0])
    for w, u, v in edges:
        if find_set(u) == find_set(v):
            continue
        union(u, v)
        result += w
        cnt += 1
        if cnt == V - 1:
            break
    print(f"#{tc} {result}")