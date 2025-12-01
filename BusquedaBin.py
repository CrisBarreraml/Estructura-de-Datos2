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

def main():
    print("🔍 BÚSQUEDA BINARIA")
    
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

if __name__ == "__main__":
    main()
