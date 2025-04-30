-- I
sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [] = []
sumaAcumulada (x:xs) = x : sumaAcumuladaAux x xs

sumaAcumuladaAux :: (Num t) => t -> [t] -> [t]
sumaAcumuladaAux _ [] = []
sumaAcumuladaAux n (y:ys) = (n + y) : sumaAcumuladaAux (n + y) ys


-- Ejercicio 2

descomponerEnPrimos :: [Int] -> [[Int]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs) = [(buscarPrimos x [1..x])] ++ descomponerEnPrimos xs

buscarPrimos :: Int -> [Int] -> [Int]
buscarPrimos _ [] = []
buscarPrimos n (x:xs)
    | mod n x == 0 && verEsPrimo x && x /= 1 = x : buscarPrimos n xs
    | otherwise = buscarPrimos n xs

sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

verEsPrimo :: Int -> Bool
verEsPrimo 0 = False
verEsPrimo 1 = False
verEsPrimo n
    | sumatoria (divisoresTodos n [1..n]) == n + 1 = True
    | otherwise = False

divisoresTodos :: Int -> [Int] -> [Int]
divisoresTodos _ [] = []
divisoresTodos 0 _  = []
divisoresTodos n (x:xs)
    | mod n x == 0 = x : divisoresTodos n xs
    | otherwise = divisoresTodos n xs
    