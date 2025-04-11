medioFact :: Int -> Int
factorial n
    | n == 0 = 1
    | n == 1 = 1
    | otherwise = n * factorial (n-2)


