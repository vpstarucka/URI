while True:
   n = int(input())

   if n == 0:
      break

   people = [int(x) for x in input().split()]
   time   = 0

   for i in range(n):
      try:
         if people[i + 1] - people[i] >= 10:
            time += 10
         else:
            time += people[i + 1] - people[i]

      except:
         time += 10

   print(time)