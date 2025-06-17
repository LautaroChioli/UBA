# problema pertenece (in s:seq⟨Z⟩, in e: Z) : Bool {
# requiere: { T rue }
# asegura: { (res = true) ↔ (existe un i ∈ Z tal que 0 ≤ i < |s| ∧ s[i] = e) }
# }
# Implementar al menos de 3 formas distintas.

def pertenece1(lista: list, n: int) -> bool:
    for i in range(0, len(lista)):
        if lista[i] == n:
            return True
    return False

def pertenece2(lista: list, n: int) -> bool:
    cont = 0
    while cont < len(lista):
        if lista[cont] == n:
            return True
        else:
            cont += 1
    return False

def pertenece3(lista: list, n: int) -> bool:
    while lista != []:
        if lista.pop() == n:
            return True
    return False

def pertenece4(lista: list, n: int) -> bool:
    if n in lista:
        return True
    return False

# 2. problema divide a todos (in s:seq⟨Z⟩, in e: Z) : Bool {
# requiere: { e ̸= 0 }
# asegura: { (res = true) ↔ (para todo i ∈ Z si 0 ≤ i < |s| → s[i] mod e = 0) }
# }


def divide_a_todos(s: list, n: int) -> bool:
    for i in range(0, len(s)):
        if s[i] % n != 0:
            return False
    return True

# 3. problema suma total (in s:seq⟨Z⟩) : Z {
# requiere: { T rue }
# asegura: { res es la suma de todos los elementos de s }
# }
# Nota: no utilizar la funci´on sum() nativa.

def suma(s: list) -> int:
    total = 0
    for i in s:
        total += i
    return total

# problema maximo (in s:seq⟨Z⟩) : Z {
# requiere: { |s| > 0 }
# asegura: { res = al mayor de todos los n´umeros que aparece en s }
# }
# Nota: no utilizar la funci´on max() nativa.

def maximo(s: list) -> int:
    maximo = 0
    for n in s:
        if n > maximo:
            maximo = n
    return maximo

# problema minimo (in s:seq⟨Z⟩) : Z {
# requiere: { |s| > 0 }
# asegura: { res = al menor de todos los n´umeros que aparece en s }
# }
# Nota: no utilizar la funci´on min() nativa

def minimo(s: list) -> int:
    minimo = s[0]
    for i in s:
        if i < minimo:
            minimo = i
    return minimo



# problema ordenados (in s:seq⟨Z⟩) : Bool {
# requiere: { T rue }
# asegura: { res = true ↔(para todo i ∈ Z si 0 ≤ i < (|s| − 1) → s[i] < s[i + 1] }
# }

def ordenados(lista: list) -> bool:
    actual = 0
    for i in lista:
        if actual > i:
            return False
        actual = i
    return True
    

# problema pos maximo (in s:seq⟨Z⟩) : Z {
# requiere: { T rue }
# asegura: { (Si |s| = 0, entonces res = −1; si no, res = al ´ındice de la posici´on donde aparece el mayor elemento
# de s (si hay varios es la primera aparici´on) }
# }


def pos_maximo(s: list) -> int:
    indiceMax = 0 
    valorMax = 0
    if len(s) == 0:
        return -1
    for i in range(0, len(s)):
        if s[i] > valorMax:
            indiceMax = i
            valorMax = s[i]
    return indiceMax


# problema pos minimo (in s:seq⟨Z⟩) : Z {
# requiere: { T rue }
# asegura: { (Si |s| = 0, entonces res = −1; si no, res = al ´ındice de la posici´on donde aparece el menor elemento
# de s (si hay varios es la ´ultima aparici´on) }
# }

def pos_minimo(s: list) -> int:
    indiceMin = 0 
    if len(s) == 0:
        return -1
    valorMin = s[0]
    for i in range(0, len(s)):
        if s[i] <= valorMin:
            indiceMin = i
            valorMin = s[i]
    return indiceMin

# Dada una lista de palabras (seq⟨seq⟨Char⟩⟩), devolver verdadero si alguna palabra tiene longitud mayor a 7. Ejemplo:
# [“termo”, “gato”, “tener”, “jirafas”], devuelve falso.
# problema long mayorASiete (in s:seq⟨seq⟨Char⟩⟩) : Bool {
# requiere: { T rue }
# asegura: { (res = true) ↔ (existe i ∈ Z tal que (0 ≤ i < (|s| − 1)) y (|s[i]| > 7) }
# }

def long_mayor_siete(s: list) -> bool:
    for w in s:
        if len(w) > 7:
            return True
    return False

# Dado un texto en formato string, devolver verdadero si es pal´ındromo (se lee igual en ambos sentidos), falso en caso
# contrario. Las cadenas de texto vac´ıas o con 1 s´olo elemento son pal´ındromo.
# problema es palindroma (in s:seq⟨Char⟩) : Bool {
# requiere: { T rue }
# asegura: { (res = true) ↔ (s es igual a su reverso) }

# No esta permitido s[i:f], s[-i] o similar!!
# }

def reverse(s: list) -> list:
    palabra = []
    cont = len(s) - 1
    while cont >= 0:
        palabra.append(s[cont])
        cont -= 1
    return palabra

def es_palindromo(palabra: list) -> bool:
    if palabra == reverse(palabra):
        return True
    return False

#  Recorrer una seq⟨Z⟩ y devolver verdadero si hay 3 n´umeros iguales consecutivos, en cualquier posici´on y False en caso
# contrario.
# problema iguales consecutivos (in s:seq⟨Z⟩) : Bool {
# requiere: { T rue }
# asegura: { (res = true) ↔ (existe i, j, k ∈ Z tal que (0 ≤ i, j, k < (|s| − 1)) y (i + 2 = j + 1 = k) y
# (s[i] = s[j] = s[k])) }
# }

def iguales_consecutivos(s: list) -> bool:
    cont = 1
    last = s[0]
    for i in range(1, len(s)):
        if s[i] == last:
            cont += 1
            if cont == 3:
                return True
        else:
            cont = 1
        
        last = s[i]  
    return False
        
    


# 12. Recorrer una palabra en formato string y devolver True si ´esta tiene al menos 3 vocales distintas y False en caso
# contrario.
# problema vocales distintas (in s:seq⟨Char⟩) : Bool {
# requiere: { T rue }
# asegura: { (res = true) ↔ (existe i, j, k ∈ Z tal que (0 ≤ i, j, k < (|s| − 1)) y (s[i] ̸= s[j] ̸= s[k]) y
# (s[i], s[j], s[k] ∈ {‘a‘, ‘e‘, ‘i‘, ‘o‘, ‘u‘})) }
# No esta permitida la funcion remove() nativa
# }

def vocales_distintas(s: str) -> bool:
    vocalesCont = []
    vocales = ['a','e','i','o','u']
    for letra in s:
        if letra in vocales and letra not in vocalesCont:
            vocalesCont.append(letra)
    if len(vocalesCont) >= 3:
        return True
    return False
            


# 13. Recorrer una seq⟨Z⟩ y devolver la posici´on donde inicia la secuencia de n´umeros ordenada m´as larga. Si hay dos
# subsecuencias de igual longitud devolver la posici´on donde empieza la primera. La secuencia de entrada es no vac´ıa.
# problema pos secuencia ordenada mas larga (in s:seq⟨Z⟩) : Z {
# requiere: { |s| > 0 }
# asegura: { (res = i) ↔ (existe i, j ∈ Z tal que (0 ≤ i, j < (|s| − 1)) y i ≤ j y (para todo k tal que i ≤ k < j →
# s[k] ≤ s[k + 1]) y j-i+1 es m´aximo e i es el m´ınimo valor que lo cumple) }
# }

def secuencia_ordenada_mas_larga(s: list) -> int:
    len_max = 1
    len_actual = 1
    inicio_actual = 0
    inicio_max = 0

    for i in range(1, len(s)):
        if s[i] >= s[i - 1]:
            len_actual += 1
        else:
            len_actual = 1
            inicio_actual = i

        if len_actual > len_max:
            len_max = len_actual
            inicio_max = inicio_actual

    return inicio_max


# 14. Cantidad de d´ıgitos impares.
# problema cantidad digitos impares (in s:seq⟨Z⟩) : Z {
# requiere: { Todos los elementos de n´umeros son mayores o iguales a 0 }
# asegura: { res es la cantidad total de d´ıgitos impares que aparecen en cada uno de los elementos de n´umeros }
# }
# Por ejemplo, si la lista de n´umeros es [57, 2383, 812, 246], entonces el resultado esperado ser´ıa 5 (los d´ıgitos impares
# son 5, 7, 3, 3 y 1).

# def cantidad_digitos_impares(s: list) -> int:
#     dig_impares = 0
#     for numero in s:


def int_a_lista_digitos(n: int) -> list:
    divisor = cifra_mas_alta(n)
    numero_lista = []
    digito_actual = 0
    numero = n
    while divisor >= 1:
        digito_actual = 0
        while numero >= divisor:
            numero -= divisor
            digito_actual += 1
        numero_lista.append(digito_actual)
        divisor //= 10
    return numero_lista
    
def cifra_mas_alta(n: int) -> int:
    cifra = n
    divisor = 10
    while cifra >= 10:
        if cifra / divisor <= 10:
            return divisor
        divisor *= 10
    return 1