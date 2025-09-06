
def main():
    calificaciones = [0] * 5  

    for i in range(5):
        calificaciones[i] = int(input(f"Captura la {i+1} calificación: "))

    print("\nCalificaciones capturadas:")
    for i, cal in enumerate(calificaciones, start=1):
        print(f"Calificación {i}: {cal}")


if __name__ == "__main__":
    main()
