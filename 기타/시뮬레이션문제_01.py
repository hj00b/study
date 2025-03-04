import sys
sys.stdin = open("tree.txt","r")

def my_tree():
    day_cnt = 0
    while sum(tree_diff) != 0:
        day_cnt += 1
        for idx in range(N):
            if day_cnt % 2 != 0:
                if tree_diff[idx] == 1 or tree_diff[idx] > 2:
                    tree_diff[idx] -= 1
                    break
                else:
                    continue

            if day_cnt % 2 == 0:
                if tree_diff[idx] >= 2:
                    tree_diff[idx] -= 2
                    break
                else:
                    continue

    return day_cnt


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = list(map(int, input().split()))
    max_height = max(tree)
    tree_diff = [0] *N

    for i in range(N):
        tree_diff[i] = max_height - tree[i]

    ans = my_tree()

    print(f"#{tc} {ans}")