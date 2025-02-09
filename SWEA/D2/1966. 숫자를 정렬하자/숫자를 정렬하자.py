#import sys
#sys.stdin = open('input (4).txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
    num_list = list(map(int, input().split()))

    # sort 메서드 사용
    # num_list.sort()

    # 카운팅 정렬
    max_num = max(num_list)
    # max 함수 사용하지 않을 경우
    # max_num2 = 0
    # for n in num_list:
    #     if max_num2 < n:
    #         max_num2 = n

    count_list = [0] * (max_num + 1)
    sorted_list = [0] * num
    for num in num_list:
        count_list[num] += 1

    for i in range(1, len(count_list)):
        count_list[i] += count_list[i - 1]

    for j in range(len(num_list)-1, -1, -1):
        count_list[num_list[j]] -= 1
        sorted_list[count_list[num_list[j]]] = num_list[j]

    #print(f'#{test_case} ', end="")
    #for num in sorted_list:
    #    print(num, end=" ")
    #print()
    # 리스트의 요소 출력할 때 참고하기 
    print(f"#{test_case} {' '.join(map(str, sorted_list))}")
