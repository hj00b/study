def combine(idx, now_taste, now_cal):
    global max_taste
    # 만약 현재 조합이 제한 칼로리 보다 높으면 탐색 중지
    if now_cal > L:
        return
    else:
        max_taste = max(now_taste, max_taste)
    # 만약 모든 조합을 확인했다면 탐색 중지
    if idx == N:
        return

    t, c = arr[idx]
    # idx 값을 1개씩 증가시키면서 요소를 포함하는 경우와 포함하지 않는 경우
    # 2가지 경우를 계속해서 업데이트하여 모든 조합 생성
    # 인덱스를 통해 모든 요소에 순서대로 접근하며
    # 조합은 순서가 없으므로 이미 확인한 요소에 대해 다시 방문하지 않으므로
    # 순열과 달리 방문한 요소에 대한 기록을 하지 않아도 된다.
    # => 현재 인덱스 이후의 요소만 선택하여 중복을 방지한다
    combine(idx + 1, now_taste + t, now_cal+c)
    combine(idx + 1, now_taste, now_cal)


T = int(input())
for tc in range(1, T + 1):
    # 재료의 수, 제한 칼로리
    N, L = map(int, input().split())
    # 재료별 맛 점수, 칼로리
    arr = [tuple(map(int,input().split())) for _ in range(N)]
    max_taste = 0
    combine(0, 0, 0)

    print(f"#{tc} {max_taste}")