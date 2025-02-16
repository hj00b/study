def mklst(lst):
    lst_len = len(lst)
    newlst = [[] for _ in range(100)]
    for i in range(lst_len//2):
        newlst[lst[i*2]].append(lst[i*2+1])
    return newlst
 
def push(item):
    global top
    top += 1
    stack[top] = item
 
def pop():
    global top
    top -= 1
    return stack[top+1]
 
for _ in range(10):
    tc, node = map(int, input().split())
    way_lst = mklst(list(map(int, input().split())))
 
    top = -1
    v = 0
    stack = [0] * (node +1)
    visited = [0] * 100
    visited[v] = 1
 
    while visited[99] == 0:
        for w in way_lst[v]:
            if not visited[w]:
                push(w)
                visited[w] = 1
                v = w
                if v == 99:
                    print(f'#{tc} 1')
                break
        else :
            if top != -1:
                v = pop()
            else :
                print(f'#{tc} 0')
                break