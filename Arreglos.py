import random
import json
import os

def guardar_datos(nombre_archivo, alumnos, materias, matriz):
    datos = {
        "num_alumnos": alumnos,
        "num_materias": materias,
        "calificaciones": matriz
    }
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo)
    print(f"Datos guardados correctamente en '{nombre_archivo}'.")

def cargar_datos(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        print("Datos cargados correctamente.")
        return datos["num_alumnos"], datos["num_materias"], datos["calificaciones"]
    except FileNotFoundError:
        print("El archivo no existe.")
        return None, None, None
    except (KeyError, json.JSONDecodeError):
        print("El archivo está corrupto o no tiene el formato esperado.")
        return None, None, None

def mostrar_todos(matriz):
    """
    Muestra todos los alumnos con todas sus materias.
    """
    if matriz is None:
        print("(Sin datos para mostrar)")
        return
    num_alumnos = len(matriz)
    num_materias = len(matriz[0]) if num_alumnos > 0 else 0
    titulos_materias = [f"M{i+1}" for i in range(num_materias)]
    print("Alumno\t" + "\t".join(titulos_materias))
    for i, fila in enumerate(matriz, start=1):
        print(f"A{i}\t" + "\t".join(map(str, fila)))

def buscar_valor(matriz, alumno, materia):
    if matriz is None:
        return None, "No hay matriz cargada. Primero introduce o carga datos."
    num_alumnos = len(matriz)
    num_materias = len(matriz[0]) if num_alumnos > 0 else 0

    if not (1 <= alumno <= num_alumnos):
        return None, f"Alumno {alumno} fuera de rango. Debe estar entre 1 y {num_alumnos}."
    if not (1 <= materia <= num_materias):
        return None, f"Materia {materia} fuera de rango. Debe estar entre 1 y {num_materias}."

    return matriz[alumno-1][materia-1], None

def menu():
    num_alumnos = None
    num_materias = None
    matriz = None

    while True:
        print("\nMenú:")
        print("1. Introducir datos (generar aleatorio)")
        print("2. Guardar datos a archivo")
        print("3. Cargar datos desde archivo")
        print("4. Buscar alumno y materia específicos")
        print("5. Mostrar todos los alumnos y materias")
        print("6. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            try:
                num_alumnos = int(input("Ingrese el número de alumnos: "))
                num_materias = int(input("Ingrese el número de materias: "))
                if num_alumnos <= 0 or num_materias <= 0:
                    print("Los números deben ser positivos.")
                    num_alumnos = num_materias = None
                    continue
            except ValueError:
                print("Entrada inválida. Ingrese enteros válidos.")
                num_alumnos = num_materias = None
                continue

            matriz = [[random.randint(0, 100) for _ in range(num_materias)] for _ in range(num_alumnos)]
            print("\nMatriz generada:")
            mostrar_todos(matriz)

        elif opcion == "2":
            if matriz is None:
                print("No hay datos para guardar. Primero introduce o carga datos.")
                continue
            nombre_archivo = input("Ingrese el nombre del archivo para guardar (ej. datos.json): ").strip()
            if not nombre_archivo:
                print("Nombre de archivo no válido.")
                continue
            if not os.path.splitext(nombre_archivo)[1]:
                nombre_archivo += ".json"
            guardar_datos(nombre_archivo, num_alumnos, num_materias, matriz)

        elif opcion == "3":
            nombre_archivo = input("Ingrese el nombre del archivo a cargar (ej. datos.json): ").strip()
            if not nombre_archivo:
                print("Nombre de archivo no válido.")
                continue
            if not os.path.splitext(nombre_archivo)[1] and os.path.exists(nombre_archivo + ".json"):
                nombre_archivo = nombre_archivo + ".json"
            num_alumnos, num_materias, matriz = cargar_datos(nombre_archivo)
            if num_alumnos and num_materias and matriz is not None:
                print("\nResultados de Calificaciones:")
                mostrar_todos(matriz)

        elif opcion == "4":
            if matriz is None:
                print("No hay datos cargados. Primero introduce o carga datos.")
                continue
            try:
                alumno = int(input("Ingrese el número del alumno (1-based): "))
                materia = int(input("Ingrese el número de la materia (1-based): "))
            except ValueError:
                print("Entrada inválida. Debe ingresar enteros.")
                continue

            valor, error = buscar_valor(matriz, alumno, materia)
            if error:
                print("Error:", error)
            else:
                print(f"Calificación -> Alumno {alumno}, Materia {materia} : {valor}")

        elif opcion == "5":
            print("\nLista completa de alumnos y materias:")
            mostrar_todos(matriz)

        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
