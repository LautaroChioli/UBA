def de_1_a_10() -> int:
    cont = 1
    while cont <= 10:
        print(cont)
        cont += 1

def pares_10_a_40() -> int:
    cont = 10
    while cont <= 40:
        if cont % 2 == 0:
            print(cont)
        cont += 1
        
def eco():
    cont = 0
    while cont < 10:
        print("eco")
        cont += 1

def cuenta_atras():
    cont = 10
    while cont != 0:
        print(cont)
        cont -= 1
    print("Despegue")

def viaje_temporal(partida: int, llegada: int):
    while partida > llegada:
        partida -= 1
        print(f"Año: {partida}")
    print("Llegamos")

def conocer_aristoteles(partida: int):
    while partida > -384:
        print(partida)
        partida -= 20
    print(f"Año de llegada: {partida}")
    print(f"Faltan {-385 - partida} años para el 384 a.C.")

