def floyd(grafo):
    nodos = list(grafo.keys())
    dist = {u: {v: float('inf') for v in nodos} for u in nodos}

    for u in nodos:
        dist[u][u] = 0
        for v in grafo[u]:
            dist[u][v] = grafo[u][v]

    for k in nodos:
        for i in nodos:
            for j in nodos:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

grafo = {
    'A': {'B': 3, 'C': 8},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {'A': 2}
}

print(floyd(grafo))
