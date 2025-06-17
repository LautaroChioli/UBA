type Posicion = (Int, Int)
type Fila = [Int]
type Tablero = [Fila]
type Camino = [Posicion]
type Columna = [Int]
{--                                                              0     1    2
tablero =  [[1,20,3], [1,2,25], [4, 3, 5]]  ---------->      0 |  1 | 20 |  3 | 
                                                             1 |  1 |  2 | 25 |
                                                             2 |  4 |  3 |  5 |

camino =    [[1,20,3], [1,2,25], [4, 3, 5]] [(0,0),(0,1), (1,1),(1,2),(2,2)]
Marcado entre comentarios las funciones principales que pide el enunciado.
--}

-------
maximo :: Tablero -> Int
maximo [] = 0
maximo (fila:restoFilas)
    |  maximoDeFila fila > maximo restoFilas = maximoDeFila fila
    | otherwise = maximo restoFilas
-------


maximoDeFila :: Fila -> Int
maximoDeFila [] = 0
maximoDeFila (primero:resto)
    | primero > maximoDeFila resto = primero
    | otherwise = maximoDeFila resto


----------------
masRepetido :: Tablero -> Int
masRepetido [] = 0
masRepetido tablero = masRepetidoDeLista ( listaDeListasALista tablero )
-----------------


listaDeListasALista :: Tablero -> [Int]
listaDeListasALista [] = []
listaDeListasALista (fila1:restoFilas) = fila1 ++ listaDeListasALista restoFilas

masRepetidoDeLista :: [Int] -> Int
masRepetidoDeLista [] = 0
masRepetidoDeLista [t] = t
masRepetidoDeLista (numero:resto)
    | cantidadDeVecesEnLista numero (numero:resto) >= cantidadDeVecesEnLista (masRepetidoDeLista (sacar numero resto)) resto =  numero
    | otherwise = masRepetidoDeLista resto

sacar :: Int -> [Int] -> [Int]
sacar _ [] = []
sacar n (primerN:restoN)
    |   n == primerN = sacar n restoN
    |   otherwise = primerN : sacar n restoN

cantidadDeVecesEnLista :: Int -> [Int] -> Int
cantidadDeVecesEnLista _ [] = 0
cantidadDeVecesEnLista n (numero:resto)
    | n == numero = 1 + cantidadDeVecesEnLista n resto
    | otherwise = cantidadDeVecesEnLista n resto


------------------
valoresDeCamino :: Tablero -> Camino -> [Int]
valoresDeCamino [] _ = []
valoresDeCamino _ [] = []
valoresDeCamino tablero (pasoActual:siguientesPasos) = numeroEnXY pasoActual tablero : valoresDeCamino tablero siguientesPasos
------------------

numeroEnXY :: Posicion -> Tablero -> Int
numeroEnXY _ [] = 0
numeroEnXY (x, y) tablero = buscarPosicionEnFila x (buscarFila y (tablero))

buscarFila :: Int -> Tablero -> Fila
buscarFila _ [] = []
buscarFila 0 (fila:_) = fila
buscarFila y (fila:restoFilas) = buscarFila (y-1) restoFilas

buscarPosicionEnFila :: Int -> Fila -> Int
buscarPosicionEnFila 0 (primer:resto) = primer
buscarPosicionEnFila x (primer:resto) = buscarPosicionEnFila (x-1) resto


--------------------------
esCaminoFibo :: [Integer] -> Integer -> Bool
esCaminoFibo [] _ = False
esCaminoFibo camino i = verificoFibo camino (fib i) (fib (i + 1))
---------------------------


fib :: Integer -> Integer
fib 0 = 0
fib 1 = 1
fib n = fib (n - 1) + fib (n - 2)

verificoFibo :: [Integer] -> Integer -> Integer -> Bool
verificoFibo [] _ _ = True
verificoFibo (x:xs) a b
  | x /= a = False
  | otherwise = verificoFibo xs b (a + b)