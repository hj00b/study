T = int(input())
for tc in range(1, T + 1):
    N = int(input())
 
    def pascals_triangle(num):
        if num != 1:
            lst = [0]
            lst.extend(pascals_triangle(num - 1))
            lst = lst + [0]
            lst_len = len(lst)
            result = []
            for i in range(1, lst_len):
                result += [lst[i]+lst[i-1]]
            print(*result)
            return result
        elif num == 1:
            print(1)
            return [1]
 
    print(f'#{tc}')
    pascals_triangle(N)