rows, cols = (int(x) for x in input().split())

hfield = [[int(x) for x in input().split()] for _ in range(rows)]
vfield = list(zip(*hfield))

print(max(sum(seq) for seq in hfield + vfield))