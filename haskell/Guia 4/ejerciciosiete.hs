cantDigitos :: Int -> Int
cantDigitos n
  | n < 10    = 1
  | otherwise = 1 + cantDigitos (div n 10)

iesimoDigito :: Int -> Int -> Int
iesimoDigito n digito = mod (div n (10 ^ (cantDigitos n - digito))) 10
