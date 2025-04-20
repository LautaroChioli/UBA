-- I

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece t [] = False
pertenece t (x:xs)
    | x == t = True
    | [x] == [] = False
    | otherwise = pertenece t xs


-- II

todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales (x:xs)
    | [x]== todosIguales xs = True 
    | otherwise = False