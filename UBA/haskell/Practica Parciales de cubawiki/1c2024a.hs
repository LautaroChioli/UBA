{--
La Unidad de Tecnologías de la Información (UTI) de nuestra Facultad nos ha encargado que desarrollemos un nuevo sistema para el registro de alumnos.
En este sistema se guarda la información de cada alumno, que está representada como una tupla de dos elementos:
el primero es el nombre completo del alumno y el segundo una lista con las notas de los finales que rindió.

Para implementar este sistema nos enviaron las siguientes especificaciones y nos pidieron que hagamos el desarrollo enteramente en Haskell, utilizando los tipos requeridos 
y solamente las funciones que se ven en la materia Introducción a la Programación / Algoritmos y Estructuras de Datos I (FCEyN-UBA).

Ejercicio 1 (2 puntos) 
problema aproboMasDeNMaterias (registro: seq⟨seq⟨Char⟩ x seq⟨Z⟩⟩, alumno:seq⟨Char⟩, n: Z) : Bool {
  requiere: {No hay nombres de alumnos repetidos en registro}
  requiere: {Las notas de registro son todas iguales o mayores a cero y menores o iguales a 10}
  requiere: {n > 0}
  requiere: {El alumno se encuentra en el registro }
  asegura: {res = true <=> el alumno tiene más de n notas de finales mayores o iguales a 4 en el registro}
}
[("Juan", [6,7,5,7]),("Pedro", [1,2,1,3]),("John",[5,2,4,1]),("Gurkhul",[9,10,9,8]),("DjMario",[9,9,0,10])]
--}

aproboMasDeNMaterias :: [(String, [Int])] -> String -> Int -> Bool
aproboMasDeNMaterias registro alumno n
    | n < materiasAprobadas (buscoNotasAlumno registro alumno) = True
    | otherwise = False

buscoNotasAlumno :: [(String, [Int])] -> String -> [Int]
buscoNotasAlumno [] _ = []
buscoNotasAlumno (primerAlumno:resto) buscado
    | buscado == fst primerAlumno = notaDeAlumno primerAlumno
    | otherwise = buscoNotasAlumno resto buscado

materiasAprobadas :: [Int] -> Int
materiasAprobadas [] = 0
materiasAprobadas (x:xs)
    | x >= 4 = 1 + materiasAprobadas xs
    | otherwise = materiasAprobadas xs

notaDeAlumno :: (String, [Int]) ->  [Int]
notaDeAlumno (_, notas) = notas

{--

Ejercicio 2 (2 puntos)
problema buenosAlumnos (registro: seq⟨seq⟨Char⟩ x seq⟨Z⟩⟩) : seq⟨seq⟨Char⟩⟩ {
  requiere: {No hay nombres de alumnos repetidos en registro}
  requiere: {Las notas de registro son todas iguales o mayores a cero y menores o iguales a 10}
  asegura: {res es la lista de los nombres de los alumnos que están en registro cuyo promedio de notas es mayor o igual a 8 y no tiene aplazos (notas menores que 4)}
}
Para resolver el promedio pueden utilizar la función del Preludio de Haskell fromIntegral que dado un valor de tipo Int devuelve su equivalente de tipo Float.
[("Juan", [6,7,5,7]),("Pedro", [1,2,1,3]),("John",[5,2,4,1]),("Gurkhul",[9,10,9,8]),("DjMario",[9,9,8,10]),("Washington Montevideo", [10,10,10,10])]
--}

buenosAlumnos :: [(String, [Int])] -> [String]
buenosAlumnos [] = []
buenosAlumnos (tupla:resto)
    | buenAlumno tupla = nombreDeAlumno tupla : buenosAlumnos resto
    | otherwise = buenosAlumnos resto

buenAlumno :: (String, [Int]) -> Bool
buenAlumno (nombre, notas)
    | promedioNotas notas >= 8 && tieneAplazos notas == False = True
    | otherwise = False

nombreDeAlumno :: (String, [Int]) -> String
nombreDeAlumno (nombre, _) = nombre

promedioNotas :: [Int] -> Float
promedioNotas notas = (fromIntegral (sumatoria notas)) / (fromIntegral (modulo notas))

sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

modulo :: [Int] -> Int
modulo [] = 0
modulo (x:xs) = 1 + modulo xs

tieneAplazos :: [Int] -> Bool
tieneAplazos [] = False
tieneAplazos (x:xs)
    | x < 4 = True
    | otherwise = tieneAplazos xs

{--
Ejercicio 3 (2 puntos)
problema mejorPromedio (registro: seq⟨seq⟨Char⟩ x seq⟨Z⟩⟩) : seq⟨Char⟩ {
  requiere: {No hay nombres de alumnos repetidos en registro}
  requiere: {Las notas de registro son todas iguales o mayores a cero y menores o iguales a 10}
  requiere: {|registro| > 0 }
  asegura: {res es el nombre del alumno cuyo promedio de notas es el más alto; si hay más de un alumno con el mismo promedio de notas, devuelve el nombre de alumno que aparece primero en registro}
}

--}

mejorPromedio :: [(String, [Int])] -> [Char]
mejorPromedio [] = []
mejorPromedio (tupla:resto) = mejorPromedioAux (tupla:resto) (nombreDeAlumno tupla) (promedioNotas (notaDeAlumno tupla))

mejorPromedioAux :: [(String, [Int])] -> String -> Float -> String
mejorPromedioAux [] mejor _ = mejor
mejorPromedioAux (tupla:resto) mejor notaMax
    | promedioNotas (notaDeAlumno tupla) >= notaMax = mejorPromedioAux resto (nombreDeAlumno tupla) (promedioNotas(notaDeAlumno tupla))
    | otherwise = mejorPromedioAux resto mejor notaMax

notasDeAlumno :: (String, [Int]) -> [Int]
notasDeAlumno (_, n) = n


{--
Ejercicio 4 (3 puntos)
problema seGraduoConHonores (registro: seq⟨seq⟨Char⟩ x seq⟨Z⟩⟩, cantidadDeMateriasDeLaCarrera: Z, alumno: seq⟨Char⟩ ) : Bool {
  requiere: {No hay nombres de alumnos repetidos en registro}
  requiere: {Las notas de registro son todas iguales o mayores a cero y menores o iguales a 10}
  requiere: {cantidadDeMateriasDeLaCarrera > 0}
  requiere: {El alumno se encuentra en el registro }
  requiere: {|buenosAlumnos(registro)| > 0}
  asegura: {res <=> true si aproboMasDeNMaterias(registro, alumno, cantidadDeMateriasDeLaCarrera -1) = true y alumno pertenece al conjunto de buenosAlumnos(registro) y el promedio de notas de finales de alumno está a menos (estrictamente) de 1 punto del mejorPromedio(registro)}
}


--}

seGraduoConHonores :: [(String, [Int])] -> Int -> String -> Bool
seGraduoConHonores [] _ _ = False
seGraduoConHonores (tupla:resto) materias alumno
    | aproboMasDeNMaterias (tupla:resto) alumno (materias -1) && estaEnBuenosAlumnos alumno (buenosAlumnos (tupla:resto)) && promedioNotas (notasDeAlumno tupla) > (promedioNotas (buscoNotasAlumno (tupla:resto) (mejorPromedio (tupla:resto))) -1) = True
    | otherwise = seGraduoConHonores resto materias alumno


-- buenosAlumnos :: [(String, [Int])] -> [String]
-- buenosAlumnos [] = []
-- buenosAlumnos (tupla:resto)
--     | buenAlumno tupla = nombreDeAlumno tupla : buenosAlumnos resto
--     | otherwise = buenosAlumnos resto


-- buscoNotasAlumno :: [(String, [Int])] -> String -> [Int]
-- buscoNotasAlumno [] _ = []
-- buscoNotasAlumno (primerAlumno:resto) buscado
--     | buscado == fst primerAlumno = notaDeAlumno primerAlumno
--     | otherwise = buscoNotasAlumno resto buscado

estaEnBuenosAlumnos :: String -> [String] -> Bool
estaEnBuenosAlumnos _ [] = False
estaEnBuenosAlumnos alumno (x:xs)
    | alumno == x = True
    | otherwise = estaEnBuenosAlumnos alumno xs