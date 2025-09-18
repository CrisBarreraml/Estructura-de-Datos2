def fibonacci_recursivo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)
 
n = int(input("Ingrese un número para la secuencia de Fibonacci: "))
for i in range(n):
    print(fibonacci_recursivo(i), end=" ")

    