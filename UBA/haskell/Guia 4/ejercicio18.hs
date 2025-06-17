<<<<<<< HEAD
cantDigitos :: Int -> Int
cantDigitos n
  | n < 10    = 1
  | otherwise = 1 + cantDigitos (div n 10)

iesimoDigito :: Int -> Int -> Int
iesimoDigito n digito = mod (div n (10 ^ (cantDigitos n - digito))) 10

<<<<<<< HEAD
=======
mayorDigitoPar :: Int -> Int
mayorDigitoPar n
>>>>>>> b1a8cc786aaf0b052a95437a624e1fa8a3fe0cf9

mayorPar :: Int -> Int -> Int
mayorPar n maximo
  | n == 0 = maximo
<<<<<<< HEAD
  | mod n 2 == 0 && maximo < mod n 10 = mayorPar (div n 10) (mod n 10)
  | otherwise = mayorPar (div n 10) maximo
=======
  | mod n 2 == 0 && maximo < n = mayorPar (div n 10) (mod n 10)
   | otherwise = mayorPar (div n 10) maximo
>>>>>>> b1a8cc786aaf0b052a95437a624e1fa8a3fe0cf9
=======
cantDigitos :: Int -> Int
cantDigitos n
  | n < 10    = 1
  | otherwise = 1 + cantDigitos (div n 10)

iesimoDigito :: Int -> Int -> Int
iesimoDigito n digito = mod (div n (10 ^ (cantDigitos n - digito))) 10

<<<<<<< HEAD
=======
mayorDigitoPar :: Int -> Int
mayorDigitoPar n
>>>>>>> b1a8cc786aaf0b052a95437a624e1fa8a3fe0cf9

mayorPar :: Int -> Int -> Int
mayorPar n maximo
  | n == 0 = maximo
<<<<<<< HEAD
  | mod n 2 == 0 && maximo < mod n 10 = mayorPar (div n 10) (mod n 10)
  | otherwise = mayorPar (div n 10) maximo
=======
  | mod n 2 == 0 && maximo < n = mayorPar (div n 10) (mod n 10)
   | otherwise = mayorPar (div n 10) maximo
>>>>>>> b1a8cc786aaf0b052a95437a624e1fa8a3fe0cf9
>>>>>>> 553ab75774bd751d24e754893a51d72c7e48e07b
