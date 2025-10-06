from collections import deque

class Cola:
    def __init__(self):
        self.items = deque()

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.popleft()
        return None

    def tamanio(self):
        return len(self.items)

    def ver_elementos(self):
        return list(self.items)


def sumar_colas(colaA, colaB):
    cola_resultado = Cola()
    listaA = colaA.ver_elementos()
    listaB = colaB.ver_elementos()

    longitud = min(len(listaA), len(listaB))

    for i in range(longitud):
        suma = listaA[i] + listaB[i]
        cola_resultado.encolar(suma)

    return cola_resultado


colaA = Cola()
colaB = Cola()

for n in [3, 4, 2, 8, 12, 45, 68]:
    colaA.encolar(n)

for n in [6, 2, 9, 11, 3, 35, 98]:
    colaB.encolar(n)

cola_resultado = sumar_colas(colaA, colaB)

print(f"{'Cola A':<10}{'Cola B':<10}{'Cola Resultado'}")
print("-" * 35)
for a, b, r in zip(colaA.ver_elementos(), colaB.ver_elementos(), cola_resultado.ver_elementos()):
    print(f"{a:<10}{b:<10}{r}")
