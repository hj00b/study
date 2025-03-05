N,A,B,C,D=map(int,input().split())
shelters=[tuple(map(int,input().split())) for _ in range(N)]
 
# Please write your code here.

min_reach = float("inf")

for s in range(C, D+1):
    r = A * s 
    c = B * s
    for sr, sc in shelters:
        reach = abs(r-sr) + abs(c-sc)
        if min_reach > reach:
            min_reach = reach

print(min_reach)
