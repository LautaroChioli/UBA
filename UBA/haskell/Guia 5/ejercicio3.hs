--I

sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

-- II

productoria :: [Int] -> Int
productoria [] = 1
productoria (x:xs) = x * productoria xs

--III

maximo :: [Int] -> Int
maximo [x] = x
maximo (x:xs) 
    | x >= maximo xs = x
    | otherwise = maximo xs 

--IV

sumarN :: Int -> [Int] -> [Int]
sumarN n [] = []
sumarN n (x:xs) = (x + n) : sumarN n xs

--V

sumarElPrimero :: [Int] -> [Int]
sumarElPrimero (x:xs) = sumarN x (x:xs)

--VI

ultimo :: [t] -> t
ultimo [t] = t
ultimo (x:xs) = ultimo xs

sumarElUltimo :: [Int] -> [Int]
sumarElUltimo (x:xs) = sumarN (ultimo (x:xs)) (x:xs)

-- VII

pares :: [Int] -> [Int]
pares [] = []
pares (x:xs)
    | mod x 2 == 0 = x : pares xs
    | otherwise = pares xs

-- VIII

multiplosDeN :: Int -> [Int] -> [Int]
multiplosDeN _ [] = []
multiplosDeN a (x:xs)
    | mod x a == 0 && x /= 0 = x : multiplosDeN a xs
    | otherwise = multiplosDeN a xs

