fact :: Int -> Int
fact n
    | n == 0 = 1
    | n == 1 = 1
    | otherwise = n * fact (n-1)
    
eAprox :: Int -> Int -> Float
eAprox n inicio
    | inicio > n = 0
    | otherwise = 1/(fromIntegral (fact inicio)) + eAprox n (inicio + 1)