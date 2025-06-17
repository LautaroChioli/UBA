from queue import Queue as Cola
from queue import LifoQueue as Pila

# Ejercicio 1 (2,25 puntos)
# Implementar la función subsecuencia_mas_larga especificada (todos_consecutivos no es testeado)

# problema subsecuencia_mas_larga (in v: seq⟨Z⟩) : ZxZ {
#   requiere: { La longitud de v es distinto de 0 }
#   asegura: { Sea x la primera subsecuencia más larga en v tal que vale todos_consecutivos(x), la primera componente de res es igual a |x|
#   y la segunda es igual al índice en v donde comenzaría x }
# }

# problema todos_consecutivos (in v: seq⟨Z⟩) : Bool {
#   asegura: { res == True <==> cada par de elementos adyacentes en v son números consecutivos, es decir, que su diferencia es igual a 1 }
# }

def subsecuencia_mas_larga(v: list[int]) -> tuple[int, int]:
    indice_comienzo_max = 0
    long_max = 0
    long_actual = 0
    indice_comienzo_actual = 0
    secuencia_actual = []
    indice_actual = 0
    for numero in v:
        if len(secuencia_actual) == 1 or len(secuencia_actual) == 0:
            indice_comienzo_actual = indice_actual
        secuencia_actual.append(numero)
        if todos_consecutivos(secuencia_actual):
            long_actual += 1
        else:
            secuencia_actual.clear()
            long_actual = 1
            indice_comienzo_actual = 0
            secuencia_actual.append(numero)
        if long_actual > long_max:
            indice_comienzo_max = indice_comienzo_actual
            long_max = long_actual
        
        
        indice_actual += 1
    return (long_max, indice_comienzo_max - 1)


def todos_consecutivos(v: list[int]) -> bool:
    anterior = v[0]
    for i in range(1,len(v)):
        if not (v[i] == anterior + 1 or v[i] == anterior - 1):
            return False
        anterior = v[i]
    return True

# Ejercicio 2 (2,25 puntos)
# Ana tiene exámenes de respuesta Verdadero ó Falso. Ella sabe que en cada examen la cantidad 
# de respuestas correctas cuyo valor es Falso es igual a la cantidad de respuestas correctas 
# cuyo valor es Verdadero. Tenemos el historial de las respuestas de cada exámen dados por Ana 
# en una cola. En cada uno Ana respondió todas las preguntas.

# problema mejor_resultado_de_ana (in examenes: Cola⟨ seq⟨Bool⟩ ⟩) : seq⟨Z⟩ {
#   requiere:{ Cada elemento de examenes es no vacío y tiene longitud par }
#   asegura: { res tiene la misma cantidad de elementos que examenes }
#   asegura: { res[i] es igual a la máxima cantidad de respuestas correctas que Ana podría haber respondido en el i-ésimo exámen resuelto en examenes,
# para 0 <= i < cantidad de elementos de examenes }
# }
examenes = Cola()
examenes.put([True, False, False, False])
examenes.put([False,True,False,True])
examenes.put([True,True, True, True])
examenes.put([True, True])
examenes.put([False,False,False,False,False,False])
def mejor_resultado_de_ana(examenes: Cola[list[bool]]) -> list[int]:
    resultados = []
    res = []
    while not examenes.empty():
        resultados.append(examenes.get())
    for examen in resultados:
        falsos = 0
        verdaderos = 0
        for resp in examen:
            if resp:
                verdaderos += 1
            else:
                falsos += 1
        if verdaderos == falsos:
            res.append(len(examen))
        elif verdaderos > falsos:
            res.append((falsos % verdaderos) + len(examen)//2 )
        else:
            res.append((verdaderos % falsos) + len(examen)//2)
    return res


# Ejercicio 3 (2,25 puntos)
# problema cambiar_matriz(inout A: seq⟨seq⟨Z⟩⟩) {
#   requiere: { Todas las filas de A tienen la misma longitud }
#   requiere: { El mínimo número que aparece en A es igual a 1 }
#   requiere: { El máximo número que aparece en A es igual a #filas de A por #columnas de A }
#   requiere: { No hay enteros repetidos en A }
#   requiere: { Existen al menos dos enteros distintos en A }
#   modifica: { A }
#   asegura: { A tiene exactamente las mismas dimensiones que A@pre }
#   asegura: { El conjunto de elementos que aparecen en A es igual al conjunto de elementos que aparecen en A@pre }
#   asegura: { A[i][j] != A@pre[i][j] para todo i, j en rango }
# }

d = [[1,2,3], [4,5,6], [7,8,9]]


def cambiar_matriz(A: list[list[int]]) -> None:
    res = []
    pila = Pila()
    if len(A) % 2 == 1:
        tiene_centro = True
    for fila in A:
        pila.put(fila)
    while not pila.empty():
        res.append(pila.get())
    if tiene_centro:
        indice = 0
        fila_del_centro = res[len(A) // 2]
        nueva_fila = []
        for i in range(len(fila_del_centro)):
            if i < len(fila_del_centro) - 1:
                nueva_fila.append(fila_del_centro[i + 1])
            else:
                nueva_fila.append(fila_del_centro[0])
    temp= []
    temp.append(res.pop())
    fila = temp[0]
    while fila != fila_del_centro:
        if fila not in temp:
            temp.append(fila)
        fila = res.pop()
    if fila == fila_del_centro:
        res.append(nueva_fila)
    for l in temp:
        res.append(l)
        
    return res

        
# Ejercicio 4 (2,25 puntos)
# Tenemos un texto que contiene palabras. Por simplicidad, las palabras están separadas únicamente por uno o más espacios.

# problema palabras_por_vocales (in texto: string): Diccionario⟨Z,Z⟩ {
#   requiere: { Si existe una letra vocal en texto, esta no lleva tildes, diéresis, ni ningún otro símbolo }
#   asegura: { Si existe una palabra en texto con x vocales en total, x es clave de res }
#   asegura: { Las claves de res representan la cantidad total de vocales de una palabra, y cada valor corresponde a la cantidad de palabras en texto con ese número de vocales. }
#   asegura: { Los valores de res son positivos }
# }
ej = " hola todos  putopos "

def palabras_por_vocales(texto: str) -> dict[tuple[int ,int]]:
    palabras = separar_palabras(texto)
    vocales = ['a','e','i','o','u']
    res = {}
    for palabra in palabras:
        cant_vocales = 0
        for letra in palabra:
            if letra in vocales:
                cant_vocales += 1
        if cant_vocales not in res.keys():
            res[cant_vocales] = 1
        else:
            res[cant_vocales] += 1
    return res
def separar_palabras(texto):
    palabras = []
    palabra_actual = ""
    
    for caracter in texto:
        if caracter != " ":
            palabra_actual += caracter
        else:
            if palabra_actual:
                palabras.append(palabra_actual)
                palabra_actual = ""
    
    # Agregar la última palabra si hay algo pendiente
    if palabra_actual:
        palabras.append(palabra_actual)
    
    return palabras
print(palabras_por_vocales(" hola todos jaaa mu n"))
