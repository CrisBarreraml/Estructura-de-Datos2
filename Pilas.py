class Pila:
    def __init__(self):
        self.elementos = []

    def esta_vacia(self):
        return len(self.elementos) == 0

    def apilar(self, dato):
        self.elementos.append(dato)
        print(f"Se apiló: {dato}")

    def desapilar(self):
        if self.esta_vacia():
            print("La pila está vacía, no se puede desapilar.")
            return None
        return self.elementos.pop()

    def ver_tope(self):
        if self.esta_vacia():
            print("La pila está vacía.")
            return None
        return self.elementos[-1]

    def mostrar(self):
        if self.esta_vacia():
            print("La pila está vacía.")
        else:
            print("Contenido de la pila (de arriba hacia abajo):")
            for elemento in reversed(self.elementos):
                print(elemento)


if __name__ == "__main__":
    pila = Pila()

    while True:
        print("\n--- Menú de opciones ---")
        print("1. Apilar (push)")
        print("2. Desapilar (pop)")
        print("3. Ver tope")
        print("4. Mostrar pila")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            dato = input("Ingresa un valor para apilar: ")
            pila.apilar(dato)
        elif opcion == "2":
            desapilado = pila.desapilar()
            if desapilado is not None:
                print(f"Se desapiló: {desapilado}")
        elif opcion == "3":
            tope = pila.ver_tope()
            if tope is not None:
                print(f"El tope de la pila es: {tope}")
        elif opcion == "4":
            pila.mostrar()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
