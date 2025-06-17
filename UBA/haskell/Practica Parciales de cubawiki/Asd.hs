module Asd where

-- EJERCICIO 1 (2 puntos)
-- problema mediaMovilN (lista: seq⟨Z⟩, n: Z) : Float {
--   requiere: {|lista| > 0}
--   requiere: {n > 0 ∧ n ≤ |lista|}
--   asegura: {res es el promedio de los últimos n elementos de lista}
-- }

mediaMovilN :: [Int] -> Int -> Float
mediaMovilN [] _ = 0
mediaMovilN (x:xs) n
    | modulo (x:xs) == n = media (x:xs)
    | otherwise = mediaMovilN xs n

modulo :: [Int] -> Int
modulo [] = 0
modulo (x:xs) = 1 + modulo xs

sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

media :: [Int] -> Float
media [] = 0
media n = (fromIntegral (sumatoria n)) / (fromIntegral (modulo n))




-- EJERCICIO 2 (2 puntos)    n>0
-- problema esAtractivo (n: Z) : Bool {
--   requiere: {n > 0}
--   asegura: {res = true <=> la cantidad de factores primos de n (distintos o no) es también un número primo.}
-- }
-- Aclaración: los factores primos de 30 son [5,3,2]. Los factores primos de 9 son [3,3]. 


esAtractivo :: Int -> Bool
esAtractivo n
    | esPrimo(modulo (factoresDe n)) = True
    | otherwise = False


factoresDe :: Int -> [Int]
factoresDe n = factoresDeAux n 2

factoresDeAux :: Int -> Int -> [Int]
factoresDeAux 1 _ = []
factoresDeAux n divisor
    | mod n divisor == 0 = divisor : factoresDeAux (div n divisor) divisor
    | otherwise = factoresDeAux n (divisor + 1)

esPrimo :: Int -> Bool
esPrimo 0 = False
esPrimo n
    | (sumatoria (divisores n)) == (n + 1) = True
    | otherwise = False

divisores :: Int -> [Int]
divisores n = divisoresAux n 1

divisoresAux :: Int -> Int -> [Int]
divisoresAux n divisor
    | n == divisor = divisor : []
    | mod n divisor == 0 = divisor : divisoresAux n (divisor + 1)
    | otherwise = divisoresAux n (divisor + 1)


-- EJERCICIO 3 (2 puntos)
-- problema palabraOrdenada (palabra: seq⟨Char⟩) : Bool {
--   requiere: {True}
--   asegura: {res = true <=> cada uno de los elementos no blancos de palabra es mayor o igual al anterior caracter no blanco, si existe alguno.}
-- }
-- Aclaración: 'a' < 'b' es True. 

palabraOrdenada :: [Char] -> Bool
palabraOrdenada palabra = palabraOrdenadaAux (sacarBlancos palabra)

palabraOrdenadaAux :: [Char] -> Bool
palabraOrdenadaAux [] = True
palabraOrdenadaAux [t] = True
palabraOrdenadaAux (x:siguiente:xs)
    | x > siguiente = False
    | otherwise = palabraOrdenadaAux (siguiente:xs)


sacarBlancos :: [Char] -> [Char]
sacarBlancos [] = []
sacarBlancos (x:xs)
    | x == ' ' = sacarBlancos xs
    | otherwise = x : sacarBlancos xs


-- EJERCICIO 4 (3 puntos)
-- problema similAnagrama (palabra1: seq⟨Char⟩, palabra2: seq⟨Char⟩) : Bool⟩{
--   requiere: {True}
--   asegura: {res = true <=> (para todo caracter no blanco, la cantidad de apariciones de ese caracter en palabra1 es igual a la cantidad de apariciones en palabra2, y además existe al menos un caracter en palabra1 que tiene una posición distinta en palabra2)}
-- }


similAnagrama :: [Char] -> [Char] -> Bool
similAnagrama p1 p2
    | esIgual (sacarBlancos p1) (sacarBlancos p2) = False
    | otherwise = similAnagramaAux p1 p2


similAnagramaAux :: [Char] -> [Char] -> Bool
similAnagramaAux [] [] = True
similAnagramaAux [] _ = False
similAnagramaAux _ [] = False
similAnagramaAux (letra1:resto1) p2
    | ((moduloT (dejarLetra letra1 (sacarBlancos(letra1:resto1)))) == (moduloT (dejarLetra letra1 (sacarBlancos p2)))) = similAnagramaAux (sacoLetra letra1 (letra1:resto1)) (sacoLetra letra1 p2)
    | otherwise = False

moduloT :: [Char] -> Int
moduloT [] = 0
moduloT (x:xs) = 1 + moduloT xs

esIgual :: String -> String -> Bool
esIgual p1 p2
    | sacarBlancos p1 == sacarBlancos p2 = True
    | otherwise = False

letraEnPalabra :: Char -> [Char] -> Int
letraEnPalabra _ [] = 0
letraEnPalabra letra (x:xs)
    | letra == x = 1 + letraEnPalabra letra xs
    | otherwise = letraEnPalabra letra xs

dejarLetra :: Char -> [Char] -> [Char]
dejarLetra _ [] = []
dejarLetra le (x:xs)
    | le == x = le : dejarLetra le xs
    | otherwise = dejarLetra le xs

sacoLetra :: Char -> [Char] -> [Char]
sacoLetra _ [] = []
sacoLetra le (x:xs)
    | le == x =  sacoLetra le xs
    | otherwise = x : sacoLetra le xs

