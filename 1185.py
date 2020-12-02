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
aux = 12
for i in range(11):
	aux-=1
	for j in range(aux):
		soma += mr[i][j]
if t == 'S':
	print('%.1f' %(soma))
elif t == 'M':
	print('%.1f' %(soma/66.0))