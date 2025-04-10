for _ in range(4):
    x1a, y1a, x2a, y2a, x1b, y1b, x2b, y2b = map(int, input().split())

    # 완전히 떨어진 경우 (겹치는 부분 없음)
    if x2a < x1b or x2b < x1a or y2a < y1b or y2b < y1a:
        print('d')
    # 점으로만 접하는 경우 (꼭짓점에서만 접함)
    elif (x2a == x1b or x2b == x1a) and (y2a == y1b or y2b == y1a):
        print('c')
    # 선분으로 접하는 경우 (변이 겹침)
    elif (x2a == x1b or x2b == x1a) and (y1a < y2b and y1b < y2a):
        print('b')
    elif (y2a == y1b or y2b == y1a) and (x1a < x2b and x1b < x2a):
        print('b')
    # 그 외 겹치는 경우 (영역이 겹침)
    else:
        print('a')
