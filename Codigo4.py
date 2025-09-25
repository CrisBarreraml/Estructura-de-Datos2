import random

A, B, C = None, None, None
longitud = 0

def llenar_vector():
    return [random.randint(-100, 100) for _ in range(longitud)]

def mostrar_vec(vector, nombre):
    print(f"\nVector {nombre}: {vector}")

def main():
    global A, B, C, longitud
    
    print("PROGRAMA DE OPERACIONES CON VECTORES")
    longitud = int(input("Longitud de los vectores: "))
    
    while True:
        print("\n" + "="*50)
        print("SELECCIONE UNA OPCIÓN")
        print("="*50)
        print("1. Llenar Vector A de manera aleatoria")
        print("2. Llenar Vector B de manera aleatoria")
        print("3. Realizar C = A + B")
        print("4. Realizar C = B - A")
        print("5. Mostrar Vector (A, B o C)")
        print("6. Salir")
        print("="*50)
        op = input("Opción: ")
        
        if op == "1":
            A = llenar_vector()
            mostrar_vec(A, "A")
        elif op == "2":
            B = llenar_vector()
            mostrar_vec(B, "B")
        elif op == "3":
            if A and B:
                C = [A[i] + B[i] for i in range(longitud)]
                mostrar_vec(C, "C")
            else:
                print("Primero llene A y B")
        elif op == "4":
            if A and B:
                C = [B[i] - A[i] for i in range(longitud)]
                mostrar_vec(C, "C")
            else:
                print("Primero llene A y B")
        elif op == "5":
            vec = input("Eliga el vector que desea ver: (A/B/C): ").upper()
            if vec == "A" and A: mostrar_vec(A, "A")
            elif vec == "B" and B: mostrar_vec(B, "B")
            elif vec == "C" and C: mostrar_vec(C, "C")
            else: print("Vector vacío o inválido")
        elif op == "6":
            print("¡Gracias por usar el programa!")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()