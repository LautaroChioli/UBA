-- I

longitud :: [t] -> Int
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

-- II

ultimo :: [t] -> t
ultimo [t] = t
ultimo (x:xs) = ultimo xs

-- III

principio :: [t] -> [t]
principio [t] = []
principio (x:xs) = x : principio xs

-- IV

reverso :: [t] -> [t]
reverso [] = []
reverso (x:xs) = reverso xs ++ [x]