t = input()
m = []
mr = []
for i in range(12):
	for j in range(12):
		item = float(input())
		m.append(item)
	mr.append(m)
	m = []
soma = 0
for i in range(2, 13):
	for j in range(0, i-1):
		soma += mr[i-1][j]
if t == 'S':
	print('%.1f' %(soma))
elif t == 'M':
	print('%.1f' %(soma/66.0))