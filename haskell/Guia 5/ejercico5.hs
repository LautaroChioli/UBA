-- I
sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [] = []
sumaAcumulada (x:xs) = x : sumaAcumuladaAux x xs

sumaAcumuladaAux :: (Num t) => t -> [t] -> [t]
sumaAcumuladaAux _ [] = []
sumaAcumuladaAux n (y:ys) = (n + y) : sumaAcumuladaAux (n + y) ys
