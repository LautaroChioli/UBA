parteEntera :: Float -> Int
parteEntera n
    | mod n 1 == 0 = 4
    |otherwise = n - mod n 1