# Ejercicio 8. Implementar una soluci´on para el siguiente problema.
# problema generar nros al azar (in cantidad: Z, in desde: Z, in hasta: Z) : Cola[Z] {
# requiere: {cantidad ≥ 0}
# requiere: {desde ≤ hasta}
# asegura: {El tama˜no de res es igual a cantidad}
# asegura: {Todos los elementos de res son valores entre desde y hasta (ambos inclusive), seleccionados aleatoriamente
# con probabilidad uniforme}
# }
# Para generar n´umeros en un rango con probabilidad uniforme, pueden usar la funci´on random.randint(< desde >, < hasta >)
# que devuelve un n´umero en el rango indicado. Recuerden importar el m´odulo random con import random. Pueden usar la clase
# Queue() que es un ejemplo de una implementaci´on b´asica de una Cola:
# from queue import Queue as Cola # importa Queue y le asigna el alias Cola
# c = Cola () # creo una cola
# c . put (1) # encolo el 1
# elemento = c . get () # desencolo
# c . empty () # devuelve true si y solo si la cola est ´a vac ´ı a
from queue import Queue as Cola
import random

def generar_nros_al_azar(cantidad: list[int], desde, hasta) -> Cola[int]:
    c = Cola()
    for i in range(cantidad):
        c.put(random.randint(desde, hasta))
    print_cola(c)
    return c

def print_cola(cola):
    c = cola
    s = []
    while not c.empty():
        s.append(c.get())
    print(s)
    return s

# Ejercicio 9. Implementar una soluci´on para el siguiente problema.
# problema cantidad elementos (in c: Cola) : Z {
# requiere: {True}
# asegura: {res es igual a la cantidad de elementos que contiene c}
# }

def cantidad_elementos(cola):
    c = cola
    cont = 0
    while not c.empty():
        cont += 1
        c.get()
    return cont


# Ejercicio 10. Implementar una soluci´on para el siguiente problema.
# problema buscar el maximo (in c: Cola[Z]) : Z {
# requiere: {c no est´a vac´ıa}
# asegura: {res es un elemento de c}
# asegura: {res es mayor o igual a todos los elementos de c}
# }

def buscar_el_maximo(cola: Cola[int]):
    c = cola
    max = c.get()
    while not c.empty():
        n_actual = c.get()
        if n_actual > max:
            max = n_actual
    return max



# Ejercicio 11. Implementar una soluci´on para el siguiente problema.
# problema buscar nota minima (in c: Cola[seq⟨Char × Z⟩]) : (seq⟨Char × Z⟩) {
# requiere: {c no est´a vac´ıa}
# requiere: {los elementos de c no tienen valores repetidos en la segunda componente de las tuplas}
# asegura: {res es una tupla de c}
# asegura: {No hay ning´un elemento en c cuya segunda componente sea menor que la de res }
# }

def buscar_nota_minima(cola: Cola):
    c = cola
    min = c.get()[1]
    while not c.empty():
        n = c.get()[1]
        if n < min:
            min = n
    return min 




# Ejercicio 12. Implementar una soluci´on para el siguiente problema.
# problema intercalar (in c1: Cola, in c2: Cola) : Cola {
# requiere: {c1 y c2 tienen la misma cantidad de elementos}
# asegura: {res solo contiene los elementos de c1 y c2}
# asegura: {res contiene todos los elementos de c1 y c2, intercalados y respetando el orden original}
# asegura: {El primer elemento de res es el primer elemento de c1}
# asegura: {El tama˜no de res es igual al doble del tama˜no de c1}
# }

def intercalar(cola1: Cola, cola2: Cola) -> Cola:
    cola3 = Cola()
    while not cola2.empty():
        cola3.put(cola1.get())
        cola3.put(cola2.get())
    return cola3

c = Cola()
c.put(1)
c.put(2)
c.put(3)
d = Cola()
d.put(4)
d.put(5)
d.put(6)

# Ejercicio 13. Bingo: un cart´on de bingo contiene 12 n´umeros al azar en el rango [0, 99]. Implementar una soluci´on para cada
# uno de los siguientes problemas.
# 1. problema armar secuencia de bingo () : Cola[Z] {
# requiere: {True}
# asegura: {res solo contiene 100 n´umeros del 0 al 99 inclusive, sin repetidos}
# asegura: {Los n´umeros de res est´an ordenados al azar}
# }
# Para generar n´umeros pseudoaleatorios pueden usar la funci´on random.randint(< desde >, < hasta >) que devuelve un
# n´umero en el rango indicado. Recuerden importar el m´odulo random con import random.

def armar_secuencia_de_bingo() -> Cola[int]:
    numeros_elegidos = []
    res = Cola()
    while len(numeros_elegidos) != 100:
        numero = random.randint(0,99)
        if numero not in numeros_elegidos:
            res.put(numero)
            numeros_elegidos.append(numero)
    return res


    

# 2. problema jugar carton de bingo (in carton: seq⟨Z⟩, in bolillero: Cola[Z]) : Z {
# requiere: {carton solo contiene 12 n´umeros, sin repetidos, con valores entre 0 y 99, ambos inclusive}
# requiere: {bolillero solo contiene 100 n´umeros, ordenados al azar, del 0 al 99, ambos inclusive, sin repetidos}
# asegura: {res es la cantidad m´ınima de jugadas necesarias para que todos los n´umeros del carton hayan salido del
# bolillero}
# }

def jugar_carton_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    jugadas = 0
    numeros_marcados = []
    while len(numeros_marcados) < 13:
        jugadas += 1
        bola_actual = bolillero.get()
        if bola_actual in carton:
            numeros_marcados.append(bola_actual)
    return jugadas
            
            
def crear_carton():
    carton = []
    while len(carton) < 13:
        n = random.randint(0,99)
        if n not in carton:
            carton.append(n)
    return carton

# Ejercicio 14. Vamos a modelar una guardia de un hospital usando una cola donde se van almacenando los pedidos de atenci´on
# para los pacientes que van llegando. A cada paciente se le asigna una prioridad del 1 al 10 (donde la prioridad 1 es la m´as urgente
# y requiere atenci´on inmediata) junto con su nombre y la especialidad m´edica que le corresponde. Implementar una soluci´on para
# el siguiente problema.
# problema pacientes urgentes (in c:Cola[Z× seq⟨Char⟩ × seq⟨Char⟩]) : Z {
# requiere: {Todos los elementos de c tienen como primer componente de la tupla un entero positivo y menor a 11}
# asegura: {res es la cantidad de elementos de c que tienen como primer componente de la tupla un n´umero menor a 4}
# }



# Ejercicio 15. La gerencia de un banco nos pide modelar la atenci´on de los clientes usando una cola donde se van registrando
# los pedidos de atenci´on. Cada vez que ingresa una persona a la entidad, debe completar sus datos en una pantalla que est´a a la
# entrada: Nombre y Apellido, DNI, tipo de cuenta (true si es preferencial o f alse en el caso contrario) y si tiene prioridad (true
# o f alse) por ser adulto +65, embarazada o con movilidad reducida.
# La atenci´on a los clientes se da por el siguiente orden: primero las personas que tienen prioridad, luego las que tienen cuenta
# bancaria preferencial y por ´ultimo el resto. Dentro de cada subgrupo de clientes, se respeta el orden de llegada.
# 1. Dar una especificaci´on para el problema planteado.
# 2. Implementar atencion a clientes(in c : Cola[tuple[str, int, bool, bool]]) → Cola[tuple[str, int, bool, bool]] que dada la cola de ingreso de clientes al banco devuelve la cola en la que van a ser atendidos.
