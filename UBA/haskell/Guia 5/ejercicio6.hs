type Texto = String
type Nombre = Texto
type Telefono = Texto
type Contacto = (Nombre, Telefono)
type ContactosTel = [Contacto]

-- ContactosTel [("Juan", "100"), ("Pedro", "200"),("Toro Sentado", "300"),("Robert McNamara", "400"), ("John Haskell", "500")]

-- I

enLosContactos :: Nombre -> ContactosTel -> Bool
enLosContactos _ [] = False
enLosContactos nombre (x:xs)
   | nombre == nombreDeContacto x = True
   | otherwise = enLosContactos nombre xs

nombreDeContacto :: Contacto -> Nombre
nombreDeContacto (nombre, numero) = nombre

-- II, tambien hice el 3 sin querer haciendo el 2 jijo, sacoContactoViejo

agregarContacto :: Contacto -> ContactosTel -> ContactosTel
agregarContacto nuevo lista
    | enLosContactos (nombreDeContacto nuevo) lista == False = nuevo : lista
    | otherwise = buscarRepetidoYActualizo nuevo lista : sacoContactoViejo nuevo lista


buscarRepetidoYActualizo :: Contacto -> ContactosTel -> Contacto
buscarRepetidoYActualizo nuevo lista
    | enLosContactos (nombreDeContacto nuevo) lista = actualizarNumero nuevo (buscoRepetido nuevo lista)

buscoRepetido :: Contacto -> ContactosTel -> Contacto
buscoRepetido cont (x:xs)
    | nombreDeContacto cont == nombreDeContacto x = x

actualizarNumero :: Contacto -> Contacto -> Contacto
actualizarNumero (_, numeroNuevo) ( nombreViejo , _) = (nombreViejo, numeroNuevo)  

sacoContactoViejo :: Contacto -> ContactosTel -> ContactosTel
sacoContactoViejo _ [] = []
sacoContactoViejo nuevo (x:xs)
    | nombreDeContacto nuevo == nombreDeContacto x = sacoContactoViejo nuevo xs
    | otherwise = x : sacoContactoViejo nuevo xs