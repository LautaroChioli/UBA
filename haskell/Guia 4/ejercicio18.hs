cantDigitos :: Int -> Int
cantDigitos n
  | n < 10    = 1
  | otherwise = 1 + cantDigitos (div n 10)

iesimoDigito :: Int -> Int -> Int
iesimoDigito n digito = mod (div n (10 ^ (cantDigitos n - digito))) 10

mayorDigitoPar :: Int -> Int
mayorDigitoPar n

mayorPar :: Int -> Int -> Int
mayorPar n maximo
  | n == 0 = maximo
  | mod n 2 == 0 && maximo < n = mayorPar (div n 10) (mod n 10)
   | otherwise = mayorPar (div n 10) maximo
