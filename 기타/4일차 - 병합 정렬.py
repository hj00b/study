def merge_sort(start, end):
    if start == end - 1:
        return start, end

    mid = (start+end)//2

    left_start, left_end = merge_sort(start, mid)
    right_start, right_end = merge_sort(mid,end)

    merge(left_start, left_end, right_start, right_end)

    return start, end

def merge(left_start, left_end, right_start, right_end):
    global cnt

    # 분할한 배열의 제일 작은 원소의 인덱스
    l, r = left_start, right_start

    if li[left_end-1] > li[right_end-1]:
        cnt += 1

    # 정렬 결과를 저장할 배열
    N = right_end - left_start
    result = [0]*N
    idx = 0

    while l < left_end and r < right_end:
        if li[l] < li[r]:
            result[idx] = li[l]
            l += 1
            idx += 1
        else:
            result[idx] = li[r]
            r += 1
            idx += 1

    while r < right_end:
        result[idx] = li[r]
        r += 1
        idx += 1

    while l < left_end:
        result[idx] = li[l]
        l += 1
        idx += 1

    for i in range(N):
        li[left_start+i] = result[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))

    # 분할된 리스트를 합칠 때 왼쪽의 마지막 원소가 오른쪽의 마지막 원소보다 큰 경우를 카운트
    cnt = 0
    merge_sort(0,N)
    print(f"#{tc} {li[N//2]} {cnt}")
