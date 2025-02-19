N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

t_cnt = 0
p_cnt = 0
rest = 0

for s in size :
    if s % T :
        t_cnt += s // T + 1
    else :
        t_cnt += s // T

p_cnt = N // P
rest = N % P

print(t_cnt)
print(p_cnt, rest)