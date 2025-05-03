{--

Un número natural es perfecto cuando la suma de sus divisores propios (números que lo dividen menores a él) es igual
al mismo número. Por ejemplo, 6 es un número perfecto porque la suma de sus divisores propios (1,2 y 3) es igual a 6.

Dos números naturales distintos son amigos si cada uno de ellos se obtiene sumando los divisores propios del otro.
Por ejemplo, 220 y 284 son amigos porque los divisores propios de 220 son 1,2,4,5,10,11,20,22,44,55,110 y sumados dan 284, y vice versa.

Entre comentarios las funciones buscadasa por el enunciado.

--}


-------------------
divisoresPropios :: Int -> [Int]
divisoresPropios n = buscoDivisores n 1
-----------------


buscoDivisores :: Int -> Int -> [Int]
buscoDivisores n primerDivisor
    | primerDivisor == n = []
    | mod n primerDivisor == 0 = primerDivisor : buscoDivisores n (primerDivisor + 1)
    | otherwise = buscoDivisores n (primerDivisor + 1)


------------
sonAmigos :: Int -> Int -> Bool
sonAmigos n m = igualdadDeSumaDeDivisores n m 
------------

igualdadDeSumaDeDivisores :: Int -> Int -> Bool
igualdadDeSumaDeDivisores n m
    | sumoDivisores (divisoresPropios n) == m && sumoDivisores (divisoresPropios m) == n = True 
    | otherwise = False

sumoDivisores :: [Int] -> Int
sumoDivisores [] = 0
sumoDivisores (primero:resto) = primero + sumoDivisores resto


----------
primerosNPerfectos :: Int -> [Int]
primerosNPerfectos n = buscoNPerfectos n 1 
-------------


esPerfecto :: Int -> Bool
esPerfecto 0 = False
esPerfecto n
    | sumoDivisores (divisoresPropios n) == n = True
    | otherwise = False

buscoNPerfectos :: Int -> Int -> [Int]
buscoNPerfectos 0 _ = []
buscoNPerfectos n actual
    | esPerfecto actual = actual : buscoNPerfectos (n - 1) (actual + 1)
    | otherwise = buscoNPerfectos n (actual + 1)





listaDeAmigos :: [Int] -> [(Int, Int)]
listaDeAmigos [] = []
listaDeAmigos (elegido:resto) = sacoTuplaCeroCero (buscoAmigoConRestoDeLista elegido resto : listaDeAmigos resto)

buscoAmigoConRestoDeLista :: Int -> [Int] -> (Int, Int)
buscoAmigoConRestoDeLista _ [] = (0,0)
buscoAmigoConRestoDeLista n (elegido:resto)
    | sonAmigos n elegido = (n, elegido)
    | otherwise = buscoAmigoConRestoDeLista n resto

sacoTuplaCeroCero :: [(Int,Int)] -> [(Int,Int)]
sacoTuplaCeroCero [] = []
sacoTuplaCeroCero (primerTupla:resto)
    | primerTupla == (0,0) = sacoTuplaCeroCero resto
    | otherwise = primerTupla : sacoTuplaCeroCero resto