-- I

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece x (y:ys)
    | x == y = True
    | otherwise = pertenece x ys



-- II

compara :: (Eq t) => t -> [t] -> Bool
compara _ [] = True
compara x (y:ys)
    | x == y = compara x ys
    | otherwise = False

todosIguales :: (Eq t) => [t] -> Bool
todosIguales (x:xs) = compara x xs

-- III
comparaDistintos :: (Eq t) => t -> [t] -> Bool
comparaDistintos _ [] = True
comparaDistintos x (y:ys)
    | x == y = False
    | otherwise = comparaDistintos x ys

todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos (x:xs)
    | comparaDistintos x xs = todosDistintos xs
    | otherwise = False

--IV

comparaRepetidos :: (Eq t) => t -> [t] -> Bool
comparaRepetidos _ [] = False
comparaRepetidos x (y:ys)
    | x == y = True
    | otherwise = comparaRepetidos x ys

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs)
    | comparaRepetidos x xs = True
    | otherwise = hayRepetidos xs

--V

quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar t (x:xs)
    | x == t = xs
    | otherwise = x : quitar t xs

-- VI

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos t (x:xs)
    | x == t = quitarTodos t xs
    | otherwise = x : quitarTodos t xs

-- VII


quitarTodos2 :: (Eq t) => t -> [t] -> [t]
quitarTodos2 _ [] = []
quitarTodos2 t (x:xs)
    | x == t = quitarTodos2 t xs
    | otherwise = x : quitarTodos2 t xs

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) = x : eliminarRepetidos (quitarTodos x xs)

--- VIII

mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos [] m = True
mismosElementos (a:as) m
    | comparaElemConLista a m = mismosElementos as m
    | otherwise = False


comparaElemConLista :: (Eq t) => t -> [t] -> Bool
comparaElemConLista t (x:xs)
    | t == x = True
    | otherwise = comparaElemConLista t xs
comparaElemConLista t _ = False

comparaElemConLista2 :: (Eq t) => t -> [t] -> Bool
comparaElemConLista2 t (x:xs)
    | t == x = True
    | otherwise = comparaElemConLista2 t xs
comparaElemConLista2 t _ = False

-- IX

reverso :: [t] -> [t]
reverso [] = []
reverso (x:xs) = reverso xs ++ [x]

capicua :: (Eq t) => [t] -> Bool
capicua [] = True
capicua (x:xs)
    | reverso (x:xs) == (x:xs) = True
    | otherwise = False

