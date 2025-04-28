-- I

sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [t] = [t]
sacarBlancosRepetidos (x:y:xs)
    | x == ' ' && y == ' ' = sacarBlancosRepetidos (y:xs)
    | otherwise = x : sacarBlancosRepetidos (y:xs)

-- II

contarPalabras :: [Char] -> Int 
contarPalabras [] = 0
contarPalabras [t] 
    | t == ' ' = 0
    | t /= ' ' = 1
contarPalabras (x:y:xs)
    | x /= ' ' && y == ' ' = 1 + contarPalabras (y:xs)
    | otherwise = contarPalabras (y:xs)

--III

palabras :: [Char] -> [[Char]]
palabras [] = []
palabras xs = primera xs : palabras (resto xs)

primera :: [Char] -> [Char]
primera [] = []
primera (x:xs)
    | x == ' '  = []
    | otherwise = x : primera xs

resto :: [Char] -> [Char]
resto [] = []
resto (x:xs)
    | x == ' '  = sinEspacios xs
    | otherwise = resto xs

sinEspacios :: [Char] -> [Char]
sinEspacios [] = []
sinEspacios (x:xs)
    | x == ' '  = sinEspacios xs
    | otherwise = x:xs

--IV

palabraMasLarga :: [Char] -> [Char]
palabraMasLarga [x] = [x]
palabraMasLarga xs = compararPalabras (primera2 (palabras xs)) (palabras xs)

compararPalabras :: [Char] -> [[Char]] -> [Char]
compararPalabras [] [] = []
compararPalabras t [] = t
compararPalabras [] (x:xs) = compararPalabras x xs
compararPalabras t (x:xs) 
    | largoPalabra t >= largoPalabra x = compararPalabras t xs
    | otherwise = compararPalabras x xs

largoPalabra :: [Char] -> Int
largoPalabra [] = 0
largoPalabra (x:xs) = 1 + largoPalabra xs
    
primera2 :: [[Char]] -> [Char]
primera2 [] = []
primera2 (x:xs) = x