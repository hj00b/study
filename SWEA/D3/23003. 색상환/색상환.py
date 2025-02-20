color = {}
color["red"] = 1
color["orange"] = 2
color["yellow"] = 3
color["green"] = 4
color["blue"] = 5
color["purple"] = 6


T = int(input())
for tc in range(1, T + 1):
    c1, c2 = input().split()
    ans = ""
    if c1 == c2:
        ans = "E"
    if abs(color[c1] - color[c2]) == 1 or abs(color[c1] - color[c2]) == 5:
        ans = "A"
    if ans == "" and color[c1] % 3 == color[c2] % 3:
        ans = "C"
    if ans == "":
        ans = "X"

    print(ans)