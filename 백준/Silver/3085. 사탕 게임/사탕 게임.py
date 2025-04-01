

def count_candy(val_list):
    # 현재 체크할 행 또는 열의 첫번째 색
    now = val_list[0]
    # 현재 확인하고 있는 연속된 사탕 카운트
    cnt = 1
    # 최댓값 저장 변수
    max_cnt = 0
    for i in range(1, len(val_list)):
        # 연속된 값이면 cnt 증가
        # 아닐 경우 현재까지 카운트한 값과 최댓값을 비교 후
        # 필요 시 최댓값 갱신
        # 현재 확인하는 색 변경과 카운트 초기화
        if val_list[i] == now:
            cnt += 1
        else :
            max_cnt = max(max_cnt, cnt)
            now = val_list[i]
            cnt = 1
    max_cnt = max(max_cnt, cnt)
    return max_cnt


N = int(input())
candy = [list(input()) for _ in range(N)]
ans = 0
for r in range(N):
    for c in range(N):
        # 좌우가 다른 경우 교환 후 카운트
        if c+1 < N and candy[r][c] != candy[r][c + 1]:
            candy[r][c], candy[r][c + 1] = candy[r][c + 1], candy[r][c]

            col1 = [candy[row][c] for row in range(N)]
            col2 = [candy[row][c+1] for row in range(N)]
            row1 = candy[r]
            ans = max(ans, count_candy(col1), count_candy(col2), count_candy(row1))

            candy[r][c], candy[r][c + 1] = candy[r][c + 1], candy[r][c]


for r in range(N):
    for c in range(N):
        # 상하 가 다른 경우 교환 후 카운트
        if r+1 <N and candy[r][c] != candy[r + 1][c]:
            candy[r][c], candy[r + 1][c] = candy[r + 1][c], candy[r][c]

            row1 = candy[r]
            row2 = candy[r+1]
            col = [candy[row][c] for row in range(N)]
            ans = max(ans, count_candy(row1), count_candy(row2), count_candy(col))

            candy[r][c], candy[r + 1][c] = candy[r + 1][c], candy[r][c]


# 교환하지 않은 경우에 최댓값이 있을 경우 체크
for idx in range(N):
    row = candy[idx]
    col = [candy[i][idx] for i in range(N)]
    ans = max(ans, count_candy(row), count_candy(col))

print(ans)