# 행 길이, 열 길이 8~50
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

# 찾아야 하는 패턴은 2종류다
pattern_BW = ["B","W"]*4
pattern_WB = ["W","B"]*4
board_BW = [pattern_BW if i % 2 == 0 else pattern_WB for i in range(8) ]
board_WB = [pattern_WB if i % 2 == 0 else pattern_BW for i in range(8) ]


min_cnt = 64
for i in range(N-7):
    for j in range(M-7):
        diff_BW = 0
        diff_WB = 0
        # 주어진 전체 보드를 체스 보드 크기로 잘라서 패턴과 얼마나 불일치 하는지 비교
        for r in range(i,i+8):
            for c in range(j,j+8):
                if board[r][c] != board_BW[r-i][c-j]:
                    diff_BW += 1
                if board[r][c] != board_WB[r-i][c-j]:
                    diff_WB += 1
        if min_cnt > diff_BW:
            min_cnt = diff_BW
        if min_cnt > diff_WB:
            min_cnt = diff_WB
print(min_cnt)