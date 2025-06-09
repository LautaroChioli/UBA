    archivo_tablero     = open(os.path.join(ruta_directorio, "tablero.txt"), "r")
    tablero: list[str]  = []
    for linea in archivo_tablero: # iteramos en cada linea del archivo y listamos las lineas que sean válidas
        if linea_valida(linea):
            residuo: str    = ""
            i: int          = 0
            while i < len(linea):
                if linea[i] != '\n':
                    residuo += linea[i]
                i += 1
            tablero.append(residuo)
    archivo_tablero.close()