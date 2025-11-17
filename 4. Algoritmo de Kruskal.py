def kruskal(nodos, aristas):
    parent = {nodo: nodo for nodo in nodos}

    def find(nodo):
        if parent[nodo] != nodo:
            parent[nodo] = find(parent[nodo])
        return parent[nodo]

    def union(nodo1, nodo2):
        raiz1 = find(nodo1)
        raiz2 = find(nodo2)
        if raiz1 != raiz2:
            parent[raiz2] = raiz1
            return True
        return False

    aristas.sort(key=lambda x: x[2])  
    mst = []

    for u, v, peso in aristas:
        if union(u, v):
            mst.append((u, v, peso))

    return mst

nodos = ['A', 'B', 'C', 'D']
aristas = [
    ('A', 'B', 1),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 5),
    ('C', 'D', 4)
]

print(kruskal(nodos, aristas))
