-- tuplas y listas
type Punto2D = (Float, Float)

absoluto :: Float -> Float
absoluto n 
    | n < 0 = -n
    | otherwise = n

productoInterno :: Punto2D -> Punto2D -> Punto2D
productoInterno (x1, y1) (x2, y2) = (x1 * x2, y1 * y2)

esParMenor :: Punto2D -> Punto2D -> (Bool, Bool)
esParMenor (x1, y1) (x2, y2)
    | (x1 > x2) && (y1 > y2) = (False, False)
    | (x1 < x2) && (y1 > y2) = (True, False)
    | (x1 > x2) && (y1 < y2) = (False, True)
    | (x1 < x2) && (y1 < y2) = (True, True)
    | otherwise = (False, False)

distancia :: Punto2D -> Punto2D -> Punto2D
distancia (x1, y1) (x2, y2) = (abs( x1 - x2 ), abs(y1 -y2))

sumaTerna :: (Int, Int, Int) -> Int
sumaTerna (x, y ,z) = x + y + z


-- Mismo Ejercicio
sumaSiMultiplo :: Int -> Int -> Int
sumaSiMultiplo n a
    |mod n a == 0 = n 
    |otherwise = 0
sumarSoloMultiplos :: (Int, Int, Int) -> Int -> Int
sumarSoloMultiplos (x, y, z) a 
    | a == 0 = 0
    |otherwise = sumaSiMultiplo x a + sumaSiMultiplo y a+ sumaSiMultiplo z a
-----------

posPrimerPar :: (Int, Int, Int) -> Int
posPrimerPar (x, y, z)
    |mod x 2 == 0 = 1
    |mod y 2 == 0 = 2
    |mod z 2 == 0 = 3
    |otherwise = 4

crearPar :: a -> b -> (a, b)
crearPar x y = (x, y)

invertir :: (a, b) -> (b, a)
invertir (a, b) = (b, a)

