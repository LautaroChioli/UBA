# Ejercicio 1. Veterinaria - Stock
# En la veterinaria ”Exactas’s pets”, al finalizar cada d´ıa, el personal registra en papeles los nombres y la cantidad actual de
# los productos cuyo stock ha cambiado. Para mejorar la gesti´on, desde la direcci´on de la veterinaria han pedido desarrollar una
# soluci´on en Python que les permita analizar las fluctuaciones del stock. Se pide implementar una funci´on, que reciba una lista
# de tuplas donde cada tupla contiene el nombre de un producto y su stock en ese momento. La funci´on debe procesar esta lista
# y devolver un diccionario que tenga como clave el nombre del producto y como valor una tupla con su m´ınimo y m´aximo stock
# hist´orico registrado.
# problema stock productos (in stock cambios : seq⟨str × Z⟩) : seq⟨Z⟩ {
# requiere: {Todos los elementos de stock cambios est´an formados por un str no vac´ıo y un entero ≥ 0.}
# asegura: {res tiene como claves solo los primeros elementos de las tuplas de stock cambios (o sea, un producto).}
# asegura: {res tiene como claves todos los primeros elementos de las tuplas de stock cambios.}
# asegura: {El valor en res de un producto es una tupla de cantidades. Su primer elemento es la menor cantidad de ese
# producto en stock cambios y como segundo valor el mayor.}
# }


def stock_productos(cambios: list[tuple[str, int]]) -> dict[tuple[int, int]]:
    res = {}
    temp = {}
    for cambio in cambios:
        if cambio[0] not in temp:
            temp[cambio[0]] = [cambio[1]]
        else:
            temp[cambio[0]].append(cambio[1])
    for key in temp:
        lista_actual = temp[key]
        max = maximo(lista_actual)
        min = minimo(lista_actual)
        res[key] = (minimo(lista_actual), maximo(lista_actual))
    print(res)
    return res
        
def maximo(lista):
    res = lista[0]
    for n in lista:
        if n > res:
            res = n
    return res

def minimo(lista):
    res = lista[0]
    for n in lista:
        if n < res:
            res = n
    return res

# Ejercicio 2. Veterinaria - Filtrar c´odigos de barra
# El hijo del due˜no de la veterinaria, cuya actividad principal es ver tik toks, cree que los productos cuyos c´odigos de barras
# terminan en n´umeros primos son especialmente auspiciosos y deben ser destacados en la tienda. Luego de convencer a su padre
# de esta idea, solicita una funci´on en Python que facilite esta gesti´on. Se pide implementar una funci´on que, dada una secuencia de
# enteros, cada uno representando un c´odigo de barras de un producto, cree y devuelva una nueva lista que contenga ´unicamente
# aquellos n´umeros de la lista original cuyos ´ultimos tres d´ıgitos formen un n´umero primo (por ejemplo, 101, 002 y 011).
# Nota: Un n´umero primo es aquel que solo es divisible por s´ı mismo y por 1. Algunos ejemplos de n´umeros primos de hasta
# tres d´ıgitos son: 2, 3, 5, 101, 103, 107, etc.
# problema filtrar codigos primos (in codigos barra : seq⟨Z⟩) : seq⟨Z⟩ {
# requiere: {Todos los enteros de codigos barra tienen, por lo menos, 3 d´ıgitos.}
# requiere: {No hay elementos repetidos en codigos barra.}
# asegura: {Los ´ultimos 3 d´ıgitos de cada uno de los elementos de res forman un n´umero primo.}
# asegura: {Todos los elementos de codigos barra cuyos ´ultimos 3 d´ıgitos forman un n´umero primo est´an en res.}
# asegura: {Todos los elementos de res est´an en codigos barra.}
# }

def filtar_codigos_primos(codigos: list[int]) -> list[int]:
    res = []
    original = copia_lista(codigos)
    indice_actual = 0
    for codigo in codigos:
        while codigo / 1000 >= 1:
            codigo %= 1000
        if es_primo(codigo):
            res.append(original[indice_actual])
        indice_actual += 1
    return res
    
def copia_lista(lista_original):
    res = []
    for original in lista_original:
        res.append(original)
    return res

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True

# Ejercicio 3. Veterinaria - Flujo de pacientes
# Con el objetivo de organizar el flujo de pacientes, en una veterinaria se anotan los tipos de mascotas que van ingresando
# al local. Se necesita identificar las consultas que involucran solo a perros y gatos. Por eso, se decide desarrollar una funci´on en
# Python que encuentre la secuencia m´as larga de consultas consecutivas que solo contenga los tipos de mascota ”perro” o ”gato”.
# Se pide implementar una funci´on que, dada una secuencia de strs, que representan los tipos de animales atendidos, devuelva el
# ´ındice donde comienza la subsecuencia m´as larga que cumpla con estas condiciones.
# problema subsecuencia mas larga (in tipos pacientes atendidos : seq⟨str⟩) : Z {
# requiere: {tipos pacientes atendidos tiene, por lo menos, un elemento ”perro” o ”gato”.}
# asegura: {res es el ´ındice donde empieza la subsecuencia m´as larga de tipos pacientes atendidos que contenga solo
# elementos ”perro” o ”gato”.}
# asegura: {Si hay m´as de una subsecuencia de tama˜no m´aximo, res tiene el ´ındice de la primera.}
# }

def subsecuencia_mas_larga(pacientes: list[str]) -> int:
    max_inicio = -1
    max_largo = 0

    i = 0
    while i < len(pacientes):
        if pacientes[i] == "perro" or pacientes[i] == "gato":
            tipo_actual = pacientes[i]
            inicio_actual = i
            largo_actual = 0
            while i < len(pacientes) and pacientes[i] == tipo_actual:
                largo_actual += 1
                i += 1
            if largo_actual > max_largo:
                max_largo = largo_actual
                max_inicio = inicio_actual
        else:
            i += 1  # Avanzamos si el elemento no es perro ni gato

    return max_inicio

# Ejercicio 4. Veterinaria - Tabla turnos
# Las personas responsables de los turnos est´an anotadas en una matriz donde las columnas representan los d´ıas, en orden de
# lunes a domingo, y cada fila un rango de una hora. Hay cuatro filas para los turnos de la ma˜nana (9, 10, 11 y 12 hs) y otras
# cuatro para la tarde (14, 15, 16 y 17).
# 1
# Para hacer m´as eficiente el trabajo del personal de una veterinaria, se necesita analizar si quienes quedan de responsables,
# est´an asignadas de manera continuada en los turnos de cada d´ıa.
# Para ello se pide desarrollar una funci´on en Python que, dada la matriz de turnos, devuelva una lista de tuplas de bool, una
# por cada d´ıa. Cada tupla debe contener dos elementos. El primer elemento debe ser True si y solo si todos los valores de los
# turnos de la ma˜nana para ese d´ıa son iguales entre s´ı. El segundo elemento debe ser True si y solo si todos los valores de los
# turnos de la tarde para ese d´ıa son iguales entre s´ı.
# Siempre hay una persona responsable en cualquier horario de la veterinaria.
# problema un responsable por turno (in grilla horaria : seq⟨seq⟨str⟩⟩) : seq⟨Bool × Bool⟩ {
# requiere: {|grilla horaria| = 8.}
# requiere: {Todos los elementos de grilla horaria tienen el mismo tama˜no (mayor a 0 y menor 8).}
# requiere: {No hay cadenas vac´ıas en las listas de grilla horaria.}
# asegura: {|res| = |grilla horaria[0]|.}
# asegura: {El primer valor de la tupla en res [i], con i:Z, 0 res| es igual a True los primeros 4 valores de la columna i de
# grilla horaria son iguales entre s´ı.}
# asegura: {El segundo valor de la tupla en res [i], con i:Z, 0 res| es igual a True los ´ultimos 4 valores de la columna i de
# grilla horaria son iguales entre s´ı.}
"""
  lunes  martes  miercoles jueves viernes sabado domingo
[["Juan","Maria","Juan","Maria","Maria","Pedro","Pedro"], 
["Juan", "Maria", "Juan","Maria","Maria","Pedro","Juan"],
["Juan", "Maria", "Juan","Maria","Maria","Pedro","Juan"], 
["Juan", "Maria", "Juan","Pedro","Maria","Pedro","Juan"],  12
["Maria","Maria", "Juan","Maria","Maria","Juan""Pedro"],   14
["Maria","Maria", "Juan","Maria","Maria","Juan","Pedro"],  
["Grug", "Maria", "Pedro","Maria","Maria","Juan","Pedro"],  
["Maria","Maria", "Juan","Maria","Maria","Juan","Pedro"]]  
"""

def responsable_por_turno(grilla: list[list[str]]) -> list[tuple[bool, bool]]:
    i = 0
    cuatro_iguales_mañana = False
    cuatro_iguales_tarde = False
    personas_mañana = []
    personas_tarde = []
    tarde = []
    while i < 4:
        tarde.append(grilla.pop())
        i += 1
    mañana = grilla
    i = 0
    res = []
    while i < 7:
        for hora in mañana:
            personas_mañana.append(hora[i])
        for hora in tarde:
            personas_tarde.append(hora[i])
        res.append((todos_iguales(personas_mañana),todos_iguales(personas_tarde)))
        personas_tarde.clear()
        personas_mañana.clear()
        i += 1
    return res

            
def todos_iguales(nombres):
    primero = nombres[0]
    for nombre in nombres:
        if nombre != primero:
            return False
    return True
        
            
        

# print(responsable_por_turno([["Juan","Maria","Juan","Maria","Maria","Pedro","Pedro"], 
# ["Juan", "Maria", "Juan","Maria","Maria","Pedro","Juan"],
# ["Juan", "Maria", "Juan","Maria","Maria","Pedro","Juan"], 
# ["Juan", "Maria", "Juan","Pedro","Maria","Pedro","Juan"],  
# ["Maria","Maria", "Juan","Maria","Maria","Juan","Pedro"],
# ["Maria","Maria", "Juan","Maria","Maria","Juan","Pedro"],  
# ["Grug", "Maria", "Pedro","Maria","Maria","Juan","Pedro"],  
# ["Maria","Maria", "Juan","Maria","Maria","Juan","Pedro"]] ))

# Ejercicio 5. Sala de Escape - Promedio de salidas
# Un grupo de amigos apasionados por las salas de escape, esas aventuras inmersivas donde tienen 60 minutos para salir de
# una habitaci´on resolviendo enigmas, llevan un registro meticuloso de todas las salas de escape que hay en Capital. Este registro
# indica si han visitado una sala y si pudieron o no salir de ella. Un 0 significa que no fueron, un 61 que no lograron salir a tiempo,
# y un n´umero entre 1 y 60 representa los minutos que les tom´o escapar exitosamente. Con estos datos, pueden comparar sus
# logros y desaf´ıos en cada nueva aventura que emprenden juntos.
# Dado un diccionario donde la clave es el nombre de cada amigo y el valor es una lista de los tiempos (en minutos) registrados
# para cada sala de escape en Capital, escribir una funci´on en Python que devuelva un diccionario. En este nuevo diccionario,
# las claves deben ser los nombres de los amigos y los valores deben ser tuplas que indiquen la cantidad de salas de las que cada
# persona logr´o salir y el promedio de los tiempos de salida (solo considerando las salas de las que lograron salir).
# problema promedio de salidas (in registro: dict<str, seq⟨Z⟩>) : dict<str, <Z×R>> {
# requiere: {registro tiene por lo menos un integrante.}
# requiere: {Todos los integrantes de registro tiene por lo menos un tiempo.}
# requiere: {Todos los valores de registro tiene la misma longitud.}
# requiere: {Todos los tiempos de los valores de registro est´an entre 0 y 61 inclusive.}
# asegura: {res tiene las mismas claves que registro.}
# asegura: {El primer elemento de la tupla de res para un integrante, es la cantidad de salas con tiempo mayor estricto a
# 0 y menor estricto a 61 que figuran en sus valores de registro.}
# asegura: {El segundo elemento de la tupla de res para un integrante, si la cantidad de salas de las que sali´o es mayor a
# 0: es el promedio de salas con tiempo mayor estricto a 0 y menor estricto a 61 que figuran en sus valores de registro; sino
# es 0.0.}
# }
"""
{
    "Juan": [0,10,50,61,59,0],
    "Pedro": [41,10,0,61,29]
}
"""

def promedio_de_salidas(registro: dict[str, list[int]]) -> dict[str, tuple[int, float]]:
    nuevo_dict = {}
    for persona in registro:
        lista_actual = lista_sin_0_y_61(registro[persona]) 
        prom = promedio(lista_actual)
        nuevo_dict[persona] = (len(lista_actual), prom)
    return nuevo_dict

def promedio(lista):
    total = 0
    for n in lista:
        total += n
    total = total/len(lista)
    return total

def lista_sin_0_y_61(lista):
    nueva = []
    for n in lista:
        if n != 0 and n != 61:
            nueva.append(n)
    return nueva

# Ejercicio 6. Sala de Escape - Tiempo m´as r´apido
# Dada una lista con los tiempos (en minutos) registrados para cada sala de escape de Capital, escribir una funci´on en Python
# que devuelva la posici´on (´ındice) en la cual se encuentra el tiempo m´as r´apido, excluyendo las salas en las que no haya salido (0
# o mayor a 60).
# problema tiempo mas rapido (in tiempos salas: seq⟨Z⟩) : Z {
# requiere: {Hay por lo menos un elemento en tiempos salas entre 1 y 60 inclusive.}
# requiere: {Todos los tiempos en tiempos salas est´an entre 0 y 61 inclusive.}
# asegura: {res es la posici´on de la sala en tiempos salas de la que m´as r´apido se sali´o (en caso que haya m´as de una,
# devolver la primera, osea la de menor ´ındice).}
# }

def tiempo_mas_rapido(tiempos: list[int]) -> int:
    lista_bien = tiempos
    indice_max = 0
    numero_max = lista_bien[0]
    indice = 0
    for tiempo in lista_bien:
        if 0 < tiempo < 61:
            if tiempo > numero_max:
                numero_max = tiempo
                indice_max = indice
        indice += 1
    return indice_max
    
            
        

# Ejercicio 7. Sala de Escape - Racha m´as larga
# Dada una lista con los tiempos (en minutos) registrados para cada sala de escape a la que fue una persona, escribir una
# funci´on en Python que devuelva una tupla con el ´ındice de inicio y el ´ındice de fin de la subsecuencia m´as larga de salidas
# exitosas de salas de escape consecutivas.
# problema racha mas larga (in tiempos: seq⟨Z⟩) : <Z×Z> {
# requiere: {Hay por lo menos un elemento en tiempos entre 1 y 60 inclusive.}
# requiere: {Todos los tiempos en tiempos est´an entre 0 y 61 inclusive.}
# asegura: {En la primera posici´on de res est´a la posici´on (´ındice de la lista) de la sala que inicia la racha m´as larga.}
# asegura: {En la segunda posici´on de res est´a la posici´on (´ındice de la lista) de la sala que finaliza la racha m´as larga.}
# asegura: {El elemento de la primer posici´on de res en tiempos es mayor estricto 0 y menor estricto que 61.}
# asegura: {El elemento de la segunda posici´on de res en tiempos es mayor estricto 0 y menor estricto que 61.}
# asegura: {La primera posici´on de res es menor o igual a la segunda posici´on de res.}
# asegura: {No hay valores iguales a 0 o a 61 en tiempos entre la primer posici´on de res y la segunda posici´on de res.}
# asegura: {No hay otra subsecuencia de salidas exitosas, en tiempos, de mayor longitud que la que est´a entre la primer
# posici´on de res y la segunda posici´on de res.}
# asegura: {Si hay dos o m´as subsecuencias de salidas exitosas de mayor longitud en tiempos, res debe contener la primera
# de ellas.}
# }

def racha_mas_larga(tiempos: list[int]) -> tuple[int, int]:
    cant_seguidas = 0
    max_seguidas = 0
    indice_actual = -1
    max_indice_inicio = 0
    max_indice_final = 0
    inicio_actual = 0
    final_actual = 0
    for tiempo in tiempos:
        indice_actual += 1
        if cant_seguidas == 0:
           inicio_actual = indice_actual
        if 0 < tiempo < 60:
            cant_seguidas += 1
        else:
            final_actual = indice_actual
            if cant_seguidas > max_seguidas:
                max_seguidas = cant_seguidas
                max_indice_inicio = inicio_actual
                max_indice_final = final_actual
            cant_seguidas = 0
    return (max_indice_inicio, max_indice_final -1)


# Ejercicio 8. Sala de Escape - Escape en solitario
# Dada una matriz donde las columnas representan a cada amigo y las filas representan las salas de escape, y los valores son los
# tiempos (en minutos) registrados para cada sala (0 si no fueron, 61 si no salieron, y un n´umero entre 1 y 60 si salieron), escribir
# una funci´on en Python que devuelva los ´ındices de todas las filas (que representan las salas) en las cuales el primer, segundo y
# cuarto amigo no fueron (0), pero el tercero s´ı fue independientemente de si sali´o o no).
# problema escape en solitario (in amigos por salas: seq⟨seq⟨Z⟩⟩) : seq⟨Z⟩ {
# requiere: {Hay por lo menos una sala en amigos por salas.}
# requiere: {Hay 4 amigos en amigos por salas.}
# requiere: {Todos los tiempos en cada sala de amigos por salas est´an entre 0 y 61 inclusive.}
# asegura: {La longitud de res es menor igual que la longitud de amigos por salas.}
# asegura: {Por cada sala en amigos por salas cuyo primer, segundo y cuarto valor sea 0, y el tercer valor sea distinto de
# 0, la posici´on de dicha sala en amigos por salas debe aparecer res.}
# asegura: {Para todo i pertenciente a res se cumple que el primer, segundo y cuarto valor de amigos por salas[i] es 0, y
# el tercer valor es distinto de 0.}
# }
"""
[[0,0,1,0],
 [0,1,1,0],
 [1,1,0,1],
 [0,61,4,61]]
"""

def escape_en_solitario(amigos_por_salas: list[list[int]]) -> list[int]:
    indice = -1
    salas_res = []
    for sala in amigos_por_salas:
        indice += 1
        if (sala[0] != 0 and sala[0] != 61) or (sala[1] != 0 and sala[1] != 61) or (sala[3] != 0 and sala[3] != 61):
            continue
        else:
            salas_res.append(indice)
    return salas_res


# Ejercicio 9. Juego de la Gallina
# El juego del gallina es una competici´on en la que dos participantes conducen un veh´ıculo en direcci´on al del contrario; si
# alguno se desv´ıa de la trayectoria de choque pierde y es humillado por comportarse como un ”gallina”. Se hizo un torneo para
# ver qui´en es el menos gallina. Juegan todos contra todos una vez y van sumando puntos, o restando. Si dos jugadores juegan y
# se chocan entre s´ı, entonces pierde cada uno 5 puntos por haberse da˜nado. Si ambos jugadores se desv´ıan, pierde cada uno 10
# puntos por gallinas. Si uno no se desv´ıa y el otro s´ı, el gallina pierde 15 puntos por ser humillado y el ganador suma 10 puntos!
# En este torneo, cada persona que participa tiene una estrategia predefinida para competir: o siempre se dev´ıa, o nunca lo hace.
# Se debe programar la funci´on ‘torneo de gallinas’ que recibe un diccionario (donde las claves representan los nombres de los
# participantes que se anotaron en el torneo, y los valores sus respectivas estrategias) y devuelve un diccionario con los puntajes
# obtendidos por cada jugador.
# problema torneo de gallinas (in estrategias: dict<str, str>) : dict<str, Z> {
# requiere: {estrategias tiene por lo menos 2 elementos (jugadores).}
# requiere: {Las claves de estrategias tienen longitud mayor a 0.}
# requiere: {Los valores de estrategias s´olo pueden ser los strs ”me desv´ıo siempre” ´o ”me la banco y no me desv´ıo”.}
# asegura: {Las claves de res y las claves de estrategias son iguales.}
# asegura: {Para cada jugador p perteneciente a claves(estrategias), res[p] es igual a la cantidad de puntos que obtuvo al
# finalizar el torneo, dado que jug´o una vez contra cada otro jugador.}
# }
# 3


# Ejercicio 10. Cola en el Banco
# En el banco ExactaBank los clientes hacen cola para ser atendidos por un representante. Los clientes son representados por
# las tuplas (nombre, tipo afiliado) donde la primera componente es el nombre y el tipo afiliado puede ser ”com´un” o ”vip”.
# Se nos pide implementar una funci´on en python que dada una cola de clientes del banco, devuelva una nueva cola con los
# mismos clientes pero en donde los clientes vip est´an primero que los clientes comunes manteniendo el orden original de los clientes
# vips y los comunes entre s´ı.
# problema reordenar cola priorizando vips (in filaClientes: Cola<str × str>) : Cola<str> {
# requiere: {La longitud de los valores de la primera componente de las tuplas de la cola filaClientes es mayor a 0.}
# requiere: {Los valores de la segunda componente de las tuplas de la cola filaClientes son ”com´un” o ”vip”.}
# requiere: {No hay dos tuplas en filaClientes que tengan la primera componente iguales entre s´ı.}
# asegura: {todo valor de res aparece como primera componente de alguna tupla de filaClientes.}
# asegura: {|res| = |filaCliente|.}
# asegura: {res no tiene elementos repetidos.}
# asegura: {No hay ning´un cliente ”com´un” antes que un ”vip” en res.}
# asegura: {Para todo cliente c1 y cliente c2 de tipo ”com´un” pertenecientes a filaClientes si c1 aparece antes que c2 en
# filaClientes entonces el nombre de c1 aparece antes que el nombre de c2 en res.}
# asegura: {Para todo cliente c1 y cliente c2 de tipo ”vip” pertenecientes a filaClientes si c1 aparece antes que c2 en
# filaClientes entonces el nombre de c1 aparece antes que el nombre de c2 en res.}
# }


# Ejercicio 11. Sufijos que son pal´ındromos
# Decimos que una palabra es pal´ındromo si se lee igual de izquierda a derecha que de derecha a izquierda. Se nos pide programar
# en python la siguiente funci´on:
# problema cuantos sufijos son palindromos (in texto: str) : Z {
# requiere: {True}
# asegura: {res es igual a la cantidad de pal´ındromos que hay en el conjunto de sufijos de texto.}
# }
# Nota: un sufijo es una subsecuencia de texto que va desde una posici´on cualquiera hasta el al final de la palabra. Ej: ”Diego”,
# el conjunto de sufijos es: ”Diego”, ”iego”,”ego”,”go”, ”o”. Para este ejercicio no consideraremos a ”” como sufijo de ning´un texto.
# Ejercicio 12. Ta-Te-Ti-Facilito
# Ana y Beto juegan al Ta-Te-Ti-Facilito. El juego es en un tablero cuadrado de lado entre 5 y 10. Cada jugador va poniendo su
# ficha en cada turno. Juegan intercaladamente y comienza Ana. Ana pone siempre una ”X” en su turno y Beto pone una ”O” en el
# suyo. Gana la persona que logra poner 3 fichas suyas consecutivas en forma vertical. Si el tablero est´a completo y no gan´o nadie,
# entonces se declara un empate. El tablero comienza vac´ıo, representado por ” ” en cada posici´on. Notar que dado que juegan por
# turnos y comienza Ana poniendo una ”X” se cumple que la cantidad de ”X” es igual a la cantidad de ”O” o bien la cantidad
# de ”X” son uno m´as que la cantidad de ”O”. Se nos pide implementar una funci´on en python quien gano el tateti facilito que
# determine si gan´o alguno, o si Beto hizo trampa (puso una ”O” cuando Ana ya hab´ıa ganado).
# problema quien gano el tateti facilito (in tablero:seq⟨seq⟨Char⟩⟩) : Z {
# requiere: {tablero es una matriz cuadrada.}
# requiere: {5 ≤ |tablero[0]| ≤ 10.}
# requiere: {tablero s´olo tiene ”X”, ”O” y ”” (espacio vac´ıo) como elementos.}
# requiere: {En tablero la cantidad de ”X” es igual a la cantidad de ”O” o bien la cantidad de ”X” es uno m´as que la
# cantidad de ”O”.}
# asegura: {res = 1 ⇔ hay tres ”X” consecutivas en forma vertical(misma columna) y no hay tres ”O” consecutivas en
# forma vertical(misma columna).}
# asegura: {res = 2 ⇔ hay tres ”O” consecutivas en forma vertical (misma columna) y no hay tres ”X” consecutivas en
# forma vertical(misma columna).}
# asegura: {res = 0 ⇔ no hay tres ”O” ni hay tres ”X” consecutivas en forma vertical.}
# asegura: {res = 3 ⇔ hay tres ”X” y hay tres ”O” consecutivas en forma vertical (evidenciando que beto hizo trampa).}
# }


# Ejercicio 13. Hospital - Atenci´on por Guardia
# Desde el Hospital Fernandez nos pidieron solucionar una serie de problemas relacionados con la informaci´on que maneja sobre
# los pacientes y el personal de salud. En primer lugar debemos resolver en qu´e orden se deben atender los pacientes que llegan a
# 4
# la guardia. En enfermer´ıa, hay una primera instancia que clasifica en dos colas a los pacientes: una urgente y otra postergable
# (esto se llama hacer triage). A partir de dichas colas que contienen la identificaci´on del paciente, se pide devolver una nueva cola
# seg´un la siguiente especificaci´on.
# problema orden de atencion (in urgentes: cola<Z>, in postergables: cola<Z>) : cola<Z> {
# requiere: {No hay elementos repetidos en urgentes.}
# requiere: {No hay elementos repetidos en postergables.}
# requiere: {La intersecci´on entre postergables y urgentes es vac´ıa.}
# requiere: {|postergables| = |urgentes|.}
# asegura: {No hay repetidos en res.}
# asegura: {res es permutaci´on de la concatenaci´on de urgentes y postergables.}
# asegura: {Si urgentes no es vac´ıa, en la cabeza de res hay un elemento de urgentes.}
# asegura: {En res no hay dos seguidos de urgentes.}
# asegura: {En res no hay dos seguidos de postergables.}
# asegura: {Para todo c1 y c2 de tipo ”urgente” pertenecientes a urgentes si c1 aparece antes que c2 en urgentes entonces
# c1 aparece antes que c2 en res.}
# asegura: {Para todo c1 y c2 de tipo ”postergable” pertenecientes a postergables si c1 aparece antes que c2 en postergables
# entonces c1 aparece antes que c2 en res.}
# }


# Ejercicio 14. Hospital - Alarma epidemiol´ogica
# Necesitamos detectar la aparici´on de posibles epidemias. Para esto contamos con un lista de enfermedades infecciosas y los
# registros de atenci´on por guardia dados por una lista expedientes. Cada expediente es una tupla con ID paciente y enfermedad
# que motiv´o la atenci´on. Debemos devolver un diccionario cuya clave son las enfermedades infecciosas y su valor es la proporci´on
# de pacientes que se atendieron por esa enfermedad. En este diccionario deben aparecer solo aquellas enfermedades infecciosas
# cuya proporci´on supere cierto umbral.
# problema alarma epidemiologica (in registros : seq⟨Z × str⟩, in infecciosas : seq⟨str⟩, in umbral : R) : dict<str, R> {
# requiere: {0 < umbral < 1.}
# asegura: {claves de res pertenecen a infecciosas.}
# asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa
# enfermedad sobre el total de registros es mayor o igual al umbral, entonces res[enfermedad] = porcentaje.}
# asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa
# enfermedad sobre el total de registros es menor que el umbral, entonces enfermedad no aparece en res.}
# }


# Ejercicio 15. Hospital - Empleado del mes
# Dado un diccionario con la cantidad de horas trabajadas por empleado, en donde la clave es el ID del empleado y el valor es
# una lista de las horas trabajadas por d´ıa, queremos saber quienes trabajaron m´as para darles un premio. Se deber´a buscar la o
# las claves para la cual se tiene el m´aximo valor de cantidad total de horas, y devolverlas en una lista.
# problema empleados del mes (horas:dicc<Z, seq⟨Z⟩) : seq⟨Z⟩ {
# requiere: {No hay valores en horas que sean listas vac´ıas.}
# asegura: {Si ID pertence a res entonces ID pertence a las claves de horas.}
# asegura: {Si ID pertenece a res, la suma de sus valores de horas es el m´aximo de la suma de elementos de horas de todos
# los otros IDs.}
# asegura: {Para todo ID de claves de horas, si la suma de sus valores es el m´aximo de la suma de elementos de horas de
# los otros IDs, entonces ID pertenece a res.}
# }


# Ejercicio 16. Hospital - Nivel de ocupaci´on
# Queremos saber qu´e porcentaje de ocupaci´on de camas hay en el hospital. El hospital se representa por una matriz en donde
# las filas son los pisos, y las columnas son las camas. Los valores de la matriz son Booleanos que indican si la cama est´a ocupada
# o no. Si el valor es verdadero (True) indica que la cama est´a ocupada.
# Se nos pide programar en Python una funci´on que devuelve una secuencia de reales, indicando la proporci´on de camas
# ocupadas en cada piso.
# problema nivel de ocupacion (in camas por piso:seq⟨seq⟨Bool⟩⟩) : seq⟨R⟩ {
# requiere: {Todos los pisos tienen la misma cantidad de camas.}
# requiere: {Hay por lo menos 1 piso en el hospital.}
# requiere: {Hay por lo menos una cama por piso.}
# asegura: {|res| = |camas por piso|.}
# asegura: {Para todo 0 ≤ i < |res| se cumple que res[i] es igual a la cantidad de camas ocupadas del piso i dividido el
# total de camas del piso i).}
# }