l = int(input())
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
for i in range(12):
	soma += mr[l][i]
if t == 'S':
	print(soma)
elif t == 'M':
	print(soma/12.0)