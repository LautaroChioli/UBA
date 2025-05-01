type Producto = String
type Mercaderia = [Producto]
type Cantidad = Int
type ItemStock = (Producto, Cantidad)
type Stock = [ItemStock]
type Precio = Float
type PrecioProducto = (Producto, Precio)
type ListaPrecios = [PrecioProducto]
type DineroTotal = Float

-- Practica sistema de stock, marcadas entre comentarios las funciones buscadas por el enunciaado
--
generarStock :: Mercaderia -> Stock
generarStock [] = []
generarStock (producto:productos) = (producto, cantidadDeVeces producto (producto:productos)) : generarStock (sacar producto productos)
--
cantidadDeVeces :: Producto -> Mercaderia -> Cantidad
cantidadDeVeces _ [] = 0
cantidadDeVeces elegido (producto:productos)
    |   elegido == producto = 1 + cantidadDeVeces elegido productos
    |   otherwise = cantidadDeVeces elegido productos

sacar :: Producto -> Mercaderia -> Mercaderia
sacar _ [] = []
sacar elegido (producto:productos)
    |   elegido == producto = sacar elegido productos
    |   otherwise = producto : sacar elegido productos
--
stockDeProducto :: Producto -> Stock -> Cantidad
stockDeProducto _ [] = 0
stockDeProducto elegido (producto:productos) 
    | elegido == nombreDeItemStock producto = cantidadEnStock producto
    | otherwise = stockDeProducto elegido productos
--
nombreDeItemStock :: ItemStock -> Producto
nombreDeItemStock (producto, _) = producto

cantidadEnStock :: ItemStock -> Cantidad
cantidadEnStock (_, cantidad) = cantidad
--
dineroEnStock :: Stock -> ListaPrecios -> DineroTotal
dineroEnStock [] _ = 0
dineroEnStock _ [] = 0
dineroEnStock (itemStock:restoStock) listaDePrecios = buscoPrecio itemStock listaDePrecios + dineroEnStock restoStock listaDePrecios
--
precioTotalDeUnProducto :: ItemStock -> PrecioProducto -> DineroTotal
precioTotalDeUnProducto (productoCant, cantidad) (productoPrecio, precio) = fromIntegral cantidad * precio

nombreDePrecioProducto :: PrecioProducto -> Producto
nombreDePrecioProducto (nombre, _) = nombre

buscoPrecio :: ItemStock -> ListaPrecios -> DineroTotal
buscoPrecio _ [] = 0
buscoPrecio itemStock (precioProducto:restoPrecios)
    | nombreDeItemStock itemStock == nombreDePrecioProducto precioProducto = precioTotalDeUnProducto itemStock precioProducto
    | otherwise = buscoPrecio itemStock restoPrecios
--
aplicarOferta :: Stock -> ListaPrecios -> ListaPrecios
aplicarOferta [] _ = []
aplicarOferta (itemStock:restoStock) listaDePrecios
    | cantidadEnStock itemStock > 10 = aplicoOferta(devuelvoPrecioDeProducto itemStock listaDePrecios) : aplicarOferta restoStock listaDePrecios
    | otherwise = devuelvoPrecioDeProducto itemStock listaDePrecios : aplicarOferta restoStock listaDePrecios
--
aplicoOferta :: PrecioProducto -> PrecioProducto
aplicoOferta (prod , precio) = (prod , precio * 0.8)

devuelvoPrecioDeProducto :: ItemStock -> ListaPrecios -> PrecioProducto
devuelvoPrecioDeProducto itemStock (precioProducto:preciosRestantes)
    | nombreDeItemStock itemStock == nombreDePrecioProducto precioProducto = precioProducto
    | otherwise = devuelvoPrecioDeProducto itemStock preciosRestantes