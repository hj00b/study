T = int(input())
for tc in range(1, T + 1):
    carrot_num = int(input())  # 당근의 개수
    carrots = sorted(map(int, input().split()))
    # 모든 당근의 크기를 저장
    # 사이즈의 중복 제거 후 사이즈 별로 카운트
    c_cnt_by_size = [carrots.count(s) for s in sorted(set(carrots))]
    # 3분할 할 대상의 길이
    whole_len = len(c_cnt_by_size)
    # 바구니에 최대로 담을 수 있는 수 제한
    b_max = carrot_num // 2
    # 최대 개수 - 최소 개수 값을 저장할 리스트
    gap = []
    for i in range(0, whole_len):
        for j in range(i + 1, whole_len):
            # 나눠 담기
            size_s = sum(c_cnt_by_size[:i])
            size_m = sum(c_cnt_by_size[i:j])
            size_l = sum(c_cnt_by_size[j:])
            # 조건에 맞게 담았다면 gap 계산
            if 0< size_s <= b_max and 0<size_m <= b_max and 0< size_l <= b_max:
                gap.append(max(size_s, size_m, size_l)-min(size_s, size_m, size_l))
    # 조건을 충족하는 케이스가 없다면 -1 있다면 차 출력
    if gap:
        print(f'#{tc} {min(gap)}')
    elif len(gap)==0:
        print(f'#{tc} -1')