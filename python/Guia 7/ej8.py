# Vamos a elaborar programas interactivos (usando la funci´on input() 3
# ) que nos permita solicitar al usuario
# informaci´on cuando usamos las funciones.

# 1. Implementar una funci´on para construir una lista con los nombres de mis estudiantes. La funci´on solicitar´a al usuario
# los nombres hasta que ingrese la palabra “listo”, o vac´ıo (el usuario aprieta ENTER sin escribir nada). Devuelve la
# lista con todos los nombres ingresados.

def nombres() -> list[str]:
    nombres = []
    nombre = "a"
    while nombre != "listo" and nombre != '':
        nombre = input()
        if nombre != "listo" and nombre != '': 
            nombres.append(nombre)
    return nombres



# 2. Implementar una funci´on que devuelve una lista con el historial de un monedero electr´onico (por ejemplo la SUBE).
# El usuario debe seleccionar en cada paso si quiere:
# “C” = Cargar cr´editos,
# “D” = Descontar cr´editos,
# “X” = Finalizar la simulaci´on (terminar el programa).
# En los casos de cargar y descontar cr´editos, el programa debe adem´as solicitar el monto para la operaci´on. Vamos a
# asumir que el monedero comienza en cero. Para guardar la informaci´on grabaremos en el historial tuplas que representen
# los casos de cargar (“C”, monto a cargar) y descontar cr´edito (“D”, monto a descontar).

def sube():
    carga = 0
    accion = ""
    historial = []
    while accion != 'X':
        accion = input("Que hacer: ")
        if accion == "C":
            carga_local = int(input("Cuanto? "))
            carga += carga_local
            historial.append(("C", carga_local))
            carga_local = 0
        if accion == "D":
            descarga_local = int(input("Cuanto? "))
            carga -= descarga_local
            historial.append(("D", descarga_local))
            descarga_local = 0
    return carga, historial
            
        

# 3. Vamos a escribir un programa para simular el juego conocido como 7 y medio. El mismo deber´a generar un n´umero
# aleatorio entre 0 y 12 (excluyendo el 8 y 9) y deber´a luego preguntarle al usuario si desea seguir sacando otra “carta”
# o plantarse. En este ´ultimo caso el programa debe terminar. Los n´umeros aleatorios obtenidos deber´an sumarse seg´un
# el n´umero obtenido salvo por las “figuras” (10, 11 y 12) que sumar´an medio punto cada una. El programa debe ir
# acumulando los valores y si se pasa de 7.5 debe informar que el usuario ha perdido. Al finalizar la funci´on devuelve
# el historial de “cartas” que hizo que el usuario gane o pierda. Para generar n´umeros pseudo-aleatorios entre 1 y 12
# utilizaremos la funci´on random.randint(1,12). Al mismo tiempo, la funci´on random.choice() puede ser de gran
# ayuda a la hora de repartir cartas.
import random

def siete_y_medio():
    total = 0
    cartas = genera_cartas()
    eleccion = ""
    sotas = [10, 11, 12]
    total_banca = total_de_la_banca()
    banca_perdio = False
    if total_banca == 0:
        banca_perdio = True
    while eleccion != "P" and total <= 7.5:
        eleccion = input("Que queres hacer? (P)lantarse o (C)arta? ")
        if eleccion == "C":
            carta = random.choice(cartas)
            if carta in sotas:
                total += 0.5
            else:
                total += carta
            print(f"Sacaste un {carta}, tu total es {total}")
        if eleccion == "P":
            if total > total_banca and banca_perdio:
                print(f"Ganaste, la banca se paso y vos no.")
            elif total > total_banca:
                print(f"Ganaste, tus {total} son mayores que los {total_banca} de la banca.")
            elif total == total_banca:
                print(f"Empate. {total} contra {total_banca}")
            else:
                print(f"Perdiste, los {total_banca} de la banca son mayores que tus {total}.")
    if total > 7.5:
        print(f"Te pasaste, pelotudo.")

def siete_y_medio_version_ejercicio():
    total = 0
    cartas = genera_cartas()
    eleccion = ""
    sotas = [10, 11, 12]
    total_banca = total_de_la_banca()
    banca_perdio = False
    historial = []
    if total_banca == 0:
        banca_perdio = True
    while eleccion != "P" and total <= 7.5:
        eleccion = input("Que queres hacer? (P)lantarse o (C)arta? ")
        if eleccion == "C":
            carta = random.choice(cartas)
            if carta in sotas:
                total += 0.5
            else:
                total += carta
            print(f"Sacaste un {carta}, tu total es {total}")
            historial.append(carta)
    if total > 7.5:
        print("Perdiste!")
        return historial


def total_de_la_banca():
    total = 0
    cartas = genera_cartas()
    sotas = [10,11,12]
    terminado = True
    while terminado:
        if total <= 6:
            carta = random.choice(cartas)
            if carta in sotas:
                total += 0.5
            else:
                total += carta
        elif total <= 7.5 and total > 6:
            terminado = False
        else:
            total = 0
            terminado = False
    return total
            
def genera_cartas():
    cont = 40
    cartas = []
    sin_8_o_9 = []
    while cont > 0:
        cartas.append(random.randint(1,12))
        cont -= 1
    for carta in cartas:
        if carta != 8 and carta != 9:
            sin_8_o_9.append(carta)
    return sin_8_o_9

# 4. Analizar la fortaleza de una contrase˜na. Solicitar al usuario que ingrese un texto que ser´a su contrase˜na. Armar una
# funci´on que tenga de par´ametro de entrada un string con la contrase˜na a analizar, y la salida otro string con tres
# posibles valores: VERDE, AMARILLA y ROJA. Nota: en python la “˜n/N” es considerado un car´acter especial y no ˜
# se comporta como cualquier otra letra. String es seq⟨Char⟩. Consejo: para ver si una letra es may´uscula se puede ver
# si est´a ordenada entre A y Z.
# La contrase˜na ser´a VERDE si:
# a) la longitud es mayor a 8 caracteres
# b) tiene al menos 1 letra min´uscula.
# c) tiene al menos 1 letra may´uscula.
# d) tiene al menos 1 d´ıgito num´erico (0..9)
# La contrase˜na ser´a ROJA si:
# a) la longitud es menor a 5 caracteres.
# En caso contrario ser´a AMARILLA


def analizar_contraseña():
    contraseña = input("Ingrese contraseña: ")
    cant_min = 0
    cant_may = 0
    cant_num = 0
    for letra in contraseña:
        if es_mayuscula(letra):
            cant_may += 1
        if es_numerico(letra):
            cant_num += 1
        if es_min(letra):
            cant_min += 1
    if (cant_min >= 1 )and (cant_may >= 1) and (cant_num >= 1) and (len(contraseña) >= 8):
        return "Verde"
    elif len(contraseña) < 5:
        return "Roja"
    else:
        return "Amarillo"
def es_mayuscula(letra):
    if 'A' <= letra <= 'Z':
        return True
    return False

def es_numerico(letra):
    if '0' <= letra <= '9':
        return True
    return False

def es_min(letra):
    if 'a' <= letra <= 'z':
        return True
    return False
