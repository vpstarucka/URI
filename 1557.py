while True:
    n = int(input())

    if n == 0:
        break

    highest = len(str(2**(n-1) * 2**(n-1)))

    for y in range(n):
        line = ""

        for x in range(n):
            line += "{:>{}} ".format(2**x * 2**y, highest)

        print(line[:-1])

    print()
