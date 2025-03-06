def find_code():
    code = [-1] * 8
    for r in range(N):
        if sum(map(int, arr[r])) == 0:
            continue
        for c in range(M-56):
            # 시작 지점과 끝 지점이 모두 암호일 때 암호 추출
            if code_table.get(arr[r][c:c+7]) and code_table.get(arr[r][c+49:c+56]):
                num = 0
                # 암호 길이만큼 7길이씩 반복
                for j in range(c, c+56, 7):
                    code[num] = code_table.get(arr[r][j:j+7])
                    num += 1
                return code
    return []


T = int(input())
# 암호 해독?표
code_table = {
    "0001101": "0",
    "0011001": "1",
    "0010011": "2",
    "0111101": "3",
    "0100011": "4",
    "0110001": "5",
    "0101111": "6",
    "0111011": "7",
    "0110111": "8",
    "0001011": "9"
}
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    
    code = find_code()
    # 만약 코드가 의미하는 것이 숫자 0일 경우 False가 되므로 "0"으로 처리한 후 일괄 int처리
    code = list(map(int, code))
    
    # 유효성 검사를 위한 홀수합 짝수합
    odd_sum = code[0]+code[2]+code[4]+code[6]
    even_sum = code[1]+code[3]+code[5]+code[7]
    code_sum = odd_sum*3 + even_sum
    
    if code_sum !=0 and code_sum%10 == 0:
        # 코드가 유효하면 합 출력
        code_sum = odd_sum + even_sum
    else :
        # 유효하지 않으면 0
        code_sum = 0
    print(f"#{tc} {code_sum}")
