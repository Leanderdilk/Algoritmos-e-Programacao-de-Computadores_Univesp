#colunas tem que virar linhas e linhas colunas
m = [[1,7,8], [5,3,2]]

for j in m:
    print(j)

t = list(map(list, zip(*m)))
for j in t:
    print(j)