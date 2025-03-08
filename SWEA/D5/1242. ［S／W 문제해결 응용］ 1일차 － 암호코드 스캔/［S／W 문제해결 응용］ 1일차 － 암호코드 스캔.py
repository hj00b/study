# import sys
# sys.stdin = open("2.txt", "r")

code_table = {
    "3211": "0",
    "2221": "1",
    "2122": "2",
    "1411": "3",
    "1132": "4",
    "1231": "5",
    "1114": "6",
    "1312": "7",
    "1213": "8",
    "3112": "9",
}

reverse_dict = {v: k for k, v in code_table.items()}
code_memo = {}

hex_table = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}


def hex_to_bin():
    for r in range(row):
        for c in range(col):
            arr[r][c] = hex_table[arr[r][c]]
        arr[r] = "".join(arr[r])


def find_code(col):
    r = 0
    c = col - 1
    code_list = []
    while r < row:
        if not sum(int(c) for c in arr[r]):
            r += 1
            continue
        code_len = 0
        while c >= 0:
            code = ""
            if int(arr[r][c]):
                ratio = find_ratio(r, c)
                if ratio == -1:
                    c -= 1
                    continue
                else:
                    code_len = 56 * ratio
                    # 배율을 찾은 경우

                    if c - code_len + 1 >= 0:
                        for code_row in range(c - code_len+1, c+1, 7 * ratio):
                            n_code = "".join(arr[r][code_row:code_row+7*ratio])
                            for code_num in range(10):
                                comp_code = get_code(code_num, ratio)
                                if comp_code == n_code:
                                    code += str(code_num)
                        c -= code_len

                    if code not in code_list:
                        code_list.append(code)
                        continue
            c -= 1
        c = col - 1
        r += 1
    #print(code_list)
    return code_list


def get_code(code_num, n):  # 0~9(복호화한 수), 배율
    code = ""
    # 만약 이전에 찾은 적 없는 코드면 딕셔너리에 저장
    if code_memo.get((code_num, n)) is None:
        for j in range(4):
            code += str(j % 2) * int(reverse_dict[str(code_num)][j]) * n
        code_memo[(code_num, n)] = code
    else:
        code = code_memo.get((code_num, n))
    return code


def find_ratio(r, c):
    num = 6
    n = 1
    while c - num >= 0:
        for code_num in range(10):
            code = get_code(code_num, n)
            if arr[r][c - num:c + 1] == code:
                return n
        num += 7
        n += 1
    return -1

def validation(arr):
    ans = 0
    for code in arr:
        odd = int(code[0]) + int(code[2])+ int(code[4]) + int(code[6])
        even = int(code[1]) + int(code[3]) + int(code[5])
        val = int(code[7])
        total = odd * 3 + even + val
        if total % 10 == 0:
           ans += odd + even + val
    return ans




T = int(input())
for tc in range(1, T + 1):
    row, col = map(int, input().split())
    arr = [list(input()[:col]) for _ in range(row)]

    hex_to_bin()
    c_list = find_code(col*4)
    ans = validation(c_list)

    print(f"#{tc} {ans}")