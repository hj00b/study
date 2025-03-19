
# 국가의 수, 기록의 수
N, M = map(int, input().split())
country = [0] + [int(input()) for _ in range(N)]
par = list(range(N+1))
rank = [0]*(N+1)
plan = [tuple(map(int, input().split())) for _ in range(M)]


def union(u1, u2):
    if rank[u1] >= rank[u2]:
        par[u2] = u1
        if rank[u1] == rank[u2]:
            rank[u1] += 1
        return u1, u2
    else:
        par[u1] = u2
        return u2, u1
    
def find_set(x):
    if par[x] != x:
        par[x] = find_set(par[x])
    return par[x]

for opq in plan:
    o, p, q = opq
    # 나라 1, 나라 2, 작전
    u1 = find_set(p)
    u2 = find_set(q)
    if o == 1:
        root, v = union(u1, u2)
        country[root] += country[v]
        country[v] = 0        
    elif o == 2:
        s1 = country[u1]
        s2 = country[u2]

        if s1 > s2:
            par[u2] = u1
            country[u1] = s1 - s2
            country[u2] = 0
        elif s1 < s2:
            par[u1] = u2
            country[u2] = s2 - s1
            country[u1] = 0
        elif s1 == s2:
            par[u1] = 0
            par[u2] = 0
            country[u1] = 0
            country[u2] = 0
cnt = 0
country.sort()
for i in range(1, N+1):
    if country[i] != 0:
        cnt+=1
print(cnt)
for i in range(1, N+1):
    if country[i] != 0:
        print(country[i], end=" ")

