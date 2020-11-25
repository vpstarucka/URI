n = int(input())

for i in range(n):
   i, secret = (int(x) for x in input().split())
   guesses   = [int(x) for x in input().split()]

   closest = min(guesses, key = lambda x: abs(x - secret))

   print(guesses.index(closest) + 1)