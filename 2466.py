n     = int(input())
level = [int(x) for x in input().split()]

for balls in range(n - 1, 0, -1):
   level = [level[i] == level[i + 1] and 1 or -1 for i in range(balls)]
   
print(level[0] == 1 and "preta" or "branca")