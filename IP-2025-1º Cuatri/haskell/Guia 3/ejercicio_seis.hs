type Año = Int
type EsBisiesto = Bool

bisiesto :: Año -> EsBisiesto
bisiesto n
    | mod n 100 == 0 && mod n 400 /= 0 = False
    | mod n 400 == 0 = True
    | mod n 4 == 0 = True
    | otherwise = False

mensajeSiBisiesto :: Año -> String
mensajeSiBisiesto n
    | bisiesto n = "El anio " ++ show n ++ " es bisiesto"
    | otherwise = "El anio " ++ show n ++ " no es bisiesto"