T = int(input())
for tc in range(1, T + 1):
    # 공백을 기준으로 나눠진 데이터를 N과 S에 각각 저장
    N, S = input().split()
    # 문자열의 각 문자를 N회 반복하며 출력
    for c in S:
        for _ in range(int(N)):
            print(c, end="")
    print()