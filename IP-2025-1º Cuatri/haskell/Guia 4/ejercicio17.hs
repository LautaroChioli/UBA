fibonacci :: Int -> Int
fibonacci n
    | n == 0 = 0
    | n == 1 = 1
    | otherwise = fibonacci (n - 1) + fibonacci (n - 2)

fibonacci2 :: Int -> Int -> Int
fibonacci2 n buscado
    | fibonacci n == buscado = -1
    | fibonacci n  > buscado  = -2
    | otherwise = fibonacci2 (n + 1) buscado



esFibonacci :: Int -> Bool
esFibonacci n = fibonacci2 0 n == -1