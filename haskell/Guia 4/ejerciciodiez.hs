--I

potenciaDeDos :: Int -> Int -> Int
potenciaDeDos n i
    | i == n = 2 ^ n
    | otherwise = (2 ^ i) + potenciaDeDos n (i + 1)

-- II

potenciaDeX :: Int -> Float -> Int -> Float
potenciaDeX n x i 
    | i == n = x ** fromIntegral i
    | otherwise = (x ** fromIntegral i) + potenciaDeX n x (i + 1)


-- III

potenciaDeX2N :: Int -> Float -> Int -> Float
potenciaDeX2N n x i 
    | 2 * i == n = x ** fromIntegral i
    | otherwise = (x ** fromIntegral i) + potenciaDeX (2 * n) x (i + 1)

-- IV

potenciaDeNa2N :: Int -> Float -> Int -> Float
potenciaDeNa2N n x i 
    | i == (2 * n) = x ** fromIntegral i
    | otherwise = (x ** fromIntegral i) + potenciaDeNa2N n x (i + 1)