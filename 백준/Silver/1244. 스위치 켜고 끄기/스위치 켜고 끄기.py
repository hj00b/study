bulb_len = int(input())
bulbs = list(map(int, input().split()))
case_num = int(input())
for i in range(case_num):
    gender, num = map(int, input().split())
    idx = num - 1
    if gender == 1:
        for idx in range(idx, bulb_len, num):
            bulbs[idx] = (bulbs[idx]+1)%2
    elif gender == 2:
        n1 = idx + 1
        n2 = idx - 1
        while 0<=n1<bulb_len and 0<=n2<bulb_len:
            if bulbs[n1] == bulbs[n2]:
                bulbs[n1] = bulbs[n2] = (bulbs[n1] + 1) % 2
            else :
                break
            n1 += 1
            n2 -= 1
        bulbs[idx] = (bulbs[idx]+1) % 2
text =""
for i in range(bulb_len):
    if i != 0 and i % 20 == 0:
        text += "\n"
    text += str(bulbs[i])
    if (i + 1) % 20 != 0 and i != bulb_len - 1:
        text += " "
print(text)