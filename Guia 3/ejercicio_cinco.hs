-- mismo ejercicio
f :: Int -> Int
f n 
    | n <= 7 = n*n
    | n > 7 = 2*n - 1

g :: Int -> Int
g n
    | mod n 2 == 0 = div n 2
    | otherwise = 3*n + 1

todosMenores :: Int -> Int -> Int -> Bool
todosMenores x y z
    | f x > g x && f y > g y && f z > g z = True
    | otherwise = False
--------------------------------------


