restar :: Int -> Int -> Bool
restar numero1 div1
    | numero1 - div1 == 0 = True
    | numero1 - div1 < 0 = False
    | otherwise = restar (numero1 - div1) div1

esDivisible :: Int -> Int -> Bool
esDivisible numero divisor
    | numero == 0 = True
    | otherwise = restar numero divisor