sumatoriaM :: Int -> Int -> Int -> Int
sumatoriaM m j i 
    | j > m = 0 
    | otherwise = (i ^ j) + sumatoriaM m (j + 1) i

sumatoriaN :: Int -> Int -> Int -> Int
sumatoriaN i n m
    | i > n = 0
    | otherwise = sumatoriaM i 1 m + sumatoriaN (i + 1) n m 

sumatoriaTotal :: Int -> Int -> Int
sumatoriaTotal n m = sumatoriaN 1 n m