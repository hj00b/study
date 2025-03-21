T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    password = input().strip()
    nums = set()

    num_len = N//4
    for i in range(N):
        start = i
        end = i + num_len
        if start >= N - num_len:
            end = end % N
            nums.add(int(password[start:]+password[:end],16))
        else:
            nums.add(int(password[start:end],16))
    sorted_nums = sorted(nums, reverse=True)
    print(f"#{tc} {sorted_nums[K-1]}")
