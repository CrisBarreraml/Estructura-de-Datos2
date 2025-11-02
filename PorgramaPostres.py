POSTRES = {
    "Brownie": ["Chocolate", "Harina", "Azúcar", "Nueces"],
    "Cheesecake": ["Queso crema", "Galletas", "Azúcar", "Huevos", "Queso crema"],
    "Pastel de Zanahoria": ["Zanahoria", "Harina", "Azúcar", "Nueces", "Canela", "Harina"],
    "Tiramisú": ["Café", "Queso Mascarpone", "Bizcochos", "Cacao", "Café"]
}

def mostrar_ingredientes(postre):

    if postre in POSTRES:
        print(f"Ingredientes de {postre}: {POSTRES[postre]}")
    else:
        print(f"El postre '{postre}' no existe.")

def agregar_ingrediente(postre, ingrediente):

    if postre in POSTRES:
        POSTRES[postre].append(ingrediente)
        print(f"Se agregó '{ingrediente}' a {postre}.")
    else:
        print(f"El postre '{postre}' no existe.")

def eliminar_ingrediente(postre, ingrediente):

    if postre in POSTRES:
        if ingrediente in POSTRES[postre]:
            POSTRES[postre].remove(ingrediente)
            print(f"Se eliminó '{ingrediente}' de {postre}.")
        else:
            print(f"El ingrediente '{ingrediente}' no existe en {postre}.")
    else:
        print(f"El postre '{postre}' no existe.")

def agregar_postre(postre, ingredientes):

    if postre not in POSTRES:
        POSTRES[postre] = ingredientes
        print(f"Se agregó el postre '{postre}' con ingredientes: {ingredientes}")
    else:
        print(f"El postre '{postre}' ya existe.")

def eliminar_postre(postre):

    if postre in POSTRES:
        del POSTRES[postre]
        print(f"Se eliminó el postre '{postre}'.")
    else:
        print(f"El postre '{postre}' no existe.")

def eliminar_repetidos_postres(diccionario):
    for postre, ingredientes in diccionario.items():
        diccionario[postre] = list(set(ingredientes))

while True:
    print("\n--- Menú de Postres ---")
    print("1. Mostrar ingredientes de un postre")
    print("2. Agregar ingrediente a un postre")
    print("3. Eliminar ingrediente de un postre")
    print("4. Agregar postre")
    print("5. Eliminar postre")
    print("6. Eliminar ingredientes repetidos")
    print("7. Mostrar todos los postres")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        postre = input("Ingrese el nombre del postre: ")
        mostrar_ingredientes(postre)
    elif opcion == "2":
        postre = input("Ingrese el nombre del postre: ")
        ingrediente = input("Ingrese el ingrediente a agregar: ")
        agregar_ingrediente(postre, ingrediente)
    elif opcion == "3":
        postre = input("Ingrese el nombre del postre: ")
        ingrediente = input("Ingrese el ingrediente a eliminar: ")
        eliminar_ingrediente(postre, ingrediente)
    elif opcion == "4":
        postre = input("Ingrese el nombre del postre: ")
        ingredientes_str = input("Ingrese los ingredientes separados por comas: ")
        ingredientes = [ingrediente.strip() for ingrediente in ingredientes_str.split(",")]
        agregar_postre(postre, ingredientes)
    elif opcion == "5":
        postre = input("Ingrese el nombre del postre a eliminar: ")
        eliminar_postre(postre)
    elif opcion == "6":
        eliminar_repetidos_postres(POSTRES)
        print("Ingredientes repetidos eliminados.")
    elif opcion == "7":
        print(POSTRES)
    elif opcion == "0":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente de nuevo.")