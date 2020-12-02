while True:
    try:
        rows, cols = (int(x) for x in input().split())

        table = [[int(x) for x in input().split()] for _ in range(rows)]

        for y in range(rows):
            for x in range(cols):
                if table[y][x] == 1:
                    print(9, end = "")
                else:
                    neighbours = 0

                    if x - 1 >= 0   and table[y][x - 1]: neighbours += 1
                    if x + 1 < cols and table[y][x + 1]: neighbours += 1
                    if y - 1 >= 0   and table[y - 1][x]: neighbours += 1
                    if y + 1 < rows and table[y + 1][x]: neighbours += 1

                    print(neighbours, end = "")

            print()

    except EOFError:
        break