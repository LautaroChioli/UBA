# 1. problema es matriz (in s:seq⟨seq⟨Z⟩⟩) : Bool {
# requiere: { T rue }
# asegura: { res = true ↔ (|s| > 0) ∧ (|s[0]| > 0) ∧ (Para todo i ∈ Z si 0 ≤ i < |s| → |s[i]| = |s[0]|) }
# }

def es_matriz(s: list) -> bool:
    len_s0 : int = len(s[0])
    for fila in s:
        if len(fila) != len_s0:
            return False
    return True
        

# 2. problema filas ordenadas (in m:seq⟨seq⟨Z⟩⟩, out res: seq⟨Bool⟩) {
# requiere: { esM atriz(m) }
# asegura: { Para todo i ∈ Z si 0 ≤ i < |res| → (res[i] = true ↔ ordenados(s[i])) }
# }
# Nota: Reutilizar la funci´on ordenados() implementada previamente para listas

def ordenados(lista: list) -> bool:
    actual = 0
    for i in lista:
        if actual > i:
            return False
        actual = i
    return True
    
def filas_ordenadas(matriz: list) -> list:
    lista_booleanos: list= []
    for fila in matriz:
        if ordenados(fila):
            lista_booleanos.append(True)
        else:
            lista_booleanos.append(False)
    return lista_booleanos


# 3. problema columna (in m:seq⟨seq⟨Z⟩⟩, in c: Z) : seq⟨Z⟩ {
# requiere: { esM atriz(m) }
# requiere: { c < |m[0]| }
# requiere: { c ≥ 0 }
# asegura: { Devuelve una secuencia con exactamente los mismos elementos de la columna c de la matriz m, en
# el mismo orden que aparecen }
# }

def columna(matriz: list, columna: int) -> list:
    columna_n = []
    for fila in matriz:
        columna_n.append(fila[columna])
    return columna_n

# 4. problema columnas ordenadas (in m:seq⟨seq⟨Z⟩⟩) : seq⟨Bool⟩ {
# requiere: { esM atriz(m) }
# asegura: { Para toda columna c ∈ m → (res[c] = true ↔ ordenados(columna(m, c))) }
# }
# Nota: Reutilizar la funci´on ordenados() implementada previamente para listas

def columnas(matriz: list,):
    columnas = []
    for i in range(0, len(matriz[0])):
        columnas.append(columna(matriz, i))
    return columnas
        

def columnas_ordenadas(matriz: list) -> list:
    lista_booleanos: list = []
    for clmna in columnas(matriz):
        if ordenados(clmna):
            lista_booleanos.append(True)
        else:
            lista_booleanos.append(False)
    return lista_booleanos

# 5. problema transponer (in m:seq⟨seq⟨Z⟩⟩) : seq⟨seq⟨Z⟩⟩ {
# requiere: { esM atriz(m) }
# asegura: { Devuelve mt
# (o sea la matriz transpuesta) }
# }
# Nota: Usar columna() para ir obteniendo todas las columnas de la matriz.

def transponer(matriz: list) -> list:
    matriz_transpuesta: list = []
    for columna in columnas(matriz):
        matriz_transpuesta.append(columna)
    return matriz_transpuesta


# problema quien gana tateti (in m:seq⟨seq⟨Char⟩⟩) : Z {
# requiere: { esMatriz(m) }
# requiere: { |m| = 3 }
# requiere: { |m[0]| = 3 }
# requiere: { En la matriz si hay 3 X alineadas verticalmente =⇒ no hay 3 O alineadas verticalmente }
# requiere: { En la matriz si hay 3 O alineadas verticalmente =⇒ no hay 3 X alineadas verticalmente }
# requiere: { En la matriz si hay 3 X alineadas horizontalmente =⇒ no hay 3 O alineadas horizontalmente }
# requiere: { En la matriz si hay 3 O alineadas horizontalmente =⇒ no hay 3 X alineadas horizontalmente }
# requiere: { Para todo i,j ∈ {0, 1, 2} =⇒ m[i][j] = X ∨ m[i][j] = O ∨ m[i][j] = ” ”}
# asegura: { Si hay 3 O alineadas verticalmente, horizontalmente o en diagonal, devuelve 0 }
# asegura: { Si hay 3 X alineadas verticalmente, horizontalmente o en diagonal, devuelve 1 }
# asegura: { Si no hay ni 3 X, ni 3 O alineadas verticalmente, horizontalmente o en diagonal, devuelve 2 }
# }


def quien_gana_tateti(matriz: list[list[str]]) -> int:
    resultado = [gana_columna(matriz), gana_fila(matriz), gana_diagonal(matriz)]
    if 'X' in resultado:
        return 1
    if 'O' in resultado:
        return 0
    return 2
    
    
def gana_fila(matriz):
    for fila in matriz:
        if fila == ['X', 'X', 'X']:
            return 'X'
        if fila == ['O', 'O', 'O']:
            return 'O'
    return False

def gana_columna(matriz):
    clmns = columnas(matriz)
    for columna in clmns:
        if columna == ['X', 'X', 'X']:
            return 'X'
        if columna == ['O', 'O', 'O']:
            return 'O'
    return False

def gana_diagonal(matriz):
    diagonal_1 = []
    diagonal_2 = []
    inicio = 2
    for i in range(0,3):
        diagonal_1.append(matriz[i][i])
    for i in range(0,3):
        diagonal_2.append(matriz[i][inicio])
        inicio -= 1
    if diagonal_1 == ['X', 'X', 'X']:
        return 'X'
    if diagonal_2 == ['X', 'X', 'X']:
        return 'X'
    if diagonal_1 == ['O', 'O', 'O']:
        return 'O'
    if diagonal_2 == ['O', 'O', 'O']:
        return 'O'
    return False

