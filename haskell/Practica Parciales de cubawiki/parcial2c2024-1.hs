type  Relacion = (String, String)
type  Relaciones = [Relacion]
type Persona = String
type Personas = [Persona]

{--
problema relacionesValidas (relaciones: seq⟨String x String⟩) : Bool {
  requiere: {True}
  asegura: {(res = true) <=> relaciones no contiene ni tuplas repetidas1, ni tuplas con ambas componentes iguales}
}
1 A los fines de este problema consideraremos que dos tuplas son iguales si el par de elementos que las componen (sin importar el orden) son iguales. 

relaciones = [("Juan","Pedro"),("Marcos", "Marquito"),("Pedro","Juan"),("John", "Mark")]
--}



relacionesValidas :: Relaciones -> Bool
relacionesValidas relaciones 
    | checkDosTuplasPermutadas relaciones || checkeoUnoIgual relaciones = False
    | otherwise = True


checkDosTuplasPermutadas :: Relaciones -> Bool
checkDosTuplasPermutadas [] = False
checkDosTuplasPermutadas (elegida:resto)
    | checkPermutacion elegida resto = True
    | otherwise = checkDosTuplasPermutadas resto


checkPermutacion :: Relacion -> Relaciones -> Bool
checkPermutacion _ [] = False
checkPermutacion relacion (elegido:siguiente)
    | checkPermutacionAUX relacion elegido = True
    | otherwise = checkPermutacion relacion siguiente

checkPermutacionAUX :: Relacion -> Relacion -> Bool
checkPermutacionAUX (rel1, rel2) (seg1, seg2)
    | (rel1 == seg1 && rel2 == seg2) || (rel2 == seg1 && rel1 == seg2) = True
    | otherwise = False


checkeoUnoIgual :: Relaciones -> Bool
checkeoUnoIgual [] = False
checkeoUnoIgual (elegido:resto)
    | checkeoAmbosIguales elegido = True
    | otherwise = checkeoUnoIgual resto

checkeoAmbosIguales :: Relacion -> Bool
checkeoAmbosIguales (a1, b2)
    | a1 == b2 = True
    | otherwise = False

{--
problema personas (relaciones: seq⟨String x String⟩) : seq⟨String⟩ {
  requiere: {relacionesValidas(relaciones)}
  asegura: {res no tiene elementos repetidos}
  asegura: {res tiene exactamente los elementos que figuran en alguna tupla de relaciones, en cualquiera de sus posiciones}
}
--}

personas :: Relaciones -> Personas
personas relaciones = sacarRepetidos (agregarAListaDePersonas relaciones)



agregarAListaDePersonas :: Relaciones -> Personas
agregarAListaDePersonas [] = []
agregarAListaDePersonas (relacionElegida:resto) = (agregarAListaDePersonasAUX relacionElegida) ++ agregarAListaDePersonas resto

agregarAListaDePersonasAUX :: Relacion -> Personas
agregarAListaDePersonasAUX (per1, per2) = per1 : per2 : []

sacarRepetidos :: Personas -> Personas
sacarRepetidos [] = []
sacarRepetidos (elegido:resto)
    | cantidadRepetido elegido resto > 0 =  elegido : sacarRepetidos (sacarPersona elegido resto)
    | otherwise = elegido : sacarRepetidos resto

cantidadRepetido :: Persona -> Personas -> Int
cantidadRepetido _ [] = 0
cantidadRepetido persona (elegido:resto)
    | persona == elegido = 1 + cantidadRepetido persona resto
    | otherwise = cantidadRepetido persona resto

sacarPersona :: Persona -> Personas -> Personas
sacarPersona _ [] = []
sacarPersona persona (primero:resto)
    | persona == primero = sacarPersona persona resto
    | otherwise = primero : sacarPersona persona resto

{--
problema amigosDe (persona: String, relaciones: seq⟨String x String⟩) : seq⟨String⟩ {
  requiere: {relacionesValidas(relaciones)}
  asegura: {res tiene exactamente los elementos que figuran en las tuplas de relaciones en las que una de sus componentes es persona}
} 
--}

amigosDe :: Persona -> Relaciones -> Personas
amigosDe _ [] = []
amigosDe persona (elegido:resto)
    | estaEn persona elegido = amigo persona elegido : amigosDe persona resto
    | otherwise = amigosDe persona resto

estaEn :: Persona -> Relacion -> Bool
estaEn persona (per1, per2)
    | persona == per1 || persona == per2 = True
    | otherwise = False

amigo :: Persona -> Relacion -> Persona
amigo persona (per1, per2)
    | persona == per1 = per2
    | persona == per2 = per1


{--
problema personaConMasAmigos (relaciones: seq⟨String x String⟩) : String {
  requiere: {relaciones no vacía}
  requiere: {relacionesValidas(relaciones)}
  asegura: {res es el Strings que aparece más veces en las tuplas de relaciones (o alguno de ellos si hay empate)}
}  relaciones = [("Juan","Pedro"),("Marcos", "Marquito"),("Pedro","Javier"),("John", "Pedro")]
--}

personaConMasAmigos :: Relaciones -> Persona
personaConMasAmigos relaciones = quienMasAmigos (personas relaciones) relaciones


cantidadDeAmigos :: Persona -> Relaciones -> Int
cantidadDeAmigos _ [] = 0
cantidadDeAmigos persona relaciones = modulo (amigosDe persona relaciones)

modulo :: [String] -> Int
modulo [] = 0
modulo (elegido:resto) = 1 + modulo resto

quienMasAmigos :: Personas -> Relaciones -> Persona
quienMasAmigos [t] _ = t
quienMasAmigos (primera:resto) relaciones
    | cantidadDeAmigos primera relaciones > cantidadDeAmigos (quienMasAmigos resto relaciones) relaciones= primera
    | otherwise = quienMasAmigos resto relaciones