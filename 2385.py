length             = int(input())
p, q, r, s, t, u   = (int(x) for x in input().split())
x_lookup, y_lookup = (int(x) for x in input().split())

row = [(p * x_lookup + q * y) % t for y in range(1, length + 1)]
col = [(r * x + s * y_lookup) % u for x in range(1, length + 1)]

print(sum(elem_a * elem_b for elem_a, elem_b in zip(row, col)))