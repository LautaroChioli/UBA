-- EJERCICIO 1 (2 puntos)
-- problema mediaMovilN (lista: seq⟨Z⟩, n: Z) : Float {
--   requiere: {|lista| > 0}
--   requiere: {n > 0 ∧ n ≤ |lista|}
--   asegura: {res es el promedio de los últimos n elementos de lista}
-- }


mediaMovilN :: [Int] -> Int -> Float
mediaMovilN (elegido:resto) n
    | n == modulo (elegido:resto) = media (elegido:resto)
    | otherwise = mediaMovilN resto n

modulo :: [Int] -> Int
modulo [] = 0
modulo (elegido:resto) = 1 + modulo resto

media :: [Int] -> Float
media [] = 0
media lista = fromIntegral( (sumatoria lista)) / fromIntegral((modulo lista))

sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria (primero:resto) = primero + sumatoria resto


-- EJERCICIO 2 (2 puntos)    n>0
-- problema esAtractivo (n: Z) : Bool {
--   requiere: {n > 0}
--   asegura: {res = true <=> la cantidad de factores primos de n (distintos o no) es también un número primo.}
-- }
-- Aclaración: los factores primos de 30 son [5,3,2]. Los factores primos de 9 son [3,3]. 

esAtractivo :: Int -> Bool
esAtractivo n
    | esPrimo ( modulo ( factores )) = True
    | otherwise = False
    where factores = filtroDivisoresPrimos (factoresPrimos n 2)

factoresPrimos :: Int -> Int -> [Int]
factoresPrimos 1 _ = []
factoresPrimos n divisorInicial
    | mod n divisorInicial == 0 = divisorInicial :  factoresPrimos (div n divisorInicial) divisorInicial
    | otherwise = factoresPrimos n (divisorInicial + 1)

buscoDivisoresParaPrimos :: Int -> Int -> [Int]
buscoDivisoresParaPrimos 0 _ = []
buscoDivisoresParaPrimos n divisorInicial
    | divisorInicial == n = [n]
    | mod n divisorInicial == 0 = divisorInicial : buscoDivisoresParaPrimos n (divisorInicial + 1)
    | otherwise = buscoDivisoresParaPrimos n (divisorInicial + 1)

esPrimo :: Int -> Bool
esPrimo n
    | sumatoria (buscoDivisoresParaPrimos n 1) == (n + 1) = True
    | otherwise = False

filtroDivisoresPrimos :: [Int] -> [Int]
filtroDivisoresPrimos [] = []
filtroDivisoresPrimos (elegido:resto)
    | esPrimo elegido = elegido : filtroDivisoresPrimos resto
    | otherwise = filtroDivisoresPrimos resto

-- EJERCICIO 3 (2 puntos)
-- problema palabraOrdenada (palabra: seq⟨Char⟩) : Bool {
--   requiere: {True}
--   asegura: {res = true <=> cada uno de los elementos no blancos de palabra es mayor o igual al anterior caracter no blanco, si existe alguno.}
-- }
-- Aclaración: 'a' < 'b' es True. 

palabraOrdenada :: [Char] -> Bool
palabraOrdenada [] = True
palabraOrdenada [t] = True
palabraOrdenada palabra = prueboAscendencia ( palabraSinBlancos )
    where palabraSinBlancos = sacarBlancos palabra


sacarBlancos :: [Char] -> [Char]
sacarBlancos [] = []
sacarBlancos (elegido:resto)
    | elegido == ' ' = sacarBlancos resto
    | otherwise = elegido : sacarBlancos resto

prueboAscendencia :: [Char] -> Bool
prueboAscendencia [] = True
prueboAscendencia [t] = True
prueboAscendencia (elegida:siguiente:resto)
    | elegida <= siguiente = prueboAscendencia (siguiente:resto)
    | otherwise = False

-- EJERCICIO 4 (3 puntos)
-- problema similAnagrama (palabra1: seq⟨Char⟩, palabra2: seq⟨Char⟩) : Bool⟩{
--   requiere: {True}
--   asegura: {res = true <=> (para todo caracter no blanco, la cantidad de apariciones de ese caracter en palabra1 es igual a la cantidad de apariciones en palabra2, y además existe al menos un caracter en palabra1 que tiene una posición distinta en palabra2)}
-- }


similAnagrama :: [Char] -> [Char] -> Bool
similAnagrama [] [] = True
similAnagrama palabra1 palabra2
    | palabra1SB == palabra2SB = False
    | otherwise = prueboAnagrama palabra1SB palabra2SB
    where palabra1SB = sacarBlancos palabra1
          palabra2SB = sacarBlancos palabra2

prueboAnagrama :: [Char] -> [Char] -> Bool
prueboAnagrama [] [] = True
prueboAnagrama [] _ = False
prueboAnagrama _ [] = False
prueboAnagrama (elegido1:resto1) palabra2
    | (cantidadDeApariciones elegido1 (elegido1:resto1)) == (cantidadDeApariciones elegido1 (soloLetraDePalabra elegido1 palabra2)) = prueboAnagrama (eliminoLetraDePalabra elegido1 (elegido1:resto1) ) (eliminoLetraDePalabra elegido1 palabra2)
    | otherwise = False

cantidadDeApariciones :: Char -> [Char] -> Int
cantidadDeApariciones _ [] = 0
cantidadDeApariciones letra (primero:resto)
    | letra == primero = 1 + cantidadDeApariciones letra resto
    | otherwise = cantidadDeApariciones letra resto 

eliminoLetraDePalabra :: Char -> [Char] -> [Char]
eliminoLetraDePalabra _ [] = []
eliminoLetraDePalabra letra (primero:resto)
    | primero == letra = eliminoLetraDePalabra letra resto
    | otherwise = primero : eliminoLetraDePalabra letra resto

soloLetraDePalabra :: Char -> [Char] -> [Char]
soloLetraDePalabra _ [] = []
soloLetraDePalabra letra (primero:resto)
    | primero == letra = primero : soloLetraDePalabra letra resto
    | otherwise =  soloLetraDePalabra letra resto