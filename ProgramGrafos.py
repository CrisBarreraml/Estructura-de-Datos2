import math
import tkinter as tk

def resolver_problema_estados_sin_librerias():

    estados = ["CDMX", "Morelos", "Puebla", "Veracruz", "Oaxaca", "Guerrero", "Michoacán"]
    relaciones = {
        ("CDMX", "Morelos"): 80,
        ("CDMX", "Puebla"): 130,
        ("Morelos", "Puebla"): 90,
        ("Morelos", "Guerrero"): 250,
        ("Puebla", "Veracruz"): 280,
        ("Puebla", "Oaxaca"): 350,
        ("Veracruz", "Oaxaca"): 200,
        ("Oaxaca", "Guerrero"): 400,
        ("Guerrero", "Michoacán"): 380,
        ("Michoacán", "CDMX"): 300,
    }

    print("Estados:")
    print(estados)
    print("\nRelaciones (Estado1, Estado2, Costo):")
    for (u, v), peso in relaciones.items():
        print(f"{u} - {v}: {peso}")

    print("\nRecorrido sin repeticiones (aproximación):")
    camino_sin_repeticiones = buscar_camino_hamiltoniano(estados, relaciones)
    if camino_sin_repeticiones:
        costo_sin_repeticiones = calcular_costo_camino(camino_sin_repeticiones, relaciones)
        print(" -> ".join(camino_sin_repeticiones))
        print(f"Costo total: {costo_sin_repeticiones}")
    else:
        print("No se encontró un camino sin repeticiones (aproximación simple).")

    print("\nRecorrido con repeticiones (aproximación):")
    camino_con_repeticiones = buscar_ciclo_euleriano_aproximado(estados, relaciones)
    if camino_con_repeticiones:
        costo_con_repeticiones = calcular_costo_camino(camino_con_repeticiones, relaciones, ciclo=True)
        print(" -> ".join(camino_con_repeticiones))
        print(f"Costo total: {costo_con_repeticiones}")
    else:
        print("No se encontró un camino con repeticiones (aproximación simple).")

    grafica_grafo(estados, relaciones, titulo="Mapa de estados (grafo)")


def buscar_camino_hamiltoniano(estados, relaciones):
    camino = [estados[0]]
    estados_restantes = estados[1:]
    while estados_restantes:
        ultimo_estado = camino[-1]
        mejor_estado_siguiente = None
        mejor_costo = float('inf')
        for estado_siguiente in estados_restantes:
            if (ultimo_estado, estado_siguiente) in relaciones:
                costo = relaciones[(ultimo_estado, estado_siguiente)]
                if costo < mejor_costo:
                    mejor_costo = costo
                    mejor_estado_siguiente = estado_siguiente
        if mejor_estado_siguiente:
            camino.append(mejor_estado_siguiente)
            estados_restantes.remove(mejor_estado_siguiente)
        else:
            return None  
    return camino

def buscar_ciclo_euleriano_aproximado(estados, relaciones):
    """Busca un ciclo euleriano aproximado."""
    camino = buscar_camino_hamiltoniano(estados, relaciones)
    if camino:
        camino.append(camino[0])  
        return camino
    else:
        return None

def calcular_costo_camino(camino, relaciones, ciclo=False):
    """Calcula el costo total de un camino."""
    costo_total = 0
    for i in range(len(camino) - 1):
        u, v = camino[i], camino[i + 1]
        if (u, v) in relaciones:
            costo_total += relaciones[(u, v)]
        elif (v,u) in relaciones:
            costo_total += relaciones[(v,u)]
        else:
            return float('inf')  
    if ciclo and camino:
        u, v = camino[-1], camino[0]
        if (u,v) in relaciones:
            costo_total += relaciones[(u,v)]
        elif (v,u) in relaciones:
            costo_total += relaciones[(v,u)]
        else:
            return float('inf')

    return costo_total

def grafica_grafo(estados, relaciones, titulo="Grafo"):
    
    root = tk.Tk()
    root.title(titulo)
    W, H = 900, 700
    canvas = tk.Canvas(root, width=W, height=H, bg='white')
    canvas.pack(fill=tk.BOTH, expand=True)

    n = len(estados)
    if n == 0:
        canvas.create_text(W//2, H//2, text="Grafo vacío", font=("Arial", 20))
        root.mainloop()
        return

    radius = min(W, H) // 3
    cx, cy = W//2, H//2
    pos = {}
    for i, estado in enumerate(estados):
        angle = 2 * math.pi * i / n
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
        pos[estado] = (x, y)

    dibujadas = set()
    for (u, v), peso in relaciones.items():
        par_norm = tuple(sorted((u, v)))
        if par_norm in dibujadas:
            continue
        peso_mostrar = None
        if (u, v) in relaciones:
            peso_mostrar = relaciones[(u, v)]
        elif (v, u) in relaciones:
            peso_mostrar = relaciones[(v, u)]
        x1, y1 = pos[u]
        x2, y2 = pos[v]
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        dx, dy = x2 - x1, y2 - y1
        dist = math.hypot(dx, dy)
        if dist == 0:
            ctrlx, ctrly = mx, my - 20
        else:
            ux, uy = dx / dist, dy / dist
            px, py = -uy, ux
            offset = 15  
            ctrlx, ctrly = mx + px * offset, my + py * offset

        canvas.create_line(x1, y1, ctrlx, ctrly, x2, y2, smooth=True, width=2)
        label_x = (mx + ctrlx) / 2
        label_y = (my + ctrly) / 2
        if peso_mostrar is not None:
            canvas.create_text(label_x, label_y - 10, text=str(peso_mostrar), font=("Arial", 10, "bold"))

        dibujadas.add(par_norm)

    node_r = 26
    for estado in estados:
        x, y = pos[estado]
        canvas.create_oval(x - node_r, y - node_r, x + node_r, y + node_r, fill='lightblue', outline='black')
        canvas.create_text(x, y, text=estado, font=("Arial", 10, "bold"))

    canvas.create_text(80, 20, text="Nodos: estados (ubicados en círculo). Aristas: conexiones con costo (peso).", anchor='w', font=("Arial", 9))

    root.mainloop()

resolver_problema_estados_sin_librerias()
