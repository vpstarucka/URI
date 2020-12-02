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
aux1 = 0
aux2 = 12
for i in range(5):
	aux1+=1
	aux2-=1
	for j in range(aux1, aux2):
		soma += mr[i][j]
if t == 'S':
	print('%.1f' %(soma))
elif t == 'M':
	print('%.1f' %(soma/30.0))