potenciaDeDos :: Int -> Int -> Int
potenciaDeDos n i
    | i == n = 2 ^ n
    | otherwise = (2 ^ i) + potenciaDeDos n (i + 1)
raizDe2Aprox :: Int -> Float
raizDe2Aprox 1 = 2
raizDe2Aprox n = (serieRaizDe2Aprox n ) - 1
