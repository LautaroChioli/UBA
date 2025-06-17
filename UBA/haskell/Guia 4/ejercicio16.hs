-- I

encontrarDivisor :: Int -> Int -> Int
encontrarDivisor n divisor
    | mod n divisor == 0 = divisor
    | otherwise = encontrarDivisor n (divisor + 1)

menorDivisor :: Int -> Int
menorDivisor n = encontrarDivisor n 2

-- II 

esPrimo :: Int -> Bool
esPrimo n
    | n == encontrarDivisor n 2 = True
    |otherwise = False

-- III
noTienenDivisor :: Int -> Int -> Int -> Bool
noTienenDivisor n m divisor
    | divisor > n = True
    | mod n divisor == 0 && mod m divisor == 0 = False
    | otherwise = True


sonCoprimos :: Int -> Int -> Bool
sonCoprimos n m = noTienenDivisor n m 2

-- IV
indicePrimo :: Int -> Int -> Int -> Int
indicePrimo numero indice enesimo
    | indice == enesimo = numero - 1
    | esPrimo numero = indicePrimo (numero + 1) (indice + 1) enesimo
    | otherwise = indicePrimo (numero + 1) indice enesimo


nEsimoPrimo :: Int -> Int
nEsimoPrimo n = indicePrimo 2 0 n 