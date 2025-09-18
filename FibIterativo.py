def fibonacci_interactivo():
    while True:
        try:
            n = int(input("Ingrese un número para la secuencia de Fibonacci (o -1 para salir): "))
            if n == -1:
                print("Saliendo del programa...")
                break
            elif n < 0:
                print("Por favor, ingrese un número positivo.")
                continue
 
            a, b = 0, 1
            print("Secuencia de Fibonacci:")
            for _ in range(n):
                print(a, end=" ")
                a, b = b, a + b
            print("\n")
        except ValueError:
            print("Entrada inválida. Ingrese un número entero válido.")
 
fibonacci_interactivo()
 