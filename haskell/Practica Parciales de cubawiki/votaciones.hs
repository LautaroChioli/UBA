
type Presidente = String
type Vice = String
type Formula = (Presidente, Vice)
type Formulas = [Formula]
type Votos = [Int]




-- Ejercicio 1
{--
problema porcentajeDeVotosAfirmativos (formulas: seq⟨String x String⟩,votos:seq< Z >, cantTotalVotos: Z) : R {
 requiere: {¬formulasInvalidas(formulas)}
 requiere: {|formulas| = |votos|}
 requiere: {Todos los elementos de votos son mayores o iguales a 0}
 requiere: {La suma de todos los elementos de votos es menor o igual a cantTotalVotos}
 asegura: {res es el porcentaje de votos no blancos (es decir, asociados a alguna de las fórmulas) sobre el total de votos emitidos}
}


[("Juan","Pedro"),("Matias","Javier"),("Gonzalo","Victor")]   [100,50,25] 200
--}

porcentajeDeVotosAfirmativos :: Formulas -> Votos -> Int -> Float
porcentajeDeVotosAfirmativos _ votos votosTotales = ((fromIntegral (sumatoria votos)) / (fromIntegral(votosTotales))) * 100

sumatoria :: Votos -> Int
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs


-- Ejercicio 2
{--
problema formulasInvalidas (formulas: seq⟨String x String⟩) : Bool {
 requiere: {True}
 asegura: {(res = true) <=> formulas contiene un candidato se propone para presidente y vicepresidente en la misma fórmula; 
 o algún candidato se postula para presidente o vice en más de una fórmula }
--}


formulasInvalidas :: Formulas -> Bool
formulasInvalidas [] = False
formulasInvalidas formulas 
    | buscoMismoPresiVice formulas || buscoRepetido (listaDeTuplasALista formulas) = True
    | otherwise = False


mismoPresiVice :: Formula -> Bool
mismoPresiVice (a, b)
    | a == b = True
    | otherwise = False

buscoMismoPresiVice :: Formulas -> Bool
buscoMismoPresiVice [] = False
buscoMismoPresiVice (formula:resto)
    | mismoPresiVice formula = True
    | otherwise = buscoMismoPresiVice resto

listaDeTuplasALista :: Formulas -> [String]
listaDeTuplasALista [] = []
listaDeTuplasALista (formula:resto) = tuplaALista (formula) ++ listaDeTuplasALista resto

tuplaALista :: Formula -> [String]
tuplaALista (a, b) = [a, b]

buscoRepetido :: [String] -> Bool
buscoRepetido [] = False
buscoRepetido (x:xs)
    | buscoRepetidoAux x xs  = True
    | otherwise = buscoRepetido xs

buscoRepetidoAux :: String -> [String] -> Bool
buscoRepetidoAux _ [] = False
buscoRepetidoAux persona (x:xs)
    | persona == x = True
    | otherwise = buscoRepetidoAux persona xs

-- Ejercicio 3
{--
problema porcentajeDeVotos (vice: String, formulas: seq⟨String x String⟩,votos:seq< Z >) : R {
 requiere: {La segunda componente de algún elemento de formulas es vice}
 requiere: {¬formulasInvalidas(formulas)}
 requiere: {|formulas| = |votos|}
 requiere: {Todos los elementos de votos son mayores o iguales a 0}
 requiere: {Hay al menos un elemento de votos mayores estricto a 0}
 asegura: {res es el porcentaje de votos que obtuvo vice sobre el total de votos afirmativos}
}
Para resolver este ejercicio pueden utilizar la función division presentada en el Ejercicio 1.
[("Juan","Pedro"),("Matias","Javier"),("Gonzalo","Victor")]   [100,50,25]
--}

porcentajeDeVotos :: Vice -> Formulas -> Votos -> Float
porcentajeDeVotos _ [] _ = 0
porcentajeDeVotos _ _ [] = 0
porcentajeDeVotos  vice formulas votos = (fromIntegral (buscoVotosDeVice vice (votosPorFormula formulas votos)) / fromIntegral (sumatoria votos)) * 100


votosPorFormula :: Formulas -> Votos -> [((Presidente, Vice), Int)]
votosPorFormula [] [] = []
votosPorFormula (tupla:resto) (votosParaTuplaActual:restoVotos) = (tupla, votosParaTuplaActual) : votosPorFormula resto restoVotos

buscoVotosDeVice :: Vice -> [((Presidente, Vice), Int)] -> Int
buscoVotosDeVice _ [] = 0
buscoVotosDeVice vice (tupla:resto)
    | vice == buscoVice tupla = votosVice tupla
    | otherwise = buscoVotosDeVice vice resto

buscoVice :: ((Presidente, Vice), Int) -> Vice
buscoVice ((a, b), n) = b

votosVice :: ((Presidente, Vice), Int) -> Int
votosVice ((a, b), n) = n

