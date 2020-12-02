while True:
   try:
      n = int(input())

      start  = n//3
      middle = n//2
      end    = n - start

      for y in range(n):
         for x in range(n):
            if   x == middle and y == middle:                       print(4, end = "")
            elif x >= start and y >= start and x < end and y < end: print(1, end = "")
            elif x == y:                                            print(2, end = "")
            elif (n - 1) - x == y:                                  print(3, end = "")
            else:                                                   print(0, end = "")

         print()
      
      print()

   except EOFError:
      break