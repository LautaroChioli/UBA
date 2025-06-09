import random
from typing import Any
import os

# Constantes para dibujar
BOMBA: str      = chr(128163)       # Síimbolo de una mina
BANDERA: str    = chr(127987)       # Símbolo de bandera blanca
VACIO: str      = ' '               # Símbolo vacio inicial
EstadoJuego     = dict[str, Any]    # Tipo de alias para el estado del juego

def existe_archivo(ruta_directorio: str, nombre_archivo:str) -> bool:
    return os.path.exists(os.path.join(ruta_directorio, nombre_archivo)) # Chequea si existe el archivo en la ruta dada

#--------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 1 # TERMINADO
#--------------------------------------------------------------------------------------------------------------------------------------
def colocar_minas(filas: int, columnas: int, minas: int) -> list[list[int]]:
    # Recorre casilla por casilla con un 20% de cambiar su valor a -1 (mina), si ocurre, se le resta 1 al total de minas que faltan por poner.
    # Si llega al final de la matriz y no puso todas las minas aún, vuelve a empezar desde la primera posición.
    res: list[list[int]] = crear_matriz(filas, columnas)
    while minas > 0:
        for fila in res:
            for i in range(0, len(fila)):
                if fila[i] != -1:  # Chequea que la casilla no sea ya una mina.
                    if random.randint(1,10) > 8:
                        fila[i] = -1
                        minas -= 1
                        if minas == 0:
                            break
            if minas == 0:
                break
    return res

def es_matriz(t: list[list[int]]) -> bool:  # Vale para matrices cuadradas o no cuadradas!
    if (not t) or (not t[0]):               # Casos especiales: t=[] o t=[[]]
        return False
    for fila in t:
        if len(fila) != len(t[0]):          # Elejimos como referencia la fila t[0] (podría ser cualquiera)
            return False
    return True

#-------------------------------------------------------------------------------
# Función Auxiliar # Crea una matriz de n x m (n-filas por m-columnas) con todas las casillas = 0
def crear_matriz(filas:int, columnas:int) -> list[list[int]]:
    matriz: list[list[int]] = []
    for i in range(0,filas):
        fila: list = []
        for j in range(0,columnas):
            fila.append(0)
        matriz.append(fila)
    return matriz
#-------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 2 # TERMINADO
#--------------------------------------------------------------------------------------------------------------------------------------
# Recorre posición por posición, si no es una mina, cambia su valor por la cantidad de minas adyacentes.
def calcular_numeros(tablero: list[list[int]]) -> None: # Recibo una matriz y la actualiza (modifica) (pero la función no devuelve nada)
    filas: int      = len(tablero)
    columnas: int   = len(tablero[0])
    for i in range(0, filas):
        for j in range(0, columnas):
            if tablero[i][j] != -1:
                tablero[i][j] = minas_adyacentes(tablero, (i,j))

#-------------------------------------------------------------------------------
# Función Auxiliar # Toma como argumento la matriz tablero, y una posición (i,j) dada, cuyas cantidad de minas adyacentes quiere conocerse. Busca cada casilla adyacente a (i,j) y compara su valor con -1. Si el valor es True (es igual a -1), suma uno a la cant de minas adyacentes.
def minas_adyacentes(tablero: list[list[int]], posicion: tuple[int,int]) -> int:
    cant_minas_adyacentes: int  = 0
    pos_fila: int               = posicion[0]
    pos_columna: int            = posicion[1]
    filas: int                  = len(tablero)
    columnas: int               = len(tablero[0])
    for i in range(pos_fila - 1, pos_fila + 2):
        for j in range(pos_columna - 1, pos_columna + 2):
            if 0 <= i < filas and 0 <= j < columnas: # Condicion para que no ocurra IndexError, por ej., la posición de una esquina.
                if tablero[i][j] == -1:
                    cant_minas_adyacentes += 1
    return cant_minas_adyacentes
#-------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 3 # TERMINADO
#--------------------------------------------------------------------------------------------------------------------------------------
# Crea todas las variables necesarias para el diccionario EstadoJuego y las actualiza.
def crear_juego(filas: int, columnas: int, minas: int) -> EstadoJuego:
    if filas <= 0 or columnas <= 0 or minas < 0 or (minas > filas*columnas):
        res: str = 'Juego Inválido' # Agrego esta condición por la función estructura_y_tipos_validos
    else:
        res: dict[str,Any]                  = {}
        tablero: list[list[int]]            = colocar_minas(filas, columnas, minas)
        calcular_numeros(tablero)           # actualizamos los valores de tablero
        tablero_visible: list[list[str]]    = vaciar_matriz(tablero)
        res.update({
            'filas':            filas,
            'columnas':         columnas,
            'minas':            minas,
            'tablero':          tablero,
            'tablero_visible':  tablero_visible,
            'juego_terminado':  False
        })
    return res

def estado_valido(estado: EstadoJuego) -> bool:
    minas_totales: int = 0
    for i in range(len(estado['tablero'])):
        for j in range(len(estado['tablero'][i])):
            if estado['tablero'][i][j] == -1:
                minas_totales += 1 # voy contando las minas que haya

    if estructura_y_tipos_validos(estado) == False: # Si EstaadoJuego esta formada incorrectamente
        return False
    if minas_totales != estado['minas']: #Si no concuerdan la cantidad de minas previstas con las que hay en el tablero
        return False
    if todas_celdas_seguras_descubiertas(estado['tablero'], estado['tablero_visible']) and not (estado['juego_terminado']): # Si se ganó el juego, pero EstadoJuego no lo da como terminado
        return False

    for i in range(len(estado['tablero_visible'])):
        for j in range(len(estado['tablero_visible'][i])):
            elem: str = estado['tablero_visible'][i][j]
            valor_real: int = estado['tablero'][i][j]
            if ((elem == BOMBA) and (estado['juego_terminado'] == False)):
                return False
            if ((elem == BOMBA) and (valor_real != -1)):
                return False
            if ((elem not in [BOMBA,VACIO,BANDERA]) and (elem != str(valor_real))):
                return False
    if not todas_celdas_seguras_descubiertas(estado['tablero'], estado['tablero_visible']) and estado['juego_terminado']:
        return False
    return True
# Nota: La condición estado['tablero'] = calcular_numeros(tablero) que pide el asegura de la especificación ya está automáticamente asegurada por la función crear_juego.

def estructura_y_tipos_validos(estado: EstadoJuego) -> bool:
    res: bool = True
    if estado == 'Juego Inválido': # Por este caso, tuvimos que agregar las primeras líneas de crear_juego
        res = False
    else:
        if ( # Impongo las condiciones de los asegura
            len(estado)                 != 6 or
            len(estado['tablero'])      != estado['filas'] or
            len(estado['tablero'][0])   != estado['columnas'] or
            son_matriz_y_misma_dimension(estado['tablero'], estado['tablero_visible']) == False
        ):
            res = False
        for fila in estado['tablero']:
            for elem in fila:
                if elem not in range(-1,9):
                    res = False
        for fila in estado['tablero_visible']:
            for elem in fila:
                if elem not in [VACIO, BOMBA, BANDERA, '0', '1', '2', '3', '4', '5', '6', '7', '8']:
                    res = False
    return res

def son_matriz_y_misma_dimension(t1: list[list[int]], t2: list[list[int]]) -> bool:
    res: bool = False
    if es_matriz(t1) == False or es_matriz(t2) == False:
        res = False
    else:   # es_matriz ya chequea que len de todas las filas sean iguales => solo veo fila 0
        if (len(t1) == len(t2)) and (len(t1[0]) == len(t2[0])):
            res = True
    return res

# Prueba que aún haya una casilla sin mina que no se haya revelado, o que todas las minas estén sin revelar o con una bandera encima.
def todas_celdas_seguras_descubiertas(tablero: list[list[int]], tablero_visible: list[list[str]]) -> bool:
    res: bool = True
    for i in range(0, len(tablero)): # len(tablero) = filas!
        for j in range(0, len(tablero[0])): # columnas
            if ((tablero[i][j] != -1) and (tablero_visible[i][j] in [VACIO,BANDERA])):
                res = False # Tan pronto como una condición no se cumpla -> res=False y break!
                break
            if ((tablero[i][j] == -1) and (tablero_visible[i][j] == str(tablero[i][j]))):
                res = False # Ídem
                break
    return res

#-------------------------------------------------------------------------------
# Función Auxiliar # Para la función crear_juego (crea un tablero vacío (' ') de igual dimensión que el real)
def vaciar_matriz(tablero: list[list[int]]) -> list[list[str]]:
    tablero_visible: list[list[str]]    = []
    filas_tablero: int                  = len(tablero)
    columnas_tablero: int               = len(tablero[0])
    for i in range(filas_tablero):
        fila: list[str] = []
        for j in range(columnas_tablero):
            fila.append(VACIO)
        tablero_visible.append(fila)
    return tablero_visible
#-------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 4 # TERMINADO
#--------------------------------------------------------------------------------------------------------------------------------------
def obtener_estado_tablero_visible(estado: EstadoJuego) -> list[list[str]]:
    res: list[list[str]]                = [] # Copia del tablero
    tablero_original: list[list[str]]   = estado['tablero_visible']
    for fila in tablero_original:
        fila_copia: list[str] = []
        for elem in fila:
            fila_copia.append(elem)
        res.append(fila_copia)
    return res

#--------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 5 # TERMINADO
#--------------------------------------------------------------------------------------------------------------------------------------
# Si juego terminado = true o (fila, columna) es mina => fila y columna del tablero queda igual.
# Si era vacio, pasa a ser bandera, viceversa
def marcar_celda(estado: EstadoJuego, fila: int, columna: int) -> None:
    if estado['tablero_visible'][fila][columna] == VACIO:
        estado['tablero_visible'][fila][columna] = BANDERA
    elif estado['tablero_visible'][fila][columna] == BANDERA:
        estado['tablero_visible'][fila][columna] = VACIO
    elif estado['juego_terminado'] == True:
        return
    else:
        return

#--------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 6 # TERMINADO
#--------------------------------------------------------------------------------------------------------------------------------------
def descubrir_celda(estado: EstadoJuego, fila: int, columna: int) -> None:
    if estado ['juego_terminado']: # Si se encontró alguna mina o conseguimos ganar el juego, no se pueden descubrir mas.
        return
    tablero_visible: list[list[str]]      = estado ['tablero_visible']
    tablero: list[list[int]]              = estado ['tablero']
    if tablero [fila] [columna] == -1: # Si clickeamos una mina se termina el juego y muestra las posiciones de todas las minas
        estado ['juego_terminado'] = True
        tablero_visible = descubre_minas(tablero, tablero_visible)
    else:
        caminos: list[list[tuple[int,int]]] = caminos_descubiertos(tablero, tablero_visible, fila, columna)
        for camino in caminos:
            for filas, columnas in camino:
                if tablero_visible[filas][columnas] != BANDERA:
                    tablero_visible[filas][columnas] = str (tablero[filas][columnas]) # revela las casillas validas que no sean banderas
        if todas_celdas_seguras_descubiertas(estado['tablero'], estado['tablero_visible']):
            estado ['juego_terminado'] = True # si todas las casillas fueron reveladas, el juego termina

def caminos_descubiertos(tablero: list[list[int]], tablero_visible: list[list[str]], f: int, c: int) -> list[list[tuple[int,int]]]:
    res: list[list[tuple[int,int]]]         = []
    visitados: list[tuple[int,int]]         = [] # esta lista irá agregando elementos con el llamado de buscar_camino. por cada paso recursivo, la misma se vaciará (por eso se define dentro de esta función y no en buscar_camino)
    camino_actual: list[tuple[int,int]]     = []
    buscar_camino(tablero, tablero_visible, f, c, camino_actual, res, visitados)
    return res

#-------------------------------------------------------------------------------
# Funciones Auxiliares #
# Cambia todos los vacios en el tablero visible por un emoji de una bomba, si en esa casilla habia un -1 en el tablero real.
def descubre_minas(tablero_real: list[list[int]], tablero_visible: list[list[str]]) -> list[list[int]]:
    for i in range(len(tablero_real)):
        for j in range(len(tablero_real[0])):       # Recorremos ahora las posiciones de la cada fila
            if tablero_real[i][j] == -1:            # avanzamos en las columnas de cada fila
                tablero_visible[i][j] = BOMBA       # si es = -1 es BOMBA, finaliza el juego.
    return tablero_visible                          # retornamos el tablero visible. si se descubren bombas se retorna como quedó pero con las bombas descubiertas

def buscar_camino(tablero: list[list[int]], tablero_visible: list[list[str]], f: int, c: int, camino_actual: list[tuple[int,int]], caminos: list[list[tuple[int,int]]], visitados: list[tuple[int,int]]) -> None:
    if f < 0 or f >= len (tablero) or c < 0 or c >= len (tablero [0]):
        return # si la celda está en fuera de los límites del tablero no hay nada para revelar
    if tablero_visible[f][c] == BANDERA:
        return # si la celda es una bandera no se puede revelar
    if pertenece_lista(visitados, (f, c)):
        return # si ya fue descubierta la celda, no hay que revelarla
    valor: int                              = tablero[f][c]
    nuevos_visitados: list[tuple[int,int]]  = visitados + [(f, c)] # agregamos una celda descubierta
    nuevo_camino: list[tuple[int,int]]      = camino_actual + [(f, c)] # actualizamos el nuevo camino
    if valor > 0:
        caminos.append(nuevo_camino) # guardamos el camino
    elif valor == 0:
        revelados: int = 0 # contamos cuantas celdas adyacentes conseguimos revelar
        for fila in range(f-1,f+2): # analizamos las posiciones adyacentes a la celda seleccionada (las filas)
            for columna in range(c-1,c+2): # analizamos las posiciones adyacentes de cada fila (las columnas)
                if (fila != f or columna != c) and 0 <= fila < len(tablero) and 0 <= columna < len(tablero[0]): # verifica si es una posición válida para revelar
                    if not (pertenece_lista(nuevo_camino, (fila, columna))) and tablero_visible[fila][columna] != BANDERA:
                        if tablero[fila][columna] == 0:
                            buscar_camino(tablero, tablero_visible, fila, columna, nuevo_camino, caminos, nuevos_visitados) # llama a la recursión de a función para cada posición adyacente de la celda originalmente seleccionada
                            revelados += 1
                        elif tablero[fila][columna] > 0:
                            caminos.append(nuevo_camino + [(fila, columna)]) # si la celda es > 0 solo revelamos esa celda (sin recursión)
        if revelados == 0:
            caminos.append(nuevo_camino) # aunque no hayamos revelado ninguna celda, debemos guardar el camino, pues es una secuencia válida de descubrimiento

def pertenece_lista(l: list[tuple[int,int]], t: tuple[int,int]) -> bool:
    for fila, columna in l:
        if fila == t [0] and columna == t [1]:
            return True
    return False
#-------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 7 # TERMINADO
#--------------------------------------------------------------------------------------------------------------------------------------
def verificar_victoria(estado: EstadoJuego) -> bool:
    res: bool = False
    if todas_celdas_seguras_descubiertas(estado['tablero'], estado['tablero_visible']) == True:
        res = True
    return res

#--------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 8 # TERMINADO
#--------------------------------------------------------------------------------------------------------------------------------------
def reiniciar_juego(estado: EstadoJuego) -> None:
    filas: int                      = estado['filas']
    columnas: int                   = estado['columnas']
    minas: int                      = estado['minas'] # convocamos los elementos del diccionario
    nuevo_tablero: list[list[int]]  = colocar_minas (filas, columnas, minas) # creamos un nuevo tablero
    calcular_numeros(nuevo_tablero)
    while son_iguales_tableros(nuevo_tablero, estado['tablero']): # si crea un tablero igual a tablero@pre entonces que vuelva a crear tableros
        nuevo_tablero = colocar_minas(filas, columnas, minas)
        calcular_numeros(nuevo_tablero)
    estado['tablero'] = nuevo_tablero # reiniciamos el tablero con el nuevo tablero
    estado['tablero_visible'] = vaciar_matriz (nuevo_tablero)
    estado['juego_terminado'] = False

#-------------------------------------------------------------------------------
# Función Auxiliar #
def son_iguales_tableros(tablero_original: list[list[int]], tablero_nuevo: list[list[int]]) -> bool:
    for i in range(len(tablero_original)):
        for j in range(len(tablero_original[i])):
            if tablero_original[i][j] != tablero_nuevo[i][j]:
                return False
    return True
#-------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 9 # TERMINADO
#--------------------------------------------------------------------------------------------------------------------------------------
def guardar_estado(estado: EstadoJuego, ruta_directorio: str) -> None:                      # establece el directorio buscaminas_tp/save 
    columnas: int                   = estado['columnas']
    ruta_tablero_txt: str           = os.path.join(ruta_directorio, 'tablero.txt')          # establece el directorio del archivo tablero.txt
    ruta_tablero_visible_txt: str   = os.path.join(ruta_directorio, 'tablero_visible.txt')  # establece el directorio archivo tablero_visible.txt
    guardar_tablero(estado, ruta_tablero_txt, columnas)
    guardar_tablero_visible(estado, ruta_tablero_visible_txt, columnas)
    
#-------------------------------------------------------------------------------
# Funciones Auxiliares #
def guardar_tablero(estado: EstadoJuego, ruta_tablero_txt: str, columnas: int) -> None:
    archivo_tablero = open(ruta_tablero_txt, 'w')   # Abrimos el archivo para escribir
    for fila in estado['tablero']:
        for i in range(columnas):
            archivo_tablero.write(str(fila[i]))     # escribimos en el txt cada valor del tablero
            if i < columnas - 1:                    # si el numero no es el ultimo de la fila, agrega una coma a su derecha
                archivo_tablero.write(',')
        archivo_tablero.write('\n')                 # cuando se termina la fila, pasa a la siguiente
    archivo_tablero.close()
    
def guardar_tablero_visible(estado: EstadoJuego, ruta_tablero_visible_txt: str, columnas: int) -> None:
    archivo_tablero_visible = open(ruta_tablero_visible_txt, 'w')   # Abrimos el archivo para escribir
    for fila in estado['tablero_visible']:
        for i in range(columnas):
            if fila[i] == BANDERA:
                archivo_tablero_visible.write('*')
            elif fila[i] == VACIO:
                archivo_tablero_visible.write('?')
            else:
                archivo_tablero_visible.write(str(fila[i]))         # por el valor de la columna de cada fila, se fija si es  BANDERA o VACIO y pone el valor adecuado.
            if i < columnas - 1:
                archivo_tablero_visible.write(',')                  # si el numero no es el ultimo de la fila, agrega una coma a su derecha
        archivo_tablero_visible.write('\n')                         # cuando se termina la fila, pasa a la siguiente
    archivo_tablero_visible.close()
#-------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 10 # TERMINADO
#--------------------------------------------------------------------------------------------------------------------------------------
def cargar_estado(estado: EstadoJuego, ruta_directorio: str) -> bool:
    res: bool = False
    if (not existe_archivo(ruta_directorio, "tablero.txt")) or (not existe_archivo(ruta_directorio, "tablero_visible.txt")):  # verificamos que ambos archivos existan
        return res
    archivo_tablero     = open(os.path.join(ruta_directorio, "tablero.txt"), "r")
    tablero: list[str]  = []
    for linea in archivo_tablero: # iteramos en cada linea del archivo y listamos las lineas que sean válidas
        if linea_valida(linea):
            residuo: str    = ""
            i: int          = 0
            while i < len(linea):
                if linea[i] != '\n':
                    residuo += linea[i]
                i += 1
            tablero.append(residuo)
    archivo_tablero.close()
    archivo_tablero_visible     = open(os.path.join(ruta_directorio, "tablero_visible.txt"), "r")
    tablero_visible: list[str]  = []
    for linea in archivo_tablero_visible: # realizamos el mismo procedimiento pero con el tablero visible
        if linea_valida(linea):
            residuo: str    = ""
            i: int          = 0
            while i < len(linea):
                if linea[i] != '\n':
                    residuo += linea[i]
                i += 1
            tablero_visible.append(residuo)
    archivo_tablero_visible.close()
    if len(tablero) != len(tablero_visible) or len(tablero) == 0: # si no coinciden las longitudes de los tableros o son iguales a 0, no se puede cargar el estado
        return res
    cantidad_columnas: int = contar_columnas(tablero[0])
    i: int = 0
    while i < len(tablero): # verificamos que todas las filas de ambos archivos tengan la misma cantidad de columnas
        if contar_columnas(tablero[i]) != cantidad_columnas:
            return res
        if contar_columnas(tablero_visible[i]) != cantidad_columnas:
            return res
        i += 1
    nuevo_tablero: list[list[int]]            = [] # armamos nuevos tableros con los archivos de tablero y tablero visible ya revisados
    nuevo_tablero_visible: list[list[str]]    = []
    minas: int  = 0
    i: int      = 0
    while i < len(tablero): # armamos los nuevos tableros, iterando primero por los caracteres de tablero
        fila_tablero: list[int]            = []
        fila_tablero_visible: list[str]    = []
        linea: list[str]                   = armar_linea(tablero[i])
        linea_visible: list[str]           = armar_linea(tablero_visible[i])
        j: int = 0
        while j < cantidad_columnas:
            casillero: int = int (linea[j])
            if casillero == -1:
                minas += 1
            elif casillero < 0 or casillero > 8: # en caso de que no sea un casillero válido, devolvemos False
                return res
            fila_tablero.append(casillero)
            casillero_visible: str = linea_visible[j] # ahora iteramos en tablero visible
            if casillero_visible == BOMBA:
                if casillero != -1:
                    return res
                fila_tablero_visible.append(BOMBA)
            elif casillero_visible == BANDERA or casillero_visible == '*':
                fila_tablero_visible.append(BANDERA)
            elif casillero_visible == VACIO or casillero_visible == '?':
                fila_tablero_visible.append(VACIO)
            elif casillero_visible >= '0' and casillero_visible <= '8':
                if int(casillero_visible) != casillero:
                    return res
                fila_tablero_visible.append(casillero_visible)
            else:
                return res
            j += 1
        nuevo_tablero.append(fila_tablero) # una vez que iteramos en todos los caracteres de ambos tableros, los agregamos como filas de nuevo_tablero y nuevo_tablero_visible respectivamente
        nuevo_tablero_visible.append(fila_tablero_visible)
        i += 1
    if minas == 0:  # el tablero debe tener por lo menos una mina
        return res
    if not tablero_valido_minas(nuevo_tablero):
        return res
    estado["filas"]             = len(nuevo_tablero) # actualizamos el estado del juego
    estado["columnas"]          = cantidad_columnas
    estado["minas"]             = minas
    estado["tablero"]           = nuevo_tablero
    estado["tablero_visible"]   = nuevo_tablero_visible
    estado["juego_terminado"]   = todas_celdas_seguras_descubiertas(estado["tablero"], estado["tablero_visible"])
    if not estado_valido(estado): # verificamos que el estado sea válido
        return res
    return True

#-------------------------------------------------------------------------------
# Funciones Auxiliares #
def linea_valida(linea: str) -> bool: # verificamos que una linea sea válida (que no tenga saltos de renglón con '\n')
    i: int = 0
    while i < len(linea):
        if linea[i] != '\n' and linea[i] != ' ':
            return True
        i += 1
    return False

def contar_columnas(linea: str) -> int: # contamos las columnas de cada linea
    res: int    = 1
    i: int      = 0
    while i < len(linea):
        if linea[i] == ',':
            res += 1
        i += 1
    return res

def armar_linea(linea: str) -> list[str]: # enlistamos cada linea
    res: list[str]      = []
    contenedor: str     = ""
    i: int = 0
    while i < len(linea):
        if linea[i] == ',':
            res.append(contenedor)
            contenedor = ""
        elif linea[i] != '\n':
            contenedor += linea[i]
        i += 1
    res.append(contenedor)
    return res

def cantidad_minas_adyacentes(tablero: list[list[int]], f: int, c: int, filas: int, columnas: int) -> int: # Calcula la cantidad de minas alrededor de un casillero dado (f, c) en un tablero con determinadas filas y columnas
    cantidad: int = 0
    posiciones_adyacentes: list[tuple[int, int]] = [(f-1, c-1), (f-1, c), (f-1, c+1), # posiciones adyacentes de la fila superior del tablero
                                                    (f  , c-1),           (f,   c+1), # posiciones adyacentes en la misma fila
                                                    (f+1, c-1), (f+1, c), (f+1, c+1)] # posiciones adyacentes en la fila inferior
    i: int = 0
    while i < 8: # hay como mucho 8 posiciones adyacentes por celda
        pos_actual: tuple[int, int] = posiciones_adyacentes[i]
        if 0 <= pos_actual[0] < filas and 0 <= pos_actual[1] < columnas:
            if tablero[pos_actual[0]][pos_actual[1]] == -1:
                cantidad += 1
        i += 1
    return cantidad

def tablero_valido_minas(tablero: list[list[int]]) -> bool: # Verifica si el tablero es válido teniendo en cuenta que cada número debe coincidir con la cantidad de minas adyacentes.
    filas: int      = len(tablero)
    columnas: int   = len(tablero[0])
    i: int = 0
    while i < filas:
        j: int = 0
        while j < columnas:
            if tablero[i][j] != -1:
                minas_adyacentes: int = cantidad_minas_adyacentes(tablero, i, j, filas, columnas)
                if tablero[i][j] != minas_adyacentes: # Si el número en el tablero no coincide con la cantidad real, el tablero no es válido
                    return False
            j += 1
        i += 1
    return True
#-------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------