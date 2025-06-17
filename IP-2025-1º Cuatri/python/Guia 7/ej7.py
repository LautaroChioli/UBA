# Implementar una funci´on que tome un entero d y otro p y eleve una matriz cuadrada de tama˜no d con
# valores generados al azar a la potencia p. Es decir, multiplique a la matriz generada al azar por s´ı misma p veces.
# Realizar experimentos con diferentes valores de d. ¿Qu´e pasa con valores muy grandes?
# problema exponenciacion matriz (in d:Z, in p:Z) : seq⟨seq⟨Z⟩⟩ {
# requiere: { d, p ∈ Z y d, p > 0 }
# asegura: { esM atriz(m) y |columna(m, 0)| = d y |columna(transponer(m), 0)| = d y res =
# Qp
# i=1 m }
# }

import numpy as np
import math
import time 


def exponenciacion_matriz(d, p):
    start_time = time.time()
    m = crear_matriz(d)
    print(m)
    cont = p
    while cont > 1:
        m = matriz_por_si_misma(m)
        cont -= 1
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(elapsed_time)
    return m


def crear_matriz(d):
    m = np.random.random((d, d))
    matriz = []
    fila_nueva = []
    for fila in m:
        for n in fila:
            fila_nueva.append(round(n*10))
        matriz.append(fila_nueva)
        fila_nueva = []       
    return matriz

def columna(matriz: list, columna: int) -> list:
    columna_n = []
    for fila in matriz:
        columna_n.append(fila[columna])
    return columna_n

def columnas(matriz: list,):
    columnas = []
    for i in range(0, len(matriz[0])):
        columnas.append(columna(matriz, i))
    return columnas

def matriz_por_si_misma(m):
    res = []
    fila_nueva = []
    columnas_m = columnas(m)
    for fila in m:
        for i in range(0,len(m)):
            fila_nueva.append(fila_por_columna(fila, columnas_m[i]))
        res.append(fila_nueva)
        fila_nueva = []
    return res
            
            
def fila_por_columna(fila, columna):
    res = 0
    for i in range(0, len(fila)):
        res += fila[i] * columna[i]
    return res

