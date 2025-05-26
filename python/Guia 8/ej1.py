import random
from queue import LifoQueue as Pila


# Ejercicio 1. Implementar una soluci ́on para el siguiente problema.
# problema generar nros al azar (in cantidad: Z, in desde: Z, in hasta: Z) : Pila[Z] {
# requiere: {cantidad ≥0}
# requiere: {desde ≤hasta}
# asegura: {El tama ̃no de res es igual a cantidad}
# asegura: {Todos los elementos de res son valores entre desde y hasta (ambos inclusive), seleccionados aleatoriamente
# con probabilidad uniforme}
# }
# Para generar n ́umeros en un rango con probabilidad uniforme, pueden usar la funci ́on random.randint(< desde >, < hasta >)
# que devuelve un n ́umero en el rango indicado. Recuerden importar el m ́odulo random con import random. Adem ́as, pueden usar
# la clase LifoQueue() que es un ejemplo de una implementaci ́on b ́asica de una pila:
# from queue import LifoQueue as Pila #importa LifoQueue y le asigna el alias Pila
# p = Pila() #crea una pila
# p.put(1) # apila un 1
# elemento = p.get() # desapila
# p.empty () # devuelve true si y solo si la pila est ́a vac ́ıa

def generar_nros_al_azar(cant: int, desde: int, hasta:int) -> Pila[int]:
    pila = Pila()
    for i in range(0, cant):
        pila.put(random.randint(desde,hasta))
    imprimir_pila(pila)
    return pila

def imprimir_pila(p: Pila) -> None:
    auxiliar = Pila()
    elementos = []
    while not p.empty():
        elem = p.get()
        elementos.append(elem)
        auxiliar.put(elem)
    while not auxiliar.empty():
        p.put(auxiliar.get())

    print(elementos)

# Ejercicio 2. Implementar una soluci ́on para el siguiente problema.
# problema cantidad elementos (in p: Pila) : Z{
# requiere: {True}
# asegura: {res es igual a la cantidad de elementos que contiene p}
# }
# No se puede utilizar la funci ́on LifoQueue.qsize(). Tener en cuenta que, al usar get() para recorrer la pila, se modifica el
# par ́ametro de entrada, ya que los elementos se eliminan al accederse. Dado que la especificaci ́on lo define como de tipo in, debe
# restaurarse posteriormente.

def cantidad_elementos(pila: Pila) -> int:
    p = pila
    cont = 0
    while not p.empty():
        p.get()
        cont += 1
    return cont

# Ejercicio 3. Implementar una soluci ́on para el siguiente problema.
# problema buscar el maximo (in p: Pila[Z]) : Z{
# requiere: {p no est ́a vac ́ıa}
# asegura: {res es un elemento de p}
# asegura: {res es mayor o igual a todos los elementos de p}
# }

def buscar_el_maximo(pila: Pila[int]) -> int:
    p = pila
    maximo = p.get()
    while not p.empty():
        n_actual = p.get()
        if n_actual > maximo:
            maximo = n_actual
    return maximo
    

# print(buscar_el_maximo(p))

    


# Ejercicio 4. Implementar una soluci ́on para el siguiente problema.
# problema buscar nota maxima (in p: Pila[seq⟨Char⟩×Z]) : seq⟨Char⟩ ×Z{
# requiere: {p no est ́a vac ́ıa}
# requiere: {los elementos de p no tienen valores repetidos en la segunda posici ́on de las tuplas}
# asegura: {res es una tupla de p}
# asegura: {No hay ning ́un elemento en p cuya segunda componente sea mayor que la segunda componente de res }
# }

def buscar_nota_maxima(pila: Pila[(str, int)]) -> tuple[str, int]:
    p = pila
    maximo = p.get()[1]
    while not p.empty():
        actual = p.get()[1]
        if actual > maximo:
            maximo = actual
    return maximo
    
    

# Ejercicio 5. Implementar una soluci´on, que use pila, para el siguiente problema.
# problema esta bien balanceada (in s: seq⟨Char⟩) : Bool {
# requiere: {s solo puede tener n´umeros enteros, espacios y los s´ımbolos ’(’, ’)’, ’+’, ’-’, ’*’, ’/’}
# asegura: {res = true ↔ (La cantidad de par´entesis de apertura ’(´es igual a la de cierre ’)’) y (Para todo prefijo de ‘s‘,
# la cantidad de par´entesis de cierre no supera a la de apertura)}
# }
# Por cada par´entesis de cierre debe haber uno de apertura correspondiente antes de ´el. Las f´ormulas pueden tener:
# n´umeros enteros
# operaciones b´asicas +, −, ∗ y /
# par´entesis
# espacios
# Entonces las siguientes son f´ormulas aritm´eticas con sus par´entesis bien balanceados:
# 1 + ( 2 x 3 - ( 2 0 / 5 ) )
# 10 * ( 1 + ( 2 * ( -1)))
# Y la siguiente es una f´ormula que no tiene los par´entesis bien balanceados:
# 1 + ) 2 x 3 ( ( )

def esta_bien_balanceada(s: str) -> bool:
    p = Pila()
    cont = 0
    for c in s:
        if c == '(':
            p.put(c)
        elif c == ")":
            if p.empty():
                print(False)
                return False
            p.get()
    print(p.empty())
    return p.empty()
    


