def crear_arreglos():
    n = int(input("¿Cuántos nombres deseas ingresar? "))

    nombres = []
    longitudes = []

    for i in range(n):
        nombre = input(f"Introduce el nombre {i+1}: ")
        nombres.append(nombre)
        longitudes.append(len(nombre))

    return nombres, longitudes


def mostrar_arreglos(nombres, longitudes):
    print("\n--- Nombres y sus longitudes ---")
    for i in range(len(nombres)):
        print(f"{nombres[i]} → {longitudes[i]} caracteres")


nombres, longitudes = crear_arreglos()
mostrar_arreglos(nombres, longitudes)