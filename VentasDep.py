class VentasDepartamentos:
    def __init__(self):
        self.departamentos = ["Ropa", "Deportes", "Juguetería"]
        self.meses = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]
        self.ventas = [[0] * len(self.meses) for _ in range(len(self.departamentos))]

    def insertar_venta(self, depto, mes, valor):
        self.ventas[depto][mes] = valor

    def buscar_venta(self, depto, mes):
        return self.ventas[depto][mes]

    def eliminar_venta(self, depto, mes):
        self.ventas[depto][mes] = 0  

    def mostrar_ventas(self):
        for i, depto in enumerate(self.departamentos):
            print(f"Departamento: {depto}")
            for j, mes in enumerate(self.meses):
                print(f"  {mes}: {self.ventas[i][j]}")
        print()

ventas = VentasDepartamentos()
ventas.insertar_venta(0, 0, 5000)  
ventas.insertar_venta(1, 2, 7000)  

print("Venta en Ropa - Enero:", ventas.buscar_venta(0, 0))

ventas.eliminar_venta(1, 2) 

ventas.mostrar_ventas()
