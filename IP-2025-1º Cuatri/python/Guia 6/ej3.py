def alguno_es_0(n: int, m: int) -> bool:
    return (n == 0 or m == 0)

def ambos_son_0(n: int, m: int) -> bool:
    return (n == 0 and m == 0)

def es_largo(palabra: str) -> bool:
    return (len(palabra) >= 3 and len(palabra) <= 8)

def es_bisiesto(año: int) -> bool:
    return (año % 400 == 0 or (año % 4 == 0 and not año % 100 == 0))