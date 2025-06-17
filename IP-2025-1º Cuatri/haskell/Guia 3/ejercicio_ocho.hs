----------------------------
absoluto :: Int -> Int
absoluto n 
    | n < 0 = -n
    | otherwise = n

sumaUltimosDosDigitos :: Int -> Int
sumaUltimosDosDigitos n = mod (absoluto n) 10 + mod (absoluto (div n 10)) 10


comparar :: Int -> Int -> Int
comparar n m
    | sumaUltimosDosDigitos n  <  sumaUltimosDosDigitos m = 1
    | sumaUltimosDosDigitos n  > sumaUltimosDosDigitos m = -1
    | sumaUltimosDosDigitos n == sumaUltimosDosDigitos m = 0

--------------------------------------

