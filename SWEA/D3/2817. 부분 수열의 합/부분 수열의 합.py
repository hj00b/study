# 조건
# 1<= N <= 20, 1<= K <= 1000
# 2^20 = 1048576
# 테스트 케이스 20개
# 제한 8초 -> 가능

# 각 idx값 별로 포함 여부를 확인할 것이기 때문에
# 탐색할 idx, total에 값을 더한 인덱스의 리스트(자료형 아님), 요소 값의 합
def recur(idx, idx_list, total):
    if total == K and idx_list not in result:
        result.add(idx_list)
        return
    if idx == N:
        return
    if total > K:
        return
    # 인덱스 값을 문자열로 전달할 때 구분자가 없으면 12와 1, 2를 구분할 수 없음...
    recur(idx + 1, idx_list + f"{idx}.", total + arr[idx])
    recur(idx + 1, idx_list, total)


T = int(input())
for tc in range(1, T + 1):
    # 수열 원소의 개수, 목표 원소의 합 값
    N, K = map(int, input().split())
    # 수열
    arr = list(map(int, input().split()))
    # 중복 값을 제거한 경우의 수 저장
    result = set()
    recur(0, "", 0)
    print(f"#{tc} {len(result)}")
