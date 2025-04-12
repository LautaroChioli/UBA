contarDesde0 :: Float -> Int -> Int
contarDesde0 n inicio
    | fromIntegral inicio <= n && n < fromIntegral (inicio + 1) = inicio
    | otherwise = contarDesde0 n (inicio + 1)

parteEntera :: Float -> Int
parteEntera n
  | n < 1     = 0
  | otherwise = contarDesde0 n 0