class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class MyLinkedList:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.longitud = 0
    
    def insertar_al_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.longitud += 1
    
    def insertar_al_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cola:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.longitud += 1
    
    def eliminar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior
                
                self.longitud -= 1
                return True
            actual = actual.siguiente
        return False
    
    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False
    
    def mostrar(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        return elementos
    
    def __iter__(self):
        self._iter_actual = self.cabeza
        return self
    
    def __next__(self):
        if self._iter_actual is None:
            raise StopIteration
        valor = self._iter_actual.valor
        self._iter_actual = self._iter_actual.siguiente
        return valor

if __name__ == "__main__":
    lista = MyLinkedList()
    while True:
        print("\nMenú:")
        print("1. Insertar al inicio")
        print("2. Insertar al final")
        print("3. Eliminar un valor")
        print("4. Buscar un valor")
        print("5. Mostrar la lista")
        print("6. Iterar sobre la lista")
        print("7. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            valor = int(input("Ingresa el valor a insertar al inicio: "))
            lista.insertar_al_inicio(valor)
            print(f"Valor {valor} insertado al inicio.")
        elif opcion == "2":
            valor = int(input("Ingresa el valor a insertar al final: "))
            lista.insertar_al_final(valor)
            print(f"Valor {valor} insertado al final.")
        elif opcion == "3":
            valor = int(input("Ingresa el valor a eliminar: "))
            if lista.eliminar(valor):
                print(f"Valor {valor} eliminado.")
            else:
                print(f"Valor {valor} no encontrado en la lista.")
        elif opcion == "4":
            valor = int(input("Ingresa el valor a buscar: "))
            encontrado = lista.buscar(valor)
            print(f"El valor {valor} {'se encuentra' if encontrado else 'no se encuentra'} en la lista.")
        elif opcion == "5":
            print("Lista actual:", lista.mostrar())
        elif opcion == "6":
            print("Iterando sobre la lista:")
            for elemento in lista:
                print(elemento, end=" -> ")
            print("None")
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
