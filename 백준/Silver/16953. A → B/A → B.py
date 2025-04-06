A, B = map(int, input().split())
memo = set()

def atob(num, cnt):
    global ans
    if num == B:
        ans = min(ans, cnt)

    # 값이 커지는 연산만 존재 > 값이 B보다 커지면 종료 가능
    if num > B:
        return

    # 이미 memo에 추가된 적이 있다면 최소한의 연산으로 해당 숫자에 도달한 적이 있음
    if num in memo:
        return
    memo.add(num)

    # *2
    atob(num*2, cnt + 1)
    # 가장 오른쪽에 1 추가
    atob(int(str(num)+"1"), cnt + 1)

# 4바이트 int 최대의 근사값
ans = int(21e8)
# A 부터 시작, 연산수 + 1을 출력해야 하므로 시작점을 1로
atob(A, 1)

if ans == int(21e8):
    # ans가 변하지 않았으면 만들지 못 했다는 의미
    print(-1)
else:
    # ans가 만들어졌다면 최소 ans 출력
    print(ans)