primeraFuncion :: Int -> Int
primeraFuncion n
    | n == 1  = 8
    | n == 4  = 131
    | n == 16 = 16

segundaFuncion :: Int -> Int
segundaFuncion n
    | n == 8  = 1
    | n == 131 = 4
    | n == 16 = 16

fog :: Int -> Int
fog n = primeraFuncion(segundaFuncion n)

gof :: Int -> Int
gof n = segundaFuncion(primeraFuncion n)
