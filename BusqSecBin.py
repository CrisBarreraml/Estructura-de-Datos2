def busqueda_secuencial(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def ejecutar_busqueda_secuencial():
    print("--- 🔍 BÚSQUEDA SECUENCIAL ---")
    
    entrada = input("Ingresa una lista de números separados por comas: ")
    try:
        lista = list(map(int, entrada.strip().split(',')))
    except ValueError:
        print("Error: Ingresa solo números separados por comas.")
        return

    try:
        objetivo = int(input("Número a buscar: "))
    except ValueError:
        print("Error: Ingresa un número entero.")
        return

    posicion = busqueda_secuencial(lista, objetivo)

    if posicion != -1:
        print(f"✅ ¡Elemento encontrado en la posición {posicion}!")
    else:
        print("❌ Elemento no encontrado en la lista.")
    print("---------------------------------")

def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def ejecutar_busqueda_binaria():
    print("--- 🔍 BÚSQUEDA BINARIA ---")
    
    entrada = input("Ingresa una lista de números separados por comas: ")
    try:
        lista = list(map(int, entrada.strip().split(',')))
    except ValueError:
        print("Error: Ingresa solo números separados por comas.")
        return

    lista.sort()
    print(f"Lista ordenada: {lista}")

    try:
        objetivo = int(input("Número a buscar: "))
    except ValueError:
        print("Error: Ingresa un número entero.")
        return

    posicion = busqueda_binaria(lista, objetivo)

    if posicion != -1:
        print(f"✅ ¡Elemento encontrado en la posición {posicion}!")
    else:
        print("❌ Elemento no encontrado en la lista.")
    print("------------------------------")

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)
        print(f"\n✔ Insertado '{key}' en el índice {index}.\n")

    def search(self, key):
        index = self.hash_function(key)
        if key in self.table[index]:
            print(f"\n🔍 '{key}' encontrado en el índice {index}.\n")
            return True
        else:
            print(f"\n❌ '{key}' NO se encuentra en la tabla.\n")
            return False

    def delete(self, key):
        index = self.hash_function(key)
        if key in self.table[index]:
            self.table[index].remove(key)
            print(f"\n🗑 Eliminado '{key}' del índice {index}.\n")
            return True
        else:
            print(f"\n❌ No se puede eliminar; '{key}' no está en la tabla.\n")
            return False

    def show(self):
        print("\n======= Tabla Hash =======")
        for i, bucket in enumerate(self.table):
            print(f"Índice {i}: {bucket}")
        print("==========================\n")

def ejecutar_tabla_hash():
    print("--- ⚙️ GESTIÓN DE TABLA HASH ---")
    
    try:
        num_indices = int(input("Ingresa la cantidad de índices que tendrá la tabla: "))
    except ValueError:
        print("Error: Ingresa un número entero válido.")
        return
        
    hash_table = HashTable(num_indices)

    while True:
        print("""
======= MENÚ DE TABLA HASH =======
1. Insertar dato
2. Buscar dato
3. Eliminar dato
4. Mostrar tabla hash
5. Volver al menú principal
==================================
        """)

        opcion = input("Elige una opción: ")

        if opcion == "1":
            dato = input("Ingresa un dato a insertar: ")
            hash_table.insert(dato)

        elif opcion == "2":
            dato = input("Dato a buscar: ")
            hash_table.search(dato)

        elif opcion == "3":
            dato = input("Dato a eliminar: ")
            hash_table.delete(dato)

        elif opcion == "4":
            hash_table.show()

        elif opcion == "5":
            print("\nRegresando al menú principal.")
            break

        else:
            print("\nOpción no válida. Intenta de nuevo.\n")
    print("---------------------------------")


def menu_principal():
    while True:
        print("""
======================================
         MENU PRINCIPAL
======================================
1. Búsqueda Secuencial 
2. Búsqueda Binaria 
3. Tabla Hash 
4. Salir
======================================
        """)

        opcion_principal = input("Elige una opción: ")

        if opcion_principal == "1":
            ejecutar_busqueda_secuencial()

        elif opcion_principal == "2":
            ejecutar_busqueda_binaria()

        elif opcion_principal == "3":
            ejecutar_tabla_hash()

        elif opcion_principal == "4":
            print("\n¡Programa finalizado!")
            break

        else:
            print("\nOpción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu_principal()