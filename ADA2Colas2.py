from collections import deque

class Cola:
    def __init__(self):
        self.items = deque()
        self.contador = 0  
    def encolar(self, cliente):
        """Agrega un nuevo cliente con un número de turno."""
        self.contador += 1
        turno = f"{self.contador:03d}"
        self.items.append((turno, cliente))
        return turno

    def desencolar(self):
        """Atiende (elimina) al primer cliente de la cola."""
        if not self.esta_vacia():
            return self.items.popleft()
        else:
            return None

    def esta_vacia(self):
        return len(self.items) == 0

    def tamanio(self):
        return len(self.items)

    def ver_cola(self):
        return list(self.items)


def main():
    servicios = {
        1: {"nombre": "Atención General", "cola": Cola()},
        2: {"nombre": "Siniestros", "cola": Cola()},
        3: {"nombre": "Pagos", "cola": Cola()}
    }

    print("=== SISTEMA DE ATENCIÓN DE COMPAÑÍA DE SEGUROS ===")
    print("Servicios disponibles:")
    for num, datos in servicios.items():
        print(f"  {num} -> {datos['nombre']}")
    print("\nComandos:")
    print("  Cn -> Registrar llegada de cliente al servicio n (ejemplo: C1)")
    print("  An -> Atender cliente del servicio n (ejemplo: A2)")
    print("  V  -> Ver estado actual de todas las colas")
    print("  S  -> Salir del sistema\n")

    while True:
        comando = input("Ingrese comando: ").strip().upper()

        if comando == 'S':
            print("Saliendo del sistema... ¡Gracias por usar el sistema!")
            break

        elif comando == 'V':
            print("\n📋 Estado actual de las colas:")
            for num, datos in servicios.items():
                cola = datos["cola"]
                elementos = cola.ver_cola()
                if elementos:
                    print(f"  Servicio {num} - {datos['nombre']}:")
                    for turno, cliente in elementos:
                        print(f"    Turno {num}-{turno}: {cliente}")
                else:
                    print(f"  Servicio {num} - {datos['nombre']}: (sin clientes)")
            print()
            continue

        if len(comando) < 2:
            print("⚠️ Comando inválido. Ejemplo: C1 o A2.")
            continue

        letra = comando[0]
        try:
            numero_servicio = int(comando[1])
        except ValueError:
            print("⚠️ El número de servicio debe ser un entero (ejemplo: C1, A2).")
            continue

        if numero_servicio not in servicios:
            print(f"⚠️ El servicio {numero_servicio} no existe. Servicios válidos: 1, 2, 3.")
            continue

        servicio = servicios[numero_servicio]
        cola = servicio["cola"]

        if letra == 'C':
            cliente = input("Ingrese el nombre o descripción del cliente: ").strip()
            turno = cola.encolar(cliente)
            print(f"✅ Cliente '{cliente}' agregado al servicio {numero_servicio} ({servicio['nombre']}).")
            print(f"   Su número de atención es: {numero_servicio}-{turno}\n")

        elif letra == 'A':
            if cola.esta_vacia():
                print(f"⚠️ No hay clientes en la cola del servicio {numero_servicio} ({servicio['nombre']}).\n")
            else:
                turno, cliente = cola.desencolar()
                print(f"🎯 Atendiendo al cliente '{cliente}' (Turno {numero_servicio}-{turno})")
                print(f"   Servicio: {servicio['nombre']}\n")

        else:
            print("⚠️ Comando no reconocido. Use 'C' para cliente o 'A' para atender.\n")


if __name__ == "__main__":
    main()
