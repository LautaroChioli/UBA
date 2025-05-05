module SolucionT2 where


{--
 Ejercicio 1 (2 puntos)

problema hayQueCodificar (c: Char, mapeo: seq⟨Char x Char⟩ ) : Bool {
  requiere: {No hay elementos repetidos entre las primeras componentes de mapeo}
  requiere: {No hay elementos repetidos entre las segundas componentes de mapeo}
  asegura: {res = true <=> c es igual a la primera componente de alguna tupla de mapeo}
}

[('a','b'),('l','k'),('w','y')]
--}

hayQueCodificar :: Char -> [(Char,Char)] -> Bool
hayQueCodificar _ [] = False
hayQueCodificar letra (tupla:resto)
    | encuentraLetraACambiar letra tupla = True
    | otherwise = hayQueCodificar letra resto

-- encuentraLetraACambiarLista :: Char -> [(Char,Char)] -> Bool
-- encuentraLetraACambiarLista _ [] = False
-- encuentraLetraACambiarLista letra (tupla:resto)
--     | encuentraLetraACambiar letra tupla = True
--     |

encuentraLetraACambiar :: Char -> (Char,Char) -> Bool
encuentraLetraACambiar letra (a, b)
    | letra == a = True
    | otherwise = False



{--
 Ejercicio 2 (2 puntos)

problema cuantasVecesHayQueCodificar (c: Char, frase: seq⟨Char⟩, mapeo: seq⟨Char x Char⟩ ) : Z {
  requiere: {No hay elementos repetidos entre las primeras componentes de mapeo}
  requiere: {No hay elementos repetidos entre las segundas componentes de mapeo}
  requiere: {|frase| > 0 }
  requiere: {c pertenece a frase}
  asegura: {(res = 0 y hayQueCodificar (c, mapeo) = false) o (res = cantidad de veces que c aparece en frase y hayQueCodificar (c, mapeo) = true)}
}
--}


cuantasVecesHayQueCodificar :: Char -> [Char] -> [(Char, Char)] -> Int
cuantasVecesHayQueCodificar _ _ [] = 0
cuantasVecesHayQueCodificar letra palabra codificaciones
    | hayQueCodificar letra codificaciones = cuentoLetra letra palabra
    | otherwise = 0



cuentoLetra :: Char -> [Char] -> Int
cuentoLetra _ [] = 0
cuentoLetra letra (elegida:resto)
    | letra == elegida = 1 + cuentoLetra letra resto
    | otherwise = cuentoLetra letra resto


{--
problema laQueMasHayQueCodificar (frase: seq⟨Char⟩, mapeo: seq⟨Char x Char⟩ ) : Char {
  requiere: {No hay elementos repetidos entre las primeras componentes de mapeo}
  requiere: {No hay elementos repetidos entre las segundas componentes de mapeo}
  requiere: {|frase| > 0 }
  requiere: {Existe al menos un c que pertenece a frase y hayQueCodificar(c, mapeo)=true}
  asegura: {res = c donde c es el caracter tal que cuantasVecesHayQueCodificar(c, frase, mapeo) es mayor a cualquier otro caracter perteneciente a frase}
  asegura: {Si existen más de un caracter c que cumple la condición anterior, devuelve el que aparece primero en frase }

-- --}

laQueMasHayQueCodificar :: [Char] -> [(Char,Char)] -> Char
laQueMasHayQueCodificar palabra codificaciones = letraMasRepetida (filtroLetras codificaciones palabra)



letraMasRepetida :: [Char] -> Char
letraMasRepetida (primera:resto)
    | cuantasVecesLetra primera (primera:resto) >= cuantasVecesLetra (primero (sacoLetra primera (primera:resto))) resto = primera
    | otherwise = letraMasRepetida resto


cuantasVecesLetra :: Char -> [Char] -> Int
cuantasVecesLetra _ [] = 0
cuantasVecesLetra  letra (primera:resto)
    | letra == primera = 1 + cuantasVecesLetra letra resto
    | otherwise = cuantasVecesLetra  letra resto

primero :: [Char] -> Char
primero [] = ' '
primero (primero:_) = primero

sacoLetra :: Char -> [Char] -> [Char]
sacoLetra _ [] = []
sacoLetra letra (primera:resto)
    | letra == primera = sacoLetra letra resto
    | otherwise = primera : sacoLetra letra resto

filtroLetras :: [(Char, Char)] -> [Char] -> [Char]
filtroLetras [] _ = []
filtroLetras _ [] = []
filtroLetras (tupla:resto) palabra = filtroLetrasAUX tupla palabra ++ filtroLetras resto palabra

filtroLetrasAUX :: (Char, Char) -> [Char] -> [Char]
filtroLetrasAUX _ [] = []
filtroLetrasAUX (a,b) (primeraLetra:resto)
    | primeraLetra == a = primeraLetra : filtroLetrasAUX (a, b) resto
    | otherwise = filtroLetrasAUX (a, b) resto 



buscoEnListaDeTuplas :: Char -> [(Char, Char)] -> Bool
buscoEnListaDeTuplas  _ [] = False
buscoEnListaDeTuplas  letra (tupla:resto)
    | buscoEnTupla letra tupla = True
    | otherwise = buscoEnListaDeTuplas letra resto


{--

problema codificarFrase (frase: seq⟨Char⟩, mapeo: seq⟨Char x Char⟩ ) : seq ⟨Char⟩ {
  requiere: {No hay elementos repetidos entre las primeras componentes de mapeo}
  requiere: {No hay elementos repetidos entre las segundas componentes de mapeo}
  requiere: {|frase| > 0 }
  asegura: {|res| = | frase|}
  asegura: { Para todo 0 <= i < |frase| si hayQueCodificar(frase[i], mapeo) = true entonces res[i]= (mapeo[j])1, para un j tal que 0 <= j < |mapeo| y mapeo[j])0=frase[i]}
  asegura: { Para todo 0 <= i < |frase| si hayQueCodificar(frase[i], mapeo) = false entonces res[i]= frase[i]}
} 
--}


codificarFrase :: [Char] -> [(Char, Char)] -> [Char]
codificarFrase [] _ = []
codificarFrase _ [] = []
codificarFrase (letra:restoLetras) codificaciones
    | hayQueCodificar letra codificaciones = cambioLetra letra codificaciones : codificarFrase restoLetras codificaciones
    | otherwise = letra : codificarFrase restoLetras codificaciones

cambioTupla :: Char -> (Char, Char) -> Char
cambioTupla letra (a, b)
    | letra == a = b 
    | otherwise = letra

cambioLetra :: Char -> [(Char, Char)] -> Char
cambioLetra letra (tupla:resto)
    | buscoEnTupla letra tupla = nuevaLetra tupla
    | otherwise = cambioLetra letra resto

buscoEnTupla :: Char -> (Char, Char) -> Bool
buscoEnTupla letra (a, b)
    | letra == a = True
    | otherwise = False

nuevaLetra :: (Char, Char) -> Char
nuevaLetra (a, b) = b