S = input()
# 소문자 리스트 생성
small_letter = [chr(i) for i in range(ord('a'), ord('z') + 1)]
# 결과를 저장할 리스트, 기본 값은 포함되어 있지 않음(-1)
result_lst = [-1] * 26

for i in range(len(S)):
    # S의 i번째 문자가 몇 번째 알파벳인지
    idx = small_letter.index(S[i])
    # 알파벳 소문자이고, 등장한적 없을 경우 위치 저장
    if S[i] in small_letter and result_lst[idx] == -1:
        result_lst[idx] = i
print(*result_lst)