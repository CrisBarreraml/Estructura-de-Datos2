def busqueda_secuencial(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def main():
    print("🔍 BÚSQUEDA SECUENCIAL")
    
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

if __name__ == "__main__":
    main()
