masRepetido :: [Char] -> Char
masRepetido (primeraLetra:resto) = masRepetidoAUX (primeraLetra:resto) primeraLetra (contar primeraLetra (primeraLetra:resto)) 

contar :: Char -> [Char] -> Int
contar _ [] = 0
contar letra (primera:resto)
    | letra == primera = 1 + contar letra resto
    | otherwise = contar letra resto

sacar :: Char -> [Char] -> [Char]
sacar _ [] = []
sacar letra (x:xs)
    | letra == x = sacar letra xs
    | otherwise = x : sacar letra xs

masRepetidoAUX :: [Char] -> Char -> Int -> Char
masRepetidoAUX [] letra _ = letra
masRepetidoAUX (primeraLetra:resto) letra masVeces
    | contar primeraLetra (primeraLetra:resto) >= masVeces = masRepetidoAUX (sacar primeraLetra (primeraLetra:resto)) primeraLetra (contar primeraLetra (primeraLetra:resto))
    | otherwise = masRepetidoAUX (sacar primeraLetra(primeraLetra:resto)) letra masVeces

buscoFactores :: Int -> [Int]
buscoFactores numero = factoresPrimos numero 2

factoresPrimos :: Int -> Int -> [Int]
factoresPrimos 1 _ = []
factoresPrimos numero divisor
    | mod numero divisor == 0 = divisor : factoresPrimos (div numero divisor) divisor
    | otherwise = factoresPrimos numero (divisor + 1)