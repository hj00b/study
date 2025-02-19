txt = input()

txt_idx = 0
result = ""
stack = []
# 스택에 문자가 남아 있으면 반환하는 함수
def stack_pop():
    global result
    while stack:
        result += stack.pop()

# break를 만날 때까지 반복
while True :
    #  현재 탐색할 문자
    c = txt[txt_idx]

    # 태그를 만나면
    # 앞에 뒤집어야 하는 글자가 있을 경우 stack_pop()
    # <에서 >까지 result에 추가
    if c == "<" :
        stack_pop()
        while txt[txt_idx] != ">" :
            c = txt[txt_idx]
            result += c
            txt_idx += 1
        result += txt[txt_idx]
        continue


    # 태그나 공백이 아니면 문자 >> stack에 저장
    if c != " " and c != "<" and c != ">" :
        stack.append(c)
    # 공백을 만나면 공백 이전이 단어이므로 stack_pop()
    if c == " ":
        stack_pop()
        result += " "
    # 다음 문자 탐색
    txt_idx += 1
    # 만약 다음 문자가 없다면 while 종료
    if txt_idx >= len(txt) :
        break
# 남은 문자 반환
stack_pop()
# 출력
print(result)