cantDigitos :: Int -> Int
cantDigitos n
    | n < 10 = 1
    |  n >= 10 = 1 + cantDigitos (div n 10)

iesimoDigito :: Int -> Int -> Int
iesimoDigito n digito = mod (div n (10 ^ (cantDigitos n - digito))) 10


esCapicua :: Int -> Bool
esCapicua n
    | n < 10 = True
    | iesimoDigito n (cantDigitos n) == iesimoDigito n ((cantDigitos n) - (cantDigitos n) + 1) = esCapicua (div (mod n (10 ^ (cantDigitos n - 1))) 10)
    | otherwise = False