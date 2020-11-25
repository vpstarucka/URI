z, maximum = (int(x) for x in input().split())
pos        = [int(x) for x in input().split()]

pos.append(42195)

diff = [pos[i] - pos[i - 1] for i in range(1, len(pos))]

print(max(diff) <= maximum and "S" or "N")