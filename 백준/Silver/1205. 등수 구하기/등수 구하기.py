# 숫자의 수, 태수의 점수, 랭킹 끝 수
try:
    N, score, P = map(int, input().split())
    scores = list(map(int,input().split()))
except EOFError:
    scores = []

rank = N + 1
out_of_rank = N + 1
for s in scores:
    if s <= score:
        rank -= 1
    if s < score:
        out_of_rank -= 1

if out_of_rank > P:
    out_of_rank = True
else:
    out_of_rank = False
if out_of_rank:
    print(-1)
else:
    print(rank)