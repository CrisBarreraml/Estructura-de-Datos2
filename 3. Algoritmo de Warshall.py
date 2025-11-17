def warshall(matriz):
    n = len(matriz)
    cierre = [fila[:] for fila in matriz]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                cierre[i][j] = cierre[i][j] or (cierre[i][k] and cierre[k][j])

    return cierre

matriz = [
    [1, 1, 0],
    [0, 1, 1],
    [0, 0, 1]
]

resultado = warshall(matriz)
for fila in resultado:
    print(fila)
