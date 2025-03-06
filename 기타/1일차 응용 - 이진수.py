T = int(input())
# 0 ~ 15의 값으로 변환할 수 있도록 딕셔너리 준비
hex_dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, "C": 12, "D": 13,
            "E": 14, "F": 15}
for tc in range(1, T + 1):
    n, hex_num = input().split()
    bin_num = ""
    for i in range(int(n) - 1, -1, -1):
        for shift in range(4):
            if hex_dict[hex_num[i]] & (1 << shift):
                bin_num = "1" + bin_num
            else:
                bin_num = "0" + bin_num
    print(f"#{tc} {bin_num}")
