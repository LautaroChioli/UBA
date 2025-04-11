suma :: Int -> Int
suma n
    | n == 0 = 0
    | otherwise = (2* n - 1) + suma (n - 1)


sumaImpares :: Int -> Int 
sumaImpares n
    | n == 0 = 0
    | n == 1 = 1
    | otherwise = suma n