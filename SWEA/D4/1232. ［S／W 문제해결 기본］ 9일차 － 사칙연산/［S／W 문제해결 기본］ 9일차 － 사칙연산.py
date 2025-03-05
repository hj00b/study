# 중위 순회를 통해 각 숫자와 연산자를 순서에 맞게 순회
def in_order(T):
    global result
    if T :
        left_val = in_order(left[T])
        val = tree[T]
        right_val = in_order(right[T])

        # 방문한 정점이 str을 가지고 있고 숫자로 변경 가능하다면 float로 변경 후 반환
        if type(val) == str and str.isdigit(val):
            val = float(val)
        # 만약 방문한 정점이 연산자라면 자식으로 수를 가지고 있는 상태일 것(중위 순회 순서에 따라..)
        # 연산자에 따라 계산한 후 반환하면 계산된 값이 left_val 혹은 right_val로 반환되며 피연산자로 사용
        elif val == "+":
            val = left_val + right_val

        elif val == "-":
            val = left_val - right_val

        elif val == "*":
            val = left_val * right_val

        elif val == "/":
            val = left_val / right_val

        return val




for tc in range(1, 11):
    N = int(input())
    arr = [list(input().split()) for i in range(N)]
    tree = [0]*(N+1)
    left = [0]*(N+1)
    right = [0]*(N+1)
    for i in range(1, N+1):
        j = i -1
        tree[i] = arr[j][1]
        if len(arr[j]) > 2:
            left[i] = int(arr[j][2])
        if len(arr[i-1]) > 3:
            right[i] = int(arr[j][3])

    ans = in_order(1)

    print(f"#{tc} {int(ans)}")