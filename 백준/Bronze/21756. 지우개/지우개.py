N = int(input())
arr = list(range(N+1))


def eraser():
    # 지운 자리 저장할 배열
    visited = [0]*(N+1)
    # 홀수 자리를 지운 횟수
    time = 1
    # 안 지운 자리가 index 0번과 마지막 남은 자리만 남을 때까지 반복
    while visited.count(0) != 2:
        # 1회 지울 때마다 지우는 자리가 홀수번째의 배수자리가 되므로
        # 홀수 * 반복횟수로 지운 자리 관리
        for i in range(1, N+1, 2):
            # 곱한 값이 배열을 넘어서지 않는 경우만 체크
            if i*time < N+1:
                visited[i*time] += 1
        # 조건을 충족할 때까지 반복하며 반복횟수 증가
        time += 1
    # 지우지 않은자리 인덱스를 찾기 위해 0번 인덱스의 0을 다른 값으로 변환
    visited[0] = None
    # 지우지 않고 남은 자리 반환
    return visited.index(0)

# 지우지 않은 자리의 값 출력
print(arr[eraser()])