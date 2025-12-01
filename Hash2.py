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



print("=== Configuración de la Tabla Hash ===")
num_indices = int(input("Ingresa la cantidad de índices que tendrá la tabla: "))
hash_table = HashTable(num_indices)

while True:
    print("""
========== MENÚ ==========
1. Insertar dato
2. Buscar dato
3. Eliminar dato
4. Mostrar tabla hash
5. Salir
==========================
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
        print("\n¡Programa finalizado!")
        break

    else:
        print("\nOpción no válida. Intenta de nuevo.\n")
