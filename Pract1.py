import time

class Pila:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.items = [None] * capacidad  
        self.tope = 0  

    def insertar(self, valor):
        print(f"\nOperación: Insertar (PILA, {valor})")
        if self.tope < self.capacidad:
            self.items[self.tope] = valor
            self.tope += 1
            print(f"Elemento '{valor}' insertado en la pila.")
        else:
            print(f"Error: La pila está llena. No se puede insertar '{valor}'.")
        self.mostrar_estado()

    def eliminar(self, etiqueta):
        print(f"\nOperación: Eliminar (PILA, {etiqueta})")
        if self.tope > 0:
            self.tope -= 1
            valor_eliminado = self.items[self.tope]
            self.items[self.tope] = None
            print(f"Elemento '{valor_eliminado}' eliminado de la pila.")
        else:
            print(f"Error: La pila está vacía. No se puede eliminar '{etiqueta}'.")
        self.mostrar_estado()

    def mostrar_estado(self):
        print("\nEstado actual de la pila:")
        for i in range(self.capacidad - 1, -1, -1):
            if i < self.tope:
                print(f"|  {self.items[i]}  | <- posición {i + 1}")
            else:
                print("|      |")
        print("+------+")
        print(f"TOPE = {self.tope} (Cantidad de elementos en la pila)\n")
        time.sleep(1)

pila = Pila(capacidad=8)

pila.insertar('X')

pila.insertar('Y')

pila.eliminar('Z')

pila.eliminar('T')

pila.eliminar('U')

pila.insertar('V')

pila.insertar('W')

pila.eliminar('p')

pila.insertar('R')

print("\nTodas las operaciones han sido realizadas.")
