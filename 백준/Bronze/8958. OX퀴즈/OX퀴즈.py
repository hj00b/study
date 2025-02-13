T = int(input())
for tc in range(1, T+1):
    # 정답이 반복되는 경우를 리스트에 저장
    # filter(함수, 함수를 적용할 요소들) 형식
    # 각 요소에 함수를 적용하고 적용한 값의 True 와 False 를 판단
    # True 에 해당하는 값만 반환(iterator객체)
    # [s for s in input().split("X") if s]와 결과가 같음
    correct = list(filter(None, input().split("X")))
    #  n부터 1까지 누적 합을 구하는 재귀 함수(증가하는 점수를 누적)
    def preifx_sum(n):
        if n == 1:
            return 1
        else:
            return n  +  preifx_sum(n-1)

    ans = 0
    for c in correct:
        # 증가하는 점수의 합을 함수를 통해 반환 받아 모든 점수를 합산
        ans += preifx_sum(len(c))
    print(ans)