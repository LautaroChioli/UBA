# Implementar una funci´on para conocer el estado de aprobaci´on de una materia a partir de las notas obtenidas
# por un/a alumno/a cumpliendo con la siguiente especificaci´on:
# problema resultadoMateria (in notas: seq⟨Z⟩) : Z {
# requiere: { |notas| > 0 }
# requiere: { Para todo i ∈ Z si 0 ≤ i < |notas| → 0 ≤ notas[i] ≤ 10) }
# asegura: { res = 1 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio es mayor o igual a 7 }
# asegura: { res = 2 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio est´a entre 4 (inclusive) y 7 }
# asegura: { res = 3 ↔ alguno de los elementos de notas es menor a 4 o el promedio es menor a 4 }


def resultadoMateria(notas: list) -> int:
    nota_materia: int = promedio(notas)
    if nota_materia >= 7 and todas_aprobadas(notas):
        return 1
    elif nota_materia >= 4 and todas_aprobadas(notas):
        return 2
    return 3
    

def suma(n: list) -> int:
    total: int = 0
    for i in n:
        total +=i
    return total

def promedio(notas: list) -> int:
    promedio: int = suma(notas)/len(notas)
    return promedio
def todas_aprobadas(notas: list) -> bool:
    for nota in notas:
        if nota < 4:
            return False
    return True
