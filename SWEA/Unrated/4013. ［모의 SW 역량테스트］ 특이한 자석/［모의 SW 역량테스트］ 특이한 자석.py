# 왼쪽 방향, 오른쪽 방향별로 비교 인덱스가 같으므로
# 각 진행 방향 별로 비교와 회전 반복
# idx는 현재 보고 있는 자석
# add는 왼쪽 오른쪽 방향 판별하는 변수
# way는 회전 방향
def wave(idx, add, way):

    next_idx = idx + add
    if add == 1 and next_idx < 4 and comp_mags[idx][2] != comp_mags[next_idx][6]:
        rotate(next_idx, -way)
        wave(next_idx, add, -way)
    if add == -1 and next_idx > -1 and comp_mags[idx][6] != comp_mags[next_idx][2]:
        rotate(next_idx, -way)
        wave(next_idx, add, -way)


def rotate(target_idx, way):
    if way == 1:
        # 시계 방향 회전
        mags[target_idx] = [mags[target_idx][7]] + mags[target_idx][:7]
    elif way == -1:
        # 반시계 방향 회전
        mags[target_idx] = mags[target_idx][1:] + mags[target_idx][:1]


T = int(input().strip())
for tc in range(1, T + 1):
    K = int(input().strip())
    mags = [list(map(int, input().strip().split())) for _ in range(4)]

    for i in range(K):
        target_mag, way = map(int, input().strip().split())
        # 회전 전의 상태와 비교해야 하므로 복사본 생성
        comp_mags = mags.copy()
        wave(target_mag - 1, 1, way)
        wave(target_mag - 1, -1, way)
        rotate(target_mag-1, way)

    score = 0
    for i in range(4):
        score += mags[i][0] * (1 << i)
    print(f"#{tc} {score}")