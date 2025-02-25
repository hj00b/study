T = int(input())
for tc in range(1,T+1):
    # 입력 값 입력
    N, M = map(int,input().split())
    flag = [list(input()) for _ in range(N)]
    # 각 색을 카운트할 배열
    flag_count = [[0]*3 for _ in range(N)]
    # 각 행 별로 색의 수를 카운트해서 인덱스 0에 흰색 인덱스 1에 파란색
    # 인덱스 2에 빨간색의 수 저장
    for i in range(N):
        flag_count[i][0] = flag[i].count("W")
        flag_count[i][1] = flag[i].count("B")
        flag_count[i][2] = flag[i].count("R")

    # 국기 형태와 일치하는 개수를 카운트 해서 가장 많이 일치하는 경우를 저장
    max_correct = 0
    # 2중 for문을 통해 배열을 3분할
    # 0 ~ i - 1
    # i ~ j - 1
    # j ~ N - 1의 범위의 행을 각각 흰색, 파란색, 빨간색이 일치하는 수 총 합을 correct에 누적 합
    for i in range(1, N-1):
        for j in range(i+1, N):
            correct = 0
            # print(list(range(0,i)))
            # print(list(range(i,j)))
            # print(list(range(j,N)))
            correct += sum([flag_count[n][0] for n in range(0, i)])
            correct += sum([flag_count[m][1] for m in range(i, j)])
            correct += sum([flag_count[o][2] for o in range(j, N)])
            # 현재까지 중에 가장 많이 일치하는 경우를 저장
            if max_correct < correct:
                max_correct = correct
    # 전체 칸 수 계산 후 맞는 칸 수를 빼기
    area = N * M
    print(f'#{tc} {area - max_correct}')