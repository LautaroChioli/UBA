# 1. problema CerosEnPosicionesPares (inout s:seq⟨Z⟩) {
# requiere: { T rue }
# modifica: { s }
# asegura: { (|s| = |s@pre|) y (para todo i entero, con 0 <= i < |s|, si i es impar entonces s[i] = s@pre[i] y, si i
# es par, entonces s[i] = 0) }
# }

def cero_en_posiciones_pares(s: list) -> list:
    for i in range(0,len(s)):
        if s[i] % 2 == 0:
            s[i] = 0
    return s
        

# 2. problema CerosEnPosicionesPares2 (in s:seq⟨Z⟩) : seq⟨Z⟩ {
# requiere: { T rue }
# asegura: { (|s| = |res|) y (para todo i entero, con 0 <= i < |res|, si i es impar entonces res[i] = s[i] y, si i es
# par, entonces res[i] = 0) }
# }

def cero_en_posiciones_pares2(s: list) -> list:
    res = s
    for i in range(0, len(res)):
        if i % 2 == 0:
            res[i] = 0
        else:
            res[i] = s[i]
    return res

# 3. Dada una cadena de caracteres devuelva una cadena igual a la anterior, pero sin las vocales. No se agregan espacios,
# sino que borra la vocal y concatena a continuaci´on.
# problema sin vocales (in s:seq⟨Char⟩) : seq⟨Char⟩ {
# requiere: { T rue }
# asegura: { res es la subsecuencia de s que se obtiene al quitarle las vocales a s }
# }

def sin_vocales(s: list) -> list:
    res = []
    vocales = ['a','e','i','o','u']
    for letra in s:
        if letra not in vocales:
            res.append(letra)
    return res

# Nota: Una subsecuencia de una cadena es una nueva secuencia que se crea eliminando algunos elementos de la cadena
# original, conservando el orden de los elementos restantes.
# 4. problema reemplaza vocales (in s:seq⟨Char⟩) : seq⟨Char⟩ {
# requiere: { T rue }
# asegura: { |res| = |s| }
# asegura: { Para todo i ∈ Z, si 0 ≤ i < |res| → (pertenece(<‘a’,‘e’,‘i’,‘o’,‘u’>, s[i]) ∧ res[i] = ‘ ’) ∨
# (¬ pertenece(<‘a’,‘e’,‘i’,‘o’,‘u’>, s[i]) ∧ res[i] = s[i])) }
# }

def reemplaza_vocales(s: list) -> list:
    res = s
    vocales = ['a','e','i','o','u']
    for i in range(0,len(res)):
        if res[i] in vocales:
            res[i] = ' '
    return res

# 5. problema da vuelta str (in s:seq⟨Char⟩) : seq⟨Char⟩ {
# requiere: { T rue }
# asegura: { |res| = |s| }
# asegura: { Para todo i ∈ Z si 0 ≤ i < |res| → res[i] = s[|s| − i − 1] }
# }

def da_vuelta_str(s: list) -> list:
    res = []
    for i in range(0, len(s)):
        res.append(s[len(s) - i -1])
    return res



# 6. problema eliminar repetidos (in s:seq⟨Char⟩) : seq⟨Char⟩ {
# requiere: { T rue }
# asegura: { (|res| ≤ |s|) ∧ (para todo i ∈ Z si 0 ≤ i < |s| → pertenece(s[i], res)) ∧ (para todo i, j ∈ Z si
# (0 ≤ i, j < |res| ∧ i ̸= j) → res[i] ̸= res[j]) }
# }

def eliminar_repetidos(s: list) -> list:
    letras_repetidas = []
    res = []
    for i in range(0,len(s)):
        if s[i] not in letras_repetidas:
            letras_repetidas.append(s[i])
            res.append(s[i])
    return res
            