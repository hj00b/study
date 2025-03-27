# 문제 1, 등차 수열
n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
a = sorted(a)

ans = 0
cnt = 0


for i in range(n):
    k = a[i]
    for j in range(i):
        ai = i - j
        for k in range(i+1,n):
            aj = i + k
            if aj - k == k - ai:
                cnt += 1
    if ans < cnt:
        ans = cnt
print(ans)

# 문제 4, 최대 이익 구하기 
n = int(input())
T = []
P = []

for _ in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

# Please write your code here.
i = 0
total = 0
while i < n:
    t = T[i]
    p = P[i]
    next_p = 0
    for j in range(1, t):
        next_p += P[i+j]
    if p > next_p :
        total += p 
        i += t 
        continue
    i += 1
print(total)
