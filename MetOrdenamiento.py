import random
import time
from typing import List, Tuple

N = 1000               
MIN_VAL, MAX_VAL = 0, 9999
SNAPSHOT_EVERY = 50    
SHOW_FIRST = 20       
FULL_TRACE = False     

def generar_lista(n: int, lo: int, hi: int) -> List[int]:
    return [random.randint(lo, hi) for _ in range(n)]

def resumen_lista(lst: List[int], take: int = SHOW_FIRST) -> str:
    return f"[{', '.join(str(x) for x in lst[:take])}" + (", ...]" if len(lst) > take else "]")

def open_trace_file(name: str):
    if FULL_TRACE:
        return open(name, "w", encoding="utf-8")
    return None

def close_trace_file(f):
    if f:
        f.close()

def trace_write(f, s: str):
    if f:
        f.write(s + "\n")

def burbuja_trazado(arr: List[int]) -> Tuple[List[int], dict]:
    n = len(arr)
    a = arr[:]  
    comparisons = 0
    swaps = 0
    start = time.time()
    trace_f = open_trace_file("trace_burbuja.txt")
    print("\n=== BURBUJA ===")
    print(f"Tamaño: {n}. Muestra inicio: {resumen_lista(a)}")
    trace_write(trace_f, f"Inicio lista: {a}")

    detailed_on_screen = (n <= 50) and not FULL_TRACE

    for i in range(n - 1):
        pass_swaps = 0
        trace_write(trace_f, f"-- Pase {i+1} --")
        if i % SNAPSHOT_EVERY == 0:
            print(f"Pase {i+1}: (estado parcial) {resumen_lista(a)}")
        for j in range(n - 1 - i):
            comparisons += 1
            if detailed_on_screen:
                print(f"Comparando a[{j}]={a[j]} y a[{j+1}]={a[j+1]}")
            trace_write(trace_f, f"Comparar indices {j},{j+1}: {a[j]} vs {a[j+1]}")
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                pass_swaps += 1
                trace_write(trace_f, f" Swap -> lista parcial: {a}")
                if detailed_on_screen:
                    print(f"  Swap -> {a[j]} <-> {a[j+1]}")
        print(f"Fin pase {i+1}: swaps en este pase = {pass_swaps}")
        trace_write(trace_f, f"Fin pase {i+1}, swaps_pase={pass_swaps}")
        if pass_swaps == 0:
            print(f"Sin swaps en pase {i+1} -> la lista ya está ordenada (parada anticipada).")
            trace_write(trace_f, f"Parada anticipada en pase {i+1}")
            break

    elapsed = time.time() - start
    print(f"Burbuja terminado: comparaciones={comparisons}, swaps={swaps}, tiempo={elapsed:.4f}s")
    trace_write(trace_f, f"Resultado final: {a}")
    trace_write(trace_f, f"Stats: comps={comparisons}, swaps={swaps}, time={elapsed:.4f}")
    close_trace_file(trace_f)
    return a, {"comparisons": comparisons, "swaps": swaps, "time_s": elapsed}


def insercion_trazado(arr: List[int]) -> Tuple[List[int], dict]:
    a = arr[:]
    n = len(a)
    comparisons = 0
    shifts = 0  
    start = time.time()
    trace_f = open_trace_file("trace_insercion.txt")
    print("\n=== INSERCIÓN ===")
    print(f"Tamaño: {n}. Muestra inicio: {resumen_lista(a)}")
    trace_write(trace_f, f"Inicio lista: {a}")

    detailed_on_screen = (n <= 50) and not FULL_TRACE

    for i in range(1, n):
        key = a[i]
        j = i - 1
        if i % SNAPSHOT_EVERY == 0:
            print(f"Pivote i={i}, key={key} (muestra estado): {resumen_lista(a)}")
        trace_write(trace_f, f"-- Inserción i={i}, key={key} --")
        if detailed_on_screen:
            print(f"Tomando key a[{i}]={key}")
        moved_this_i = 0
        while j >= 0:
            comparisons += 1
            trace_write(trace_f, f"Comparar key {key} con a[{j}]={a[j]}")
            if a[j] > key:
                a[j + 1] = a[j]
                shifts += 1
                moved_this_i += 1
                trace_write(trace_f, f" Shift: movido {a[j]} a pos {j+1}")
                j -= 1
            else:
                break
        a[j + 1] = key
        trace_write(trace_f, f"Insertar key en pos {j+1}, lista parcial: {a}")
        if detailed_on_screen:
            print(f"Insertada key en pos {j+1}")
        print(f"i={i}: movidos={moved_this_i}")
    elapsed = time.time() - start
    print(f"Inserción terminado: comparaciones={comparisons}, shifts={shifts}, tiempo={elapsed:.4f}s")
    trace_write(trace_f, f"Resultado final: {a}")
    trace_write(trace_f, f"Stats: comps={comparisons}, shifts={shifts}, time={elapsed:.4f}")
    close_trace_file(trace_f)
    return a, {"comparisons": comparisons, "shifts": shifts, "time_s": elapsed}


def seleccion_trazado(arr: List[int]) -> Tuple[List[int], dict]:
    a = arr[:]
    n = len(a)
    comparisons = 0
    swaps = 0
    start = time.time()
    trace_f = open_trace_file("trace_seleccion.txt")
    print("\n=== SELECCIÓN ===")
    print(f"Tamaño: {n}. Muestra inicio: {resumen_lista(a)}")
    trace_write(trace_f, f"Inicio lista: {a}")

    detailed_on_screen = (n <= 50) and not FULL_TRACE

    for i in range(n):
        min_idx = i
        if i % SNAPSHOT_EVERY == 0:
            print(f"Pase {i+1}: buscando mínimo para la posición {i} (muestra: {resumen_lista(a)})")
        trace_write(trace_f, f"-- Pase {i+1} --")
        for j in range(i + 1, n):
            comparisons += 1
            trace_write(trace_f, f"Comparar a[{j}]={a[j]} con a[{min_idx}]={a[min_idx]}")
            if a[j] < a[min_idx]:
                min_idx = j
                trace_write(trace_f, f" Nuevo min_idx={min_idx} (valor {a[min_idx]})")
                if detailed_on_screen:
                    print(f" Nuevo min_idx={min_idx} valor={a[min_idx]}")
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swaps += 1
            trace_write(trace_f, f" Swap pos {i}<->{min_idx} -> lista parcial: {a}")
            print(f"Pase {i+1}: swap pos {i} <-> {min_idx}")
        else:
            trace_write(trace_f, f" No swap necesario en pase {i+1}")
            print(f"Pase {i+1}: no swap (elemento ya es mínimo)")
    elapsed = time.time() - start
    print(f"Selección terminado: comparaciones={comparisons}, swaps={swaps}, tiempo={elapsed:.4f}s")
    trace_write(trace_f, f"Resultado final: {a}")
    trace_write(trace_f, f"Stats: comps={comparisons}, swaps={swaps}, time={elapsed:.4f}")
    close_trace_file(trace_f)
    return a, {"comparisons": comparisons, "swaps": swaps, "time_s": elapsed}


def main():
    print("Generando lista aleatoria de", N, "elementos...")
    lista = generar_lista(N, MIN_VAL, MAX_VAL)
    print("Lista generada. Muestra inicial:", resumen_lista(lista))
    if FULL_TRACE:
        print("FULL_TRACE=True -> se generarán archivos trace_*.txt con cada comparación/swap (pueden ser muy pesados).")

    sorted_burbuja, stats_burbuja = burbuja_trazado(lista)

    sorted_insercion, stats_insercion = insercion_trazado(lista)

    sorted_seleccion, stats_seleccion = seleccion_trazado(lista)

    print("\n=== RESUMEN FINAL ===")
    print("Muestra original:", resumen_lista(lista))
    print("Burbuja (muestra final):", resumen_lista(sorted_burbuja))
    print("Inserción (muestra final):", resumen_lista(sorted_insercion))
    print("Selección (muestra final):", resumen_lista(sorted_seleccion))
    print("\nStats burbuja:", stats_burbuja)
    print("Stats inserción:", stats_insercion)
    print("Stats selección:", stats_seleccion)

    assert sorted_burbuja == sorted_insercion == sorted_seleccion == sorted(lista), \
        "Error: los algoritmos no producen el mismo resultado!"
    print("\nVerificación: todas las salidas coinciden y están ordenadas.")

if __name__ == "__main__":
    main()
