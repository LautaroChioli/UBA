# 1. problema pertenece a cada uno version 1 (in s:seq⟨seq⟨Z⟩⟩, in e:Z, out res: seq⟨Bool⟩) {
# requiere: { T rue }
# asegura: { |res| ≥ |s| }
# asegura: { Para todo i ∈ Z si 0 ≤ i < |s| → (res[i] = true ↔ pertenece(s[i], e)) }
# }
# Nota: Reutilizar la funci´on pertenece() implementada previamente para listas.

def pertenece(lista: list, n: int) -> bool:
    if n in lista:
        return True
    return False

def pertenece_n_a_matriz(matriz: list, n: int) -> list:
    lista_booleanos: list= []
    for columna in matriz:
        if pertenece(columna, n):
            lista_booleanos.append(True)
        else:
            lista_booleanos.append(False)
    return lista_booleanos