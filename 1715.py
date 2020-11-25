a, b = (int(x) for x in input().split())
count = a
for i in range(a):
	item = [int(x) for x in input().split()]
	if item.count(0) > 0:
		count -= 1
print(count)