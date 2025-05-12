import math

def imprime_saludo(nombre: str) -> str:
    return f"Hola, {nombre}."

def raiz_de_n(numero: int) -> float:
    return math.sqrt(numero)

def farenheit_a_celsius(f: float) -> float:
    return ((f - 32)*5)/9

def imprimir_dos_veces(palabra: str) -> str:
    return palabra*2

def es_multiplo_de(n: int, m: int) -> bool:
    if (n % m) == 0:
        return True
    else:
        return False

def es_par(n: int) -> bool:
    if es_multiplo_de(n, 2) == True:
        return True
    else:
        return False
    
def cantidad_de_pizzas(personas: int, min_porciones: int) -> int:
    total_porciones = personas*min_porciones
    return math.ceil(total_porciones/8)
