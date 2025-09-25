def a_binario(n: int) -> str:
    """Devuelve la representación binaria de n usando recursión.
       n debe ser un entero >= 0.
    """
    if n == 0:
        return "0"
    def rec(x: int) -> str:
        if x == 0:
            return ""
        return rec(x // 2) + str(x % 2)
    return rec(n)

def pedir_entero_no_negativo(prompt: str = "Introduce un entero no negativo: ") -> int:
    while True:
        try:
            val = int(input(prompt))
            if val >= 0:
                return val
            print("Por favor introduce un número entero mayor o igual a 0.")
        except ValueError:
            print("Entrada inválida. Introduce un número entero.")

if __name__ == "__main__":
    n = pedir_entero_no_negativo("Introduce un número entero positivo (puede ser 0): ")
    print(f"El número {n} en binario es: {a_binario(n)}")
