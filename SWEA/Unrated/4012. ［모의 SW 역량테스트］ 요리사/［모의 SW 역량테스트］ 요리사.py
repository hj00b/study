def food_combine(idx, food):
    global min_s, found_zero
    # 최소 차이가 0이면 더 이상 탐색할 필요 없음
    if found_zero:
        return
    # 조합이 완성되면 맛 계산
    if len(food) == N // 2:
        taste(food)
        return
    # 남은 원소로 조합 채우기 불가능하면 리턴 (가지치기)
    if N - idx < (N // 2 - len(food)):
        return
    food_combine(idx + 1, food + [idx])
    food_combine(idx + 1, food)

def taste(first):
    global min_s, found_zero
    # 첫 조합의 보완 집합 구성
    second = [i for i in range(N) if i not in first]
    
    s1 = 0
    s2 = 0

    # 팀 내 시너지 합 계산 (대칭이므로 한 쌍씩만 더함)
    for i in range(len(first)):
        for j in range(i + 1, len(first)):
            s1 += arr[first[i]][first[j]] + arr[first[j]][first[i]]
    for i in range(len(second)):
        for j in range(i + 1, len(second)):
            s2 += arr[second[i]][second[j]] + arr[second[j]][second[i]]
    
    diff = abs(s1 - s2)
    if diff < min_s:
        min_s = diff
    if min_s == 0:
        found_zero = True  # 0이면 더 이상 볼 필요 없음

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_s = float('inf')
    found_zero = False
    # 대칭 제거를 위해 첫 조합에 0번 재료 포함 후 재귀 호출
    food_combine(1, [0])
    print(f"#{tc} {min_s}")
