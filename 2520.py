while True:
    try:
        rows, cols = (int(x) for x in input().split())

        city = [[int(x) for x in input().split()] for _ in range(rows)]

        ax = ay = bx = by = 0

        for y in range(rows):
           if 1 in city[y]: ax, ay = city[y].index(1), y
           if 2 in city[y]: bx, by = city[y].index(2), y

        print(abs(ax - bx) + abs(ay - by))

    except EOFError:
        break