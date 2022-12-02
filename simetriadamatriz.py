def simetrica(m):
    # retorna o número de elementos da matriz que vai ser exatamente o número de linhas#
    nlinhas = len(m)
    # para obter o mesmo número de colunas quando de linhas for sempre o mesmo
    ncolunas = len(m[0])
    # verificando a simetria da matriz


    for i in range(nlinhas):
        for j in range(i + 1, ncolunas):
            if m[i][j] != m[j][i]:
                return False
    return True

m = [[1,2,3], [2,4,5],[3,5,2]]
print(simetrica(m))