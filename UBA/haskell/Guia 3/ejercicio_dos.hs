absoluto :: Int -> Int
absoluto n 
    | n < 0 = -n
    | otherwise = n

maximoDeAbsolutos :: Int -> Int -> String
maximoDeAbsolutos n m
    | absoluto n > absoluto m = "n mayor que m"
    | absoluto n < absoluto m = "m mayor que n"


maximoDeTres :: Int -> Int -> Int -> String
maximoDeTres x y z
    | x > y && x > z = "El primer numero es el mayor"
    | y > z && y > x = "El segundo numero es el mayor"
    | otherwise = "El tercer numero es el mayor"

algunoEsCeroGuards :: Int -> Int -> String
algunoEsCeroGuards n m 
    | n == 0 || m == 0 = "Uno de los dos numeros es cero"
    | otherwise = "Ninguno es cero"

algunoEsCeroPattern :: Int -> Int -> String
algunoEsCeroPattern 0 m = "Uno es cero"
algunoEsCeroPattern n 0 = "Uno es cero"
algunoEsCeroPattern n m = "Ninguno es cero"

ambosSonCeroGuards :: Int -> Int -> String
ambosSonCeroGuards n m
    | n == 0 && m == 0 = "Ambos son cero"
    | otherwise = "Uno de los dos no es cero"

ambosSonCeroPattern :: Int -> Int -> String
ambosSonCeroPattern 0 0 = "Ambos son cero"
ambosSonCeroPattern n m = "Uno de los dos no es cero"

enMismoIntervalo :: Float -> String
enMismoIntervalo n
    | n <= 3 = "Entre menos infinito y tres, incluido."
    | n <= 7 = "Entre tres y siete, incluido."
    | otherwise = "Entre siete y mas infinito"

sumaDistintos :: Int -> Int -> Int -> Int
sumaDistintos x y z
    | x == y = x +z
    | x == z = x + y
    | otherwise = x + y

esMultiploDe :: Int -> Int -> String
esMultiploDe n m 
    |mod m n == 0 = "El primero es multiplo del segundo"
    | otherwise = "El primero no es multiplo del segundo"

digitoUnidades :: Int -> Int
digitoUnidades n = mod (absoluto n) 10

digitoDecenas :: Int -> Int
digitoDecenas n = mod ( div (absoluto n) 10) 10

