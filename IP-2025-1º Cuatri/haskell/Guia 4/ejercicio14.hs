sumatoriaA :: Int -> Int -> Int
sumatoriaA n a 
    | a > n = 0
    | otherwise = a + sumatoriaA n (a + 1)

sumatoriaB :: Int -> Int -> Int
sumatoriaB n b 
    | b > n = 0
    | otherwise = b + sumatoriaB n (b + 1)

sumaPotencias :: Int -> Int -> Int -> Int
sumaPotencias q n m = q ^ ((sumatoriaA n 1) + (sumatoriaB m 1)) 