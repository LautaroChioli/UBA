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

--