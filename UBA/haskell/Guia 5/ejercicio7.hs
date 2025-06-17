type Identificacion = Integer
type Ubicacion = String
type Estado = (Disponibilidad, Ubicacion)
type Locker = (Identificacion, Estado)
type MapaDeLockers = [Locker]
type Disponibilidad = Bool

--lockers = [(100,(False,"ZD39I")),(101,(True,"JAH3I")),(103,(True,"IQSA9")),(105,(True,"QOTSA")),(109,(False,"893JJ")),(110,(False,"99292"))]

-- Ejercicio I

existeElLocker :: Identificacion -> MapaDeLockers -> Bool
existeElLocker _ [] = False
existeElLocker iden (locker:lockers)
    | idenDeLocker locker == iden = True
    | otherwise = existeElLocker iden lockers

idenDeLocker :: Locker -> Identificacion
idenDeLocker (iden, _) = iden

-- Ejercicio II

ubicacionDelLocker :: Identificacion -> MapaDeLockers -> Ubicacion
ubicacionDelLocker iden (locker:lockers)
    | existeElLocker iden (locker:lockers) && idenDeLocker locker == iden = ubiLocker (estadoDelLocker locker)
    | otherwise = ubicacionDelLocker iden lockers

estadoDelLocker :: Locker -> Estado
estadoDelLocker (_, estado ) = estado

ubiLocker :: Estado -> Ubicacion
ubiLocker (_, ubicacion) = ubicacion

-- Ejercicio III

estaDisponibleElLocker :: Identificacion -> MapaDeLockers -> Bool
estaDisponibleElLocker iden (locker:lockers)
    |existeElLocker iden (locker:lockers) && idenDeLocker locker == iden = disponibilidadLocker (estadoDelLocker locker)
    | otherwise = estaDisponibleElLocker iden lockers

disponibilidadLocker :: Estado -> Disponibilidad
disponibilidadLocker (disp, _) = disp

-- Ejercicio IV

ocuparLocker :: Identificacion -> MapaDeLockers -> MapaDeLockers
ocuparLocker _ [] = []
ocuparLocker iden (locker:lockers)
    | idenDeLocker locker == iden = cambiarOcupacionLocker locker : ocuparLocker iden lockers
    | otherwise = locker : ocuparLocker iden lockers


sacarLocker :: Identificacion -> MapaDeLockers -> MapaDeLockers
sacarLocker iden (locker:lockers)
    | existeElLocker iden (locker:lockers) && idenDeLocker locker == iden = lockers
    | otherwise = locker : sacarLocker iden lockers

cambiarOcupacionLocker :: Locker -> Locker
cambiarOcupacionLocker (iden , (ocupacion, ubicacion)) = (iden, (False, ubicacion))