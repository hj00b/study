def find_set(x):
    if p[x] == x:
        return x
    p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    if x > y :
        x, y = y, x

    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:
        return

    p[ref_y] = ref_x


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = []
    p = list(range(V+1))
    for _ in range(E):
        s, e, w = map(int, input().split())
        edges.append((w, s, e))

    cnt = 0
    result = 0
    edges.sort()
    for w, u, v in edges:
        if find_set(u) == find_set(v):
            continue
        union(u, v)
        result += w
        cnt += 1
        if cnt == V-1:
            break
    print(f"#{tc} {result}")


