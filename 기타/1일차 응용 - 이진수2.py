T = int(input())
for tc in range(1, T + 1):
    N = float(input())
    bin_num = ""

    for i in range(1, 13):
        # 십진수로 표현한 실수가 이진수로 표현할 수 있는 실수를 포함 중이라면
        # 이진 수로 표현한 후 남은 값을 이진수로 표현할 수 있는지 반복
        # 만약 표현할 수 없다면 다음 이진수와 비교하며 반복
        if N >= 1/2**i:
            bin_num += "1"
            N = N - (1/2**i)
        else:
            bin_num += "0"
        # N이 0이 되었다면 해당 십진수의 실수는 이진수로 표현이 완료됨
        if N == 0:
            break
    else:
        # for 문에서 break를 만나지 않았다면 N은 0이 아니므로
        # 이진수 12자리수까지 찾았으나 완전히 표현하지 못했으므로 overflow
        bin_num = "overflow"

    print(f"#{tc} {bin_num}")
