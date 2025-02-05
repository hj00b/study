import sys

sys.stdin = open("sample_input.txt", "r")
for test_case in range(1, 11):
    N = int(input())
    b_list = list(map(int, input().split()))
    
    view = 0
    for i in range(2, N - 2):
        i_max_flag = 0
        for n in range(i-2, i+3):
            if i == n : 
                continue
            if b_list[i] > b_list[n]:
                i_max_flag += 1

        if i_max_flag == 4:
            max_calc_list = b_list[i-2:i+3] 
            max_calc_list.pop(2)
            sec_bil = max(max_calc_list)
            view += b_list[i] - sec_bil
    print(f"#{test_case} {view}")