from itertools import zip_longest

VALID = [1, 2, 3, 4, 5, 6, 7, 8, 9]

n = int(input())

for i in range(n):
    print("Instancia", i + 1)

    hsudoku = [[int(x) for x in input().split()] for _ in range(9)]
    vsudoku = zip_longest(*hsudoku)
    bsudoku = [hsudoku[y][x:x + 3] + hsudoku[y + 1][x:x + 3] + hsudoku[y + 2][x:x + 3]
               for y in range(0, 9, 3)
               for x in range(0, 9, 3)]

    if all(sorted(row) == VALID for row in hsudoku) and \
       all(sorted(col) == VALID for col in vsudoku) and \
       all(sorted(box) == VALID for box in bsudoku):
        print("SIM")

    else:
        print("NAO")

    print()