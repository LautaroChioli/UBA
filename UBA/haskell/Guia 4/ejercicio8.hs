
sumaDigitos :: Int -> Int 
sumaDigitos n
    | n == 0 = 0
    | otherwise = mod n 10 + sumaDigitos (div n 10 )