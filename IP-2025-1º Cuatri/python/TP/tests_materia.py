import unittest
from typing import Any
from buscaminas import (os,
    colocar_minas, es_matriz,                   # Ej. 1
    calcular_numeros,                           # Ej. 2
    crear_juego, estado_valido, estructura_y_tipos_validos, son_matriz_y_misma_dimension, todas_celdas_seguras_descubiertas, # Ej. 3
    obtener_estado_tablero_visible,             # Ej. 4
    marcar_celda,                               # Ej. 5
    descubrir_celda, caminos_descubiertos,      # Ej. 6
    verificar_victoria,                         # Ej. 7
    reiniciar_juego,                            # Ej. 8
    guardar_estado,                             # Ej. 9
    cargar_estado,                              # Ej. 10

    crear_matriz,                                       # Ej. 1 Aux
    minas_adyacentes,                                   # Ej. 2 Aux
    vaciar_matriz,                                      # Ej. 3 Aux
    descubre_minas, buscar_camino, pertenece_lista,     # Ej. 6 Aux
    son_iguales_tableros,                               # Ej. 8 Aux
    guardar_tablero, guardar_tablero_visible,           #Ej 9 Aux
    linea_valida, contar_columnas, armar_linea, cantidad_minas_adyacentes, tablero_valido_minas, # Ej. 10 Aux

    BOMBA, BANDERA, VACIO,
    EstadoJuego
)

#--------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 1 # TERMINADO
#--------------------------------------------------------------------------------------------------------------------------------------
class test_es_matriz(unittest.TestCase):
    def test_no_es_matriz_vacia1(self):
        self.assertFalse(es_matriz([]))
    def test_no_es_matriz_vacia2(self):
        self.assertFalse(es_matriz([[]]))
    def test_es_matriz_cuadrada(self):
        self.assertTrue(es_matriz([[1,2,3],[4,6,3],[9,63,12]]))
    def test_es_matriz_no_cuadrada(self):
        self.assertTrue(es_matriz([[1,2],[4,6],[94,2],[143,98]]))
    def test_no_es_matriz(self):
        self.assertFalse(es_matriz([[1,2],[4,6,100],[2,2]]))
    def test_no_es_matriz_2(self):
        self.assertFalse(es_matriz([[1,2,0],[100]]))
class test_colocar_minas(unittest.TestCase):
    def test_colocar_minas_vacio1(self):
        self.assertEqual(colocar_minas(2,3,0),[[0,0,0],[0,0,0]])
    def test_colocar_minas_vacio2(self):
        self.assertEqual(colocar_minas(4,2,0),[[0,0],[0,0],[0,0],[0,0]])
    def test_colocar_minas_ejemplo(self):
        tablero: list[list[int]] = colocar_minas(3, 5, 2)           # 3 filas, 5 columnas, 2 minas
        self.assertTrue(son_solo_ceros_y_bombas(tablero))           # Testeamos que el tablero tenga solo bombas o ceros
        self.assertEqual(cant_minas_tablero(tablero), 2)            # Testeamos que haya una mina en el tablero
    def test_colocar_minas_todas_minas(self):
        tablero: list[list[int]] = colocar_minas(4, 3, 12)          # 4 filas, 3 columnas, 12 minas
        self.assertTrue(son_solo_ceros_y_bombas(tablero))
        self.assertEqual(cant_minas_tablero(tablero), 12)
    def test_colocar_minas_devuelve_estructura_matriz_valida(self):
        tablero: list[list[int]] = colocar_minas(3, 5, 4)           # 4 filas, 3 columnas, 12 minas
        self.assertTrue(es_matriz(tablero))

#-------------------------------------------------------------------------------
# Funciones Auxiliares # Para testear colocar_minas
# Chequea que el número de minas en el tablero sea igual al número de minas esperado
def cant_minas_tablero(tablero: list[list[int]]) -> int:
    contador_minas: int = 0
    for fila in tablero:
        for celda in fila:
            if celda == -1:
                contador_minas += 1
    return contador_minas

def son_solo_ceros_y_bombas (tablero: list[list[int]]) -> bool:
    for fila in tablero:
        for celda in fila:
            if celda not in [0, -1]:
                return False
    return True
#-------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 2 # TERMINADO
#--------------------------------------------------------------------------------------------------------------------------------------
class test_calcular_numeros(unittest.TestCase):
    def test_calcular_numeros_caso_minimo1(self):
        tablero: list[list[int]] = [[-1,0]]             # Borde mínimo válido (al menos un 0 y un -1)
        calcular_numeros(tablero)
        self.assertEqual(tablero, [[-1,1]])
    def test_calcular_numeros_caso_minimo2(self):
        tablero: list[list[int]] = [[0,-1]]             # Ídem
        calcular_numeros(tablero)
        self.assertEqual(tablero, [[1,-1]])
    def test_calcular_numeros_ejemplo1_2x2(self):
        tablero: list[list[int]] = [[0,-1],
                                    [0, 0]]
        calcular_numeros(tablero)
        self.assertEqual(tablero, [[1,-1],
                                   [1, 1]])             # Testeamos que el tablero tenga los números correctos
    def test_calcular_numeros_ejemplo2_2x2(self):
        tablero: list[list[int]] = [[-1, 0],
                                    [ 0,-1]]
        calcular_numeros(tablero)
        self.assertEqual(tablero, [[-1, 2],
                                   [ 2,-1]])            # Testeamos que el tablero tenga los números correctos
    def test_calcular_numeros_mina_maxima(self):
        tablero: list[list[int]] = [[-1,-1,-1],
                                    [-1, 0,-1],         # Posición rodeada de minas
                                    [-1,-1,-1]]
        calcular_numeros(tablero)
        self.assertEqual(tablero, [[-1,-1,-1],
                                   [-1, 8,-1],
                                   [-1,-1,-1]])
    def test_calcular_numeros_sin_minas(self):
        tablero: list[list[int]] = [[0, 0, 0, 0, 0],    # Celdas vacías sin minas adyacentes
                                    [0, 0, 0, 0,-1],
                                    [0, 0, 0, 0, 0]]
        calcular_numeros(tablero)
        self.assertEqual(tablero, [[0, 0, 0, 1, 1],
                                   [0, 0, 0, 1,-1],
                                   [0, 0, 0, 1, 1]])
    def test_calcular_numeros_todas_minas(self):
        tablero: list[list[int]] = [[-1,-1,-1],
                                    [-1,-1,-1],
                                    [-1,-1,-1]]
        calcular_numeros(tablero)
        self.assertEqual(tablero, [[-1,-1,-1],
                                   [-1,-1,-1],
                                   [-1,-1,-1]])

#--------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 3 # TERMINADO
#--------------------------------------------------------------------------------------------------------------------------------------
class test_crear_juego(unittest.TestCase):
    def test_crear_juego_caso_minimo(self):
        estado: EstadoJuego = crear_juego(1,1,0)
        self.assertTrue(dimension_correcta(estado['tablero'], 1, 1))            # Testeamos dimensión de tablero
        self.assertTrue(dimension_correcta(estado['tablero_visible'], 1, 1))    # y tablero visible
        self.assertEqual(estado['filas'], 1)                                    # Testeamos las claves restantes
        self.assertEqual(estado['columnas'], 1)
        self.assertEqual(estado['minas'], 0)
        self.assertFalse(estado['juego_terminado'])
        self.assertEqual(cant_minas_tablero(estado['tablero']), 0)              # Testeamos que no haya minas en 'tablero'
    def test_crear_juego_ejemplo_arbitrario(self):
        filas: int      = 5
        columnas: int   = 3
        minas: int      = 2
        estado: EstadoJuego = crear_juego(filas, columnas, minas)
        self.assertTrue(dimension_correcta(estado['tablero'], filas, columnas))             # Testeamos dimensión de tablero
        self.assertTrue(dimension_correcta(estado['tablero_visible'], filas, columnas))     # y tablero visible
        for fila in estado['tablero_visible']:                                              # Testeamos que 'tablero_visible' esté vacío
            for celda in fila:
                self.assertEqual(celda, VACIO)
        self.assertEqual(estado['filas'], filas)                                            # Testeamos las claves restantes
        self.assertEqual(estado['columnas'], columnas)
        self.assertEqual(estado['minas'], minas)
        self.assertFalse(estado['juego_terminado'])
        self.assertEqual(cant_minas_tablero(estado['tablero']), minas)                      # Testeamos que haya una mina en 'tablero'
class test_estado_valido(unittest.TestCase):
    def test_estado_valido_ejemplo_correcto(self):
        estado: EstadoJuego = {'filas': 2,'columnas': 2,'minas': 1,
                       'tablero': [[-1,1],[1,1]],'tablero_visible': [[' ',VACIO],[' ',VACIO]],'juego_terminado': False}
        self.assertTrue(estado_valido(estado))
    def test_estado_valido_estructura(self):
        estado: EstadoJuego = {'filas': 2,'columnas': 2,'minas': 2,
                       'tablero': [[-1,2],[2,-1]],'tablero_visible': [[' ',' '],[' ',' ']],'juego_terminado': False,'otra_clave': 134}
        self.assertFalse(estado_valido(estado))
    def test_estado_valido_minas_incorrectas(self):
        estado: EstadoJuego = {'filas': 3,'columnas': 3,'minas': 2,
                       'tablero': [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]],'tablero_visible': [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
                       'juego_terminado': False}
        self.assertFalse(estado_valido(estado))
    def test_estado_valido_tablero_descubierto_no_termina_el_juego(self):
        estado: EstadoJuego = {'filas': 2,'columnas': 2,'minas': 2,
                       'tablero': [[-1,2],[2,-1]],'tablero_visible': [[BANDERA,'2'],['2',BANDERA]],'juego_terminado': False}
        self.assertFalse(estado_valido(estado))
    def test_estado_valido_tablero_no_descubierto_y_juego_terminado(self):
        estado: EstadoJuego = {'filas': 2,'columnas': 2,'minas': 2,
                       'tablero': [[-1,2],[2,-1]],'tablero_visible': [[BANDERA,'2'],[' ',' ']],'juego_terminado': True}
        self.assertFalse(estado_valido(estado))
    def test_estado_valido_col_bomba_juego_no_terminado(self):
        estado: EstadoJuego = {'filas': 2,'columnas': 2,'minas': 2,
                    'tablero': [[-1,2],[2,-1]],'tablero_visible': [[BOMBA,' '],[' ',' ']],'juego_terminado': False}
        self.assertFalse(estado_valido(estado))
    def test_estado_valido_elemento_de_matriz_incorrecto(self):
        estado: EstadoJuego = {'filas': 2,'columnas': 2,'minas': 2,
                       'tablero': [[-1,2],[2,-1]],'tablero_visible': [[BANDERA,BOMBA],[12,23]],'juego_terminado': False}
        self.assertFalse(estado_valido(estado))
    def test_estado_valido_elem_visible_no_coincide_con_valor_real(self):
        estado = {
            'filas': 2,
            'columnas': 2,
            'minas': 1,
            'tablero': [[0, 1], [1, -1]],
            'tablero_visible': [['5', VACIO], [VACIO, VACIO]],  # '5' no coincide con el valor real 0
            'juego_terminado': False
        }
        self.assertFalse(estado_valido(estado))
class test_estructura_y_tipos_validos(unittest.TestCase):
    def test_estructura_y_tipos_validos_fila_menorig_cero(self):
        estado: EstadoJuego = crear_juego(0,1,1)
        self.assertFalse(estructura_y_tipos_validos(estado))
        estado: EstadoJuego = crear_juego(-5,1,1)
        self.assertFalse(estructura_y_tipos_validos(estado))
    def test_estructura_y_tipos_validos_columna_menorig_cero(self):
        estado: EstadoJuego = crear_juego(1,0,1)
        self.assertFalse(estructura_y_tipos_validos(estado))
        estado: EstadoJuego = crear_juego(1,-3,1)
        self.assertFalse(estructura_y_tipos_validos(estado))
    def test_estructura_y_tipos_validos_mas_minas_que_dimension(self):
        estado: EstadoJuego = crear_juego(3,3,10)
        self.assertFalse(estructura_y_tipos_validos(estado))
        estado: EstadoJuego = crear_juego(2,2,14)
        self.assertFalse(estructura_y_tipos_validos(estado))
    def test_estructura_y_tipos_validos_len_estado(self):
        estado: EstadoJuego = crear_juego(3,3,3)
        self.assertEqual(len(estado),6)
    def test_estructura_y_tipos_validos_len_tablero_igual_filas(self):
        estado: EstadoJuego = crear_juego(3,3,3)
        self.assertEqual(len(estado['tablero']), estado['filas'])
        self.assertNotEqual(len(estado['tablero']),7)
    def test_estructura_y_tipos_validos_len_fila_columna(self):
        estado: EstadoJuego = crear_juego(3,3,3)
        self.assertEqual(len(estado['tablero'][0]), estado['columnas'])
        self.assertNotEqual(len(estado['tablero'][0]),5)
    def test_estructura_y_tipos_validos_valores_posibles_tablero(self):
        valores_posibles_tablero: list[int] = list(range(-1,9))
        estado: EstadoJuego = crear_juego(5,3,6)
        for fila in estado['tablero']:
            for elem in fila:
                self.assertIn(elem,valores_posibles_tablero)
    def test_estructura_y_tipos_validos_valores_posibles_tablero_visible(self):
        valores_posibles_tablero_visible: list[list[Any]] = [VACIO,BOMBA,BANDERA] + list(range(0,9))
        estado: EstadoJuego = crear_juego(5,3,6)
        for fila in estado['tablero_visible']:
            for elem in fila:
                self.assertIn(elem,valores_posibles_tablero_visible)
    def test_estructura_y_tipos_validos_estado_distinto_de_6(self):
        tablero: list[list[int]] = [[1,2,3],[4,5,6],[7,8,9]]
        calcular_numeros(tablero)
        estado: EstadoJuego = {'filas': 3,'columnas': 3,'minas': 2,
                       'tablero': tablero,'tablero_visible': vaciar_matriz(tablero),'juego_terminado': False,'otra clave': 2}
        self.assertFalse(estructura_y_tipos_validos(estado))
    def test_estructura_y_tipos_validos_tablero_invalido(self):
        tablero: list[list[int]] = [[-11,14],[-9,25]]
        estado: EstadoJuego = {'filas': 2,'columnas': 2,'minas': 1,
                       'tablero': tablero,'tablero_visible': vaciar_matriz(tablero),'juego_terminado': False}
        self.assertFalse(estructura_y_tipos_validos(estado))
    def test_estructura_y_tipos_validos_tablero_visible_invalido(self):
        tablero: list[list[int]]            = [[1,2],[4,1]]
        tablero_visible: list[list[int]]    = [[12,-21],[15,11]]
        calcular_numeros(tablero)
        estado: EstadoJuego = {'filas': 2,'columnas': 2,'minas': 1,
                       'tablero': tablero,'tablero_visible': tablero_visible,'juego_terminado': False}
        self.assertFalse(estructura_y_tipos_validos(estado))
class test_son_matriz_y_misma_dimension(unittest.TestCase):
    def test_son_matriz_y_misma_dimension_no_es_matriz1(self):
        self.assertFalse(son_matriz_y_misma_dimension([[1,2,3],[2,0,2],[0,3]],
                                                      [[0,5,3],[1,3,0],[9,1]]))
    def test_son_matriz_y_misma_dimension_no_es_matriz2(self):
        self.assertFalse(son_matriz_y_misma_dimension([[1],[2,0],[0]],
                                                      [[0],[1,3],[9]]))
    def test_son_matriz_y_misma_dimension_matriz_no_llena(self):
        self.assertFalse(son_matriz_y_misma_dimension([],[]))
        self.assertFalse(son_matriz_y_misma_dimension([[]],[[]]))
    def test_son_matriz_y_misma_dimension_matriz_minima(self):
        self.assertTrue(son_matriz_y_misma_dimension([[4]],[[1]]))
    def test_son_matriz_y_misma_dimension_matriz_no_cuadrada(self):
        self.assertTrue(son_matriz_y_misma_dimension([[4,2],[3,1],[9,4],[8,5]],
                                                     [[1,6],[7,4],[2,7],[8,9]]))
    def test_son_matriz_y_misma_dimension_caso2x2(self):
        self.assertTrue(son_matriz_y_misma_dimension([[4,2],[3,1]],
                                                     [[1,6],[7,4]]))
    def test_son_matriz_y_misma_dimension_caso3x3(self):
        self.assertTrue(son_matriz_y_misma_dimension([[4,2,3],[1,9,4],[8,5,2]],
                                                     [[1,6,7],[4,2,7],[8,9,0]]))
    def test_son_matriz_y_misma_dimension_distinta_dimension(self):
        self.assertFalse(son_matriz_y_misma_dimension([[1,0],[0,1]],
                                                      [[1,0,3],[0,1,9],[0,9,2]]))
class test_todas_celdas_seguras_descubiertas(unittest.TestCase):
    def test_todas_celdas_seguras_descubiertas_vacio_o_bandera(self):
        tablero: list[list[int]]            = [[-1,-1],[-1,-1]]
        tablero_visible: list[list[int]]    = [[BANDERA,VACIO],[VACIO,BANDERA]]
        self.assertTrue(todas_celdas_seguras_descubiertas(tablero, tablero_visible))
    def test_todas_celdas_seguras_descubiertas_no_mina_o_str1(self):
        tablero: list[list[int]]            = [[0,1],[1,-1]]
        tablero_visible: list[list[int]]    = [['0','1'],['1',VACIO]]
        self.assertTrue(todas_celdas_seguras_descubiertas(tablero, tablero_visible))
    def test_todas_celdas_seguras_descubiertas_no_mina_o_str2(self):
        tablero: list[list[int]]            = [[0,1],[1,-1]]
        tablero_visible: list[list[int]]    = [['0','1'],['1',BANDERA]]
        self.assertTrue(todas_celdas_seguras_descubiertas(tablero, tablero_visible))
    def test_todas_celdas_seguras_descubiertas_no_se_descubrieron_celdas(self):
        tablero: list[list[int]]            = [[0,1,4],[1,-1,6],[0,2,4]]
        tablero_visible: list[list[int]]    = [[VACIO,VACIO,VACIO],[VACIO,VACIO,VACIO],[VACIO,VACIO,VACIO]]
        self.assertFalse(todas_celdas_seguras_descubiertas(tablero, tablero_visible))
    def test_todas_celdas_seguras_descubiertas_no_hay_minas_y_todo_descubierto(self):
        tablero: list[list[int]]            = [[0,0,0],[0,0,0]]
        tablero_visible: list[list[int]]    = [['0','0','0'],['0','0','0']]
        self.assertTrue(todas_celdas_seguras_descubiertas(tablero, tablero_visible))
    def test_todas_celdas_seguras_descubiertas_todas_banderas(self):
        tablero: list[list[int]]            = [[-1,-1],[-1,-1]]
        tablero_visible: list[list[int]]    = [[BANDERA,BANDERA],[BANDERA,BANDERA]]
        self.assertTrue(todas_celdas_seguras_descubiertas(tablero, tablero_visible))
    def test_todas_celdas_seguras_descubiertas_tablero_str(self):
        tablero: list[list[int]]            = [[-1,-1],[-1,-1]]
        tablero_visible: list[list[int]]    = [['-1','-1'],['-1','-1']]
        self.assertFalse(todas_celdas_seguras_descubiertas(tablero, tablero_visible))

#-------------------------------------------------------------------------------
# Función Auxiliar # Para testear crear_juego
def dimension_correcta(tablero: list[list[int]], filas: int, columnas: int) -> bool:
    # Chequea que el tablero tenga las dimensiones correctas
    if len(tablero) != filas:
        return False
    for fila in tablero:
        if len(fila) != columnas:
            return False
    return True
#-------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 4 # TERMINADO
#--------------------------------------------------------------------------------------------------------------------------------------
class test_obtener_estado_tablero_visible(unittest.TestCase):
    def test_obtener_estado_tablero_visible_ejemplo_de_estado(self):
        estado: EstadoJuego = {'filas': 2, 'columnas': 2, 'minas': 1,
                               'tablero': [[-1,1],[1,1]], 'tablero_visible': [[VACIO,'1'],[VACIO,VACIO]],'juego_terminado': False}
        self.assertEqual(obtener_estado_tablero_visible(estado), [[VACIO,'1'],[VACIO,VACIO]])   # Testeamos que el estado sea el esperado
        self.assertEqual(estado['filas'], 2)                                                    # Testeamos que nada se modificó
        self.assertEqual(estado['columnas'], 2)
        self.assertEqual(estado['minas'], 1)
        self.assertEqual(estado['tablero'], [[-1,1],[1,1]])
        self.assertEqual(estado['tablero_visible'], [[VACIO,'1'],[VACIO,VACIO]])
        self.assertFalse(estado['juego_terminado'])

#--------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 5 # TERMINADO
#--------------------------------------------------------------------------------------------------------------------------------------
class test_marcar_celda(unittest.TestCase):
    def test_marcar_celda_posicion_vacia(self):
        estado_vacio: EstadoJuego = {'filas': 2,'columnas': 2,'minas': 1,
                                     'tablero': [[-1,1],[1,1]],'tablero_visible': [[VACIO,VACIO],[VACIO,VACIO]],'juego_terminado': False}
        marcar_celda(estado_vacio,0, 0)
        self.assertEqual(estado_vacio['filas'], 2)                                          # Testeamos que el resto no se modificó
        self.assertEqual(estado_vacio['columnas'], 2)
        self.assertEqual(estado_vacio['minas'], 1)
        self.assertEqual(estado_vacio['tablero'], [[-1,1],[1,1]])
        self.assertEqual(estado_vacio['tablero_visible'], [[BANDERA, VACIO],[VACIO,VACIO]]) # Testeamos que sólo la celda marcada sea visible
        self.assertFalse(estado_vacio['juego_terminado'])
        self.assertEqual(cant_minas_tablero(estado_vacio['tablero']), 1)                    # Testeamos que haya una mina en el tablero
    def test_marcar_celda_posicion_bandera(self):
        estado_bandera: EstadoJuego = {'filas': 2,'columnas': 2,'minas': 1,
                                       'tablero': [[-1,1],[1,1]],'tablero_visible': [[BANDERA,BANDERA],[BANDERA,BANDERA]],'juego_terminado': False}
        marcar_celda(estado_bandera, 1, 0)
        self.assertEqual(estado_bandera['filas'], 2)                                        # Idem
        self.assertEqual(estado_bandera['columnas'], 2)
        self.assertEqual(estado_bandera['minas'], 1)
        self.assertEqual(estado_bandera['tablero'], [[-1,1],[1,1]])
        self.assertEqual(estado_bandera['tablero_visible'], [[BANDERA,BANDERA],[VACIO,BANDERA]])
        self.assertFalse(estado_bandera['juego_terminado'])
        self.assertEqual(cant_minas_tablero(estado_bandera['tablero']), 1)
    def test_marcar_celda_ni_bandera_ni_vacio(self):
        estado_terminado: EstadoJuego = {'filas': 2,'columnas': 2,'minas': 1,
                                         'tablero': [[-1,1],[1,1]],'tablero_visible': [['-1','1'],['1','1']],'juego_terminado': True}
        marcar_celda(estado_terminado, 1, 0)
        self.assertEqual(estado_terminado['filas'], 2)                                      # Idem
        self.assertEqual(estado_terminado['columnas'], 2)
        self.assertEqual(estado_terminado['minas'], 1)
        self.assertEqual(estado_terminado['tablero'], [[-1,1],[1,1]])
        self.assertEqual(estado_terminado['tablero_visible'], [['-1','1'],['1','1']])
        self.assertTrue(estado_terminado['juego_terminado'])
        self.assertEqual(cant_minas_tablero(estado_terminado['tablero']), 1)
    def test_marcar_celda_else(self):
        estado_else: EstadoJuego = {'filas': 2,'columnas': 2,'minas': 1,
                                       'tablero': [[-1,1],[1,1]],'tablero_visible': [['-1',VACIO],[VACIO,VACIO]],'juego_terminado': False}
        marcar_celda(estado_else, 0, 0)
        self.assertEqual(estado_else['filas'], 2)                                           # Idem
        self.assertEqual(estado_else['columnas'], 2)
        self.assertEqual(estado_else['minas'], 1)
        self.assertEqual(estado_else['tablero'], [[-1,1],[1,1]])
        self.assertEqual(estado_else['tablero_visible'], [['-1',VACIO],[VACIO,VACIO]])
        self.assertFalse(estado_else['juego_terminado'])
        self.assertEqual(cant_minas_tablero(estado_else['tablero']), 1)

#--------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 6 # TERMINADO
#--------------------------------------------------------------------------------------------------------------------------------------
class test_descubrir_celda(unittest.TestCase):
    def test_descubrir_celda_juego_terminado (self):                        # si el juego ya está terminado, no se modifica el tablero visible.
        estado: EstadoJuego = {'filas': 2,'columnas': 2,'minas': 1,
                  'tablero': [[0,-1],[1,1]],'tablero_visible': [[VACIO,VACIO],[VACIO,VACIO]],'juego_terminado': True}
        descubrir_celda(estado, 1, 0)
        self.assertEqual(estado['tablero_visible'], [[VACIO,VACIO],[VACIO,VACIO]])
    def test_descubrir_celda_clickear_mina (self):                          # si seleccionamos una mina, el juego se debería terminar y deberían mostrarse todas las minas
        estado: EstadoJuego = {'filas': 3,'columnas': 2,'minas': 2,
                  'tablero': [[1,-1],[0,1],[-1,1]],'tablero_visible': [[VACIO,VACIO],[VACIO,VACIO],[VACIO,VACIO]],'juego_terminado': False}
        descubrir_celda(estado, 0, 1)
        self.assertTrue(estado['juego_terminado'])
        self.assertEqual(estado['tablero_visible'][0][1], BOMBA)
        self.assertEqual(estado['tablero_visible'][2][0], BOMBA)
    def test_descubrir_celda_click_celda_valida (self):                     # si se descubre una celda válida, se muestra esa celda
        estado: EstadoJuego = {'filas': 2,'columnas': 2,'minas': 1,
                  'tablero': [[1,-1],[1, 1]],'tablero_visible': [[VACIO,VACIO],[VACIO,VACIO]],'juego_terminado': False}
        descubrir_celda(estado, 0, 0)
        self.assertEqual(estado['tablero_visible'][0][0], '1')
        self.assertFalse(estado['juego_terminado'])
    def test_descubrir_celda_click_celda_0_con_expansion (self):            # si la celda es '0', verificamos que se expanda correctamente usando 'caminos_descubiertos'
        estado: EstadoJuego = {'filas': 3,'columnas': 3,'minas': 2,
                  'tablero': [[0,0,1],[0,1,-1],[1,1,-1]],'tablero_visible': [[VACIO,VACIO,VACIO],[VACIO,VACIO,VACIO],[VACIO,VACIO,VACIO]],'juego_terminado': False}
        descubrir_celda(estado, 0, 0)
        self.assertEqual(estado['tablero_visible'][0][0], '0')
        self.assertEqual(estado['tablero_visible'][0][1], '0')
        self.assertEqual(estado['tablero_visible'][1][0], '0')
        self.assertEqual(estado['tablero_visible'][1][1], '1')
    def test_descubrir_celda_banderas (self):                               # este test verifica que no se revelen las banderas
        estado: EstadoJuego = {'filas': 3,'columnas': 3,'minas': 1,
                  'tablero': [[0,1,-1],[0,1,1],[0,0,0]],'tablero_visible': [[VACIO,BANDERA,VACIO],[VACIO,VACIO,VACIO],[VACIO,VACIO,VACIO]],'juego_terminado': False}
        descubrir_celda(estado, 2, 0)
        self.assertEqual(estado['tablero_visible'][2][0], '0')
        self.assertEqual(estado['tablero_visible'][2][1], '0')
        self.assertEqual(estado['tablero_visible'][2][2], '0')
        self.assertEqual(estado['tablero_visible'][1][0], '0')
        self.assertEqual(estado['tablero_visible'][1][1], '1')
        self.assertEqual(estado['tablero_visible'][0][1], BANDERA)          # No debe modificarse
    def test_descubrir_celda_juego_ganado (self):                           # si se descubren todas las celdas, se gana el juego
        estado: EstadoJuego = {'filas': 2,'columnas': 2,'minas': 1,
                  'tablero': [[1,-1],[1,1]],'tablero_visible': [['1',VACIO],['1','1']],'juego_terminado': False}
        descubrir_celda(estado, 0, 1)
        self.assertTrue(estado['juego_terminado'])
    def test_descubrir_celda_claves_sin_modificar (self):                   # verificamos que las claves del diccionario no se modifiquen
        estado: EstadoJuego = {'filas': 2,'columnas': 3,'minas': 1,
                  'tablero': [[0,1,-1],[0,1,1]],'tablero_visible': [[VACIO,VACIO,VACIO],[VACIO,VACIO,VACIO]],'juego_terminado': False}
        descubrir_celda(estado, 1, 0)
        self.assertEqual(estado['filas'], 2)
        self.assertEqual(estado['columnas'], 3)
        self.assertEqual(estado['minas'], 1)
        self.assertEqual(estado['tablero'], [[0,1,-1],[0,1,1]])
class test_caminos_descubiertos(unittest.TestCase):
    def test_caminos_descubiertos_celda_con_valor_mayor_a_cero(self):       # si el valor de la celda es > 0, se retorna un camino de un elemento
        tablero: list[list[int]]            = [[1,0],[0,1]]
        visible: list[list[str]]            = [[VACIO,VACIO],[VACIO,VACIO]]
        res: list[list[tuple[int,int]]]     = caminos_descubiertos (tablero, visible, 0, 0)
        self.assertEqual (res, [[(0, 0)]])
    def test_caminos_descubiertos_valor_cero_expande_caminos(self):         # verificamos la expansión de caminos adyacentes desde un 0.
        tablero: list[list[int]]            = [[0,0,1],[0,1,-1],[1,1,-1]]
        visible: list[list[str]]            = [[VACIO,VACIO,VACIO],[VACIO,VACIO,VACIO],[VACIO,VACIO,VACIO]]
        res: list[list[tuple[int,int]]]     = caminos_descubiertos(tablero, visible, 0, 0)
        pertenece: bool = False
        if pertenece_tupla (res, (0, 0)):
            pertenece = True
        self.assertTrue (pertenece)
        for camino in res:
            for i, j in camino:
                self.assertEqual(tablero[i][j] != -1, True)
                self.assertEqual(visible[i][j] != BANDERA , True)
    def test_caminos_descubiertos_camino_sin_banderas(self):                # vemos que no se incluyan las banderas en los caminos
        tablero: list[list[int]]            = [[0,0,0],[0,0,0],[0,0,0]]
        visible: list[list[str]]            = [[VACIO,BANDERA,VACIO],[VACIO,VACIO,VACIO],[VACIO,VACIO,VACIO]]
        res: list[list[tuple[int,int]]]     = caminos_descubiertos(tablero, visible, 0, 0)
        self.assertEqual(pertenece_tupla (res, (0, 1)), False)              # Las banderas no deben estar en ningún camino
    def test_caminos_descubiertos_camino_con_posiciones_validas(self):      # verificamos que los caminos sean válidos
        tablero: list[list[int]]            = [[0]]
        visible: list[list[str]]            = [[VACIO]]
        res: list[list[tuple[int,int]]]     = caminos_descubiertos(tablero, visible, 0, 0)
        for camino in res:
            for i, j in camino:
                self.assertTrue (0 <= i < len (tablero))
                self.assertTrue (0 <= j < len (tablero[0]))
    def test_caminos_descubiertos_celda_fuera(self):
        tablero: list[list[int]]            = [[1,0],[0,1]]
        visible: list[list[str]]            = [[VACIO,VACIO],[VACIO,VACIO]]
        res: list[list[tuple[int,int]]]     = caminos_descubiertos (tablero,visible,5,9)
        self.assertEqual(res, [])
    def test_caminos_descubiertos_bandera_no_revelable(self):
        tablero: list[list[int]]            = [[1,0],[0,1]]
        visible: list[list[str]]            = [[VACIO,VACIO],[VACIO,BANDERA]]
        res: list[list[tuple[int,int]]]     = caminos_descubiertos (tablero,visible,1,1)
        self.assertEqual(res, [])

class test_buscar_camino(unittest.TestCase):
    def test_buscar_camino_visitados(self):
        tablero = [
            [0, 0],
            [0, 0]
        ]
        visible = [
            [VACIO, VACIO],
            [VACIO, VACIO]
        ]
        camino_actual = []
        caminos = []
        visitados = [(0, 1)]  # celda (0,1) ya visidtadaa

        # buscar_camino sobre una celda ya visitada
        buscar_camino(tablero, visible, 0, 1, camino_actual, caminos, visitados)

        # No debe modificar los caminos, porque ya fue visitada
        self.assertEqual(camino_actual, [])
        self.assertEqual(caminos, [])
#-------------------------------------------------------------------------------
# Función Auxiliar # Para testear caminos_descubiertos (verifica si una tupla pertenece al camino)
def pertenece_tupla(l: list[list[tuple[int, int]]], t: tuple[int, int]) -> bool:
    for sublista in l:
        for elemento in sublista:
            if elemento [0] == t [0] and elemento [1] == t [1]:
                return True
    return False
#-------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 7 # TERMINADO
#--------------------------------------------------------------------------------------------------------------------------------------
class test_verificar_victoria(unittest.TestCase):
    def test_verificar_victoria_ejemplo(self):                                              # debería dar True, pues el la única celda con mina está sin descubrir, mientras que las otras están descubiertas
        estado: EstadoJuego = {'filas': 2,'columnas': 2,'minas': 1,
                               'tablero': [[-1,1],[1,1]],'tablero_visible': [[VACIO,'1'],['1','1']],'juego_terminado': False}
        self.assertTrue(verificar_victoria(estado))
        self.assertEqual(estado['filas'], 2)
        self.assertEqual(estado['columnas'], 2)
        self.assertEqual(estado['minas'], 1)
        self.assertEqual(estado['tablero'], [[-1,1],[ 1,1]])
        self.assertEqual(estado['tablero_visible'], [[VACIO,'1'],['1','1']])
        self.assertFalse(estado['juego_terminado'])
    def test_verificar_victoria_faltan_seguras(self):                                       # faltan descubrir posiciones seguras, juego no terminado
        estado: EstadoJuego = {'filas': 2,'columnas': 2,'minas': 1,
                  'tablero': [[-1, 1], [1, 1]],'tablero_visible': [[VACIO,VACIO],['1','1']],'juego_terminado': False}
        self.assertFalse(verificar_victoria (estado))
    def test_verificar_victoria_tablero_sin_minas_con_todas_celdas_descubiertas(self):      # no hay minas y se descubrieron todas las celdas, juego terminado
        estado: EstadoJuego = {'filas': 2,'columnas': 2,'minas': 0,
                  'tablero': [[0, 0], [0, 0]],'tablero_visible': [['0','0'], ['0','0']],'juego_terminado': False}
        self.assertTrue(verificar_victoria (estado))
    def test_verificar_victoria_sin_minas_y_sin_celdas_descubiertas(self):                  # no hay celdas reveladas, juego no terminado
        estado: EstadoJuego = {'filas': 1,'columnas': 1,'minas': 0,
                  'tablero': [[0]],'tablero_visible': [[VACIO]],'juego_terminado': False}
        self.assertFalse(verificar_victoria (estado))
    def test_verificar_victoria_con_celdas_seguras_ocultas(self):                           # hay minas y aún quedan celdas sin descubrir, juego no terminado
        estado: EstadoJuego = {'filas': 2,'columnas': 2,'minas': 1,
                  'tablero': [[-1, 1], [1, 1]],'tablero_visible': [[VACIO,'1'], [' ','1']],'juego_terminado': False}
        self.assertFalse(verificar_victoria (estado))

#--------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 8 # TERMINADO
#--------------------------------------------------------------------------------------------------------------------------------------
class test_reiniciar_juego(unittest.TestCase):
    def test_reiniciar_juego_ejemplo(self):
        estado: EstadoJuego = {'filas': 2,'columnas': 2,'minas': 1,
                               'tablero': [[-1,1],[ 1,1]],'tablero_visible': [[VACIO,'1'],[VACIO,VACIO]],'juego_terminado': False}
        reiniciar_juego(estado)
        self.assertEqual(estado['tablero_visible'],[[VACIO,VACIO],[VACIO,VACIO]])
        self.assertEqual(cant_minas_tablero(estado['tablero']), 1)
        self.assertEqual(estado['filas'], 2)
        self.assertEqual(estado['columnas'], 2)
        self.assertEqual(estado['minas'], 1)
        self.assertFalse(estado['juego_terminado'])
        self.assertNotEqual (estado['tablero'], [[-1,1],[1,1]])
    def test_reiniciar_juego_reinicio_tablero_1(self): # se reinicia un tablero normal
        estado: EstadoJuego = {'filas': 3,'columnas': 3,'minas': 2,
                               'tablero': [[0,1,-1],[1,2,1],[0,1,0]],'tablero_visible': [['0','1',VACIO],['1','2','1'],[VACIO,'1','0']],'juego_terminado': True}
        reiniciar_juego(estado)
        self.assertEqual(cant_minas_tablero(estado ['tablero']), 2)
        for fila in estado ['tablero_visible']:
            for celda in fila:
                self.assertEqual (celda, VACIO)
        self.assertEqual(estado['filas'], 3)
        self.assertEqual(estado['columnas'], 3)
        self.assertEqual(estado['minas'], 2)
        self.assertFalse(estado['juego_terminado'])
    def test_reiniciar_juego_reinicio_tablero_2(self):
        estado: EstadoJuego = {'filas': 4,'columnas': 4,'minas': 3,
                               'tablero': [[0,1,-1,1],[1,2,2,1],[1,-1,2,1],[1,1,1,0]],'tablero_visible': [[VACIO,'1',VACIO,'1'],['1','2','2','1'],['1',VACIO,'2','1'],['1','1','1',VACIO]],'juego_terminado': True}
        reiniciar_juego(estado)
        self.assertEqual(estado['filas'], 4)
        self.assertEqual(estado['columnas'], 4)
        self.assertEqual(estado['minas'], 3)
        for fila in estado['tablero_visible']:
            for celda in fila:
                self.assertEqual(celda,VACIO)
        self.assertEqual(cant_minas_tablero(estado['tablero']), 3)
        self.assertFalse(estado['juego_terminado'])

#--------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 9 # TERMINADO
#--------------------------------------------------------------------------------------------------------------------------------------
# Nota: la consigna pide "analizar obligatoriamente casos de test para la función que pide el enunciado". Debido a que nuestra función NO tiene condicionales, pero si otras funciones auxiliares dentro, esto implica que no podemos testear la función original (no hay ramas, o mejor dicho, las ramas están dentro de las funciones aux.), pero entonces ==> DEBEMOS testear nuestras funciones auxiliares. Por lo tanto, solo testeamos nuestras funciones:
class test_guardar_estado(unittest.TestCase):
    def test_guardar_estado_funcion_guardar_tablero_2x2(self):      # Función Aux 1
        estado: EstadoJuego = {'filas': 2,'columnas': 2,'minas': 1,
                               'tablero': [[1,-1],[1,1]],'tablero_visible': [[VACIO,VACIO],[VACIO,VACIO]],'juego_terminado': False}
        ruta_tab: str               = 'test_ej_9_funcion_aux_1_2x2.txt'
        guardar_tablero(estado, ruta_tab, estado['columnas'])       # Ejecuto guardar_tablero (la función devuelve None)
        archivo_guardar_tablero     = open(ruta_tab, 'r')           # Leo el archivo guardado
        contenido                   = archivo_guardar_tablero.read()
        archivo_guardar_tablero.close()
        esperado: str               = '1,-1\n1,1\n'                 # Verificamos que sea el texto que queremos
        self.assertEqual(contenido, esperado)
    def test_guardar_estado_funcion_guardar_tablero_3x3(self):      # Función Aux 1
        estado: EstadoJuego = {'filas': 3,'columnas': 3,'minas': 2,
                               'tablero': [[-1,1,0],[1,2,1],[0,1,-1]],'tablero_visible': [[VACIO,VACIO,VACIO],[VACIO,VACIO,VACIO],[VACIO,VACIO,VACIO]],'juego_terminado': False}
        ruta_tab: str               = 'test_ej_9_funcion_aux_1_3x3.txt'
        guardar_tablero(estado, ruta_tab, estado['columnas'])       # Ejecuto guardar_tablero (la función devuelve None)
        archivo_guardar_tablero     = open(ruta_tab, 'r')           # Leo el archivo guardado
        contenido                   = archivo_guardar_tablero.read()
        archivo_guardar_tablero.close()
        esperado: str               = '-1,1,0\n1,2,1\n0,1,-1\n'     # Verificamos que sea el texto que queremos
        self.assertEqual(contenido, esperado)
    def test_guardar_estado_funcion_guardar_tablero_visible_2x2(self):              # Función Aux 2
        estado: EstadoJuego = {'filas': 2,'columnas': 2,'minas': 1,
                               'tablero': [[0,-1],[1,1]],'tablero_visible': [[VACIO,BANDERA],[VACIO,'1']],'juego_terminado': False}
        ruta_tab_visible: str               = 'test_ej_9_funcion_aux_2_2x2.txt'
        guardar_tablero_visible(estado, ruta_tab_visible, estado['columnas'])       # Ejecutar la función
        archivo_guardar_tablero_visible     = open(ruta_tab_visible, 'r')           # Leo el archivo guardado
        contenido                           = archivo_guardar_tablero_visible.read()
        archivo_guardar_tablero_visible.close()
        esperado: str                       = '?,*\n?,1\n'                          # Verificamos que sea el texto que queremos
        self.assertEqual(contenido, esperado)
    def test_guardar_estado_funcion_guardar_tablero_visible_3x3(self):              # Función Aux 2
        estado: EstadoJuego = {'filas': 3,'columnas': 3,'minas': 2,
                               'tablero': [[2,-1,2],[2,-1,2],[1,1,1]],'tablero_visible': [[VACIO,BANDERA,'2'],['2',VACIO,'2'],[VACIO,'1',VACIO]],'juego_terminado': False}
        ruta_tab_visible: str               = 'test_ej_9_funcion_aux_2_3x3.txt'
        guardar_tablero_visible(estado, ruta_tab_visible, estado['columnas'])       # Ejecutar la función
        archivo_guardar_tablero_visible     = open(ruta_tab_visible, 'r')           # Leo el archivo guardado
        contenido                           = archivo_guardar_tablero_visible.read()
        archivo_guardar_tablero_visible.close()
        esperado: str                       = '?,*,2\n2,?,2\n?,1,?\n'               # Verificamos que sea el texto que queremos
        self.assertEqual(contenido, esperado)

#--------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 10 # TERMINADO
#--------------------------------------------------------------------------------------------------------------------------------------
class test_cargar_estado(unittest.TestCase):
    def test_cargar_estado_archivo_no_existe(self):
        estado_1: EstadoJuego = {}                  # si el archivo no existe -> res=False
        self.assertFalse(cargar_estado(estado_1, 'nonexistent_dir'))
    def test_cargar_estado_archivos_vacios(self):   # Archivos vacíos
        estado_2: EstadoJuego = {}
        archivo = open('temp_test/tablero.txt', 'w')
        archivo.write('')
        archivo.close()
        archivo = open('temp_test/tablero_visible.txt', 'w')
        archivo.write('')
        archivo.close()
        self.assertFalse(cargar_estado(estado_2, 'temp_test')) # No cumplen las condiciones -> res=False
    def test_cargar_estado_diferentes_filas(self):
        estado_3: EstadoJuego = {}
        archivo = open('temp_test/tablero.txt', 'w')
        archivo.write('0,0\n0,0\n0,0')                                  # 3 filas
        archivo.close()
        archivo = open('temp_test/tablero_visible.txt', 'w')
        archivo.write('?,?\n?,?')                                       # 2 filas
        archivo.close()
        self.assertFalse(cargar_estado(estado_3, 'temp_test'))
    def test_cargar_estado_diferentes_columnas(self):
        estado_4: EstadoJuego = {}
        archivo = open('temp_test/tablero.txt', 'w')
        archivo.write('0,0,0\n0,0,0\n')                                 # Idem, con columnas
        archivo.close()
        archivo = open('temp_test/tablero_visible.txt', 'w')
        archivo.write('?,?\n?,?\n')
        archivo.close()
        self.assertFalse(cargar_estado(estado_4, 'temp_test'))
    def test_cargar_estado_valores_no_validos(self):
        estado_5: EstadoJuego = {}
        archivo = open('temp_test/tablero.txt', 'w')
        archivo.write('0,134\n-1,0\n') # 134 >> 8
        archivo.close()
        archivo = open('temp_test/tablero_visible.txt', 'w')
        archivo.write('?,?\n?,?\n')
        archivo.close()
        self.assertFalse(cargar_estado(estado_5, 'temp_test'))
    def test_cargar_estado_simbolos_no_validos(self):
        estado_6: EstadoJuego = {}
        archivo = open('temp_test/tablero.txt', 'w')
        archivo.write('0,1\n1,-1\n')
        archivo.close()
        archivo = open('temp_test/tablero_visible.txt', 'w')
        archivo.write('?,asdf\n*,?\n') # asdf inválido
        archivo.close()
        self.assertFalse(cargar_estado(estado_6, 'temp_test'))
    def test_cargar_estado_bomba_en_posicion_incorrecta(self):
        estado_7: EstadoJuego = {}
        archivo = open('temp_test/tablero.txt', 'w')
        archivo.write('0,1\n1,0\n')
        archivo.close()
        archivo = open('temp_test/tablero_visible.txt', 'w')
        archivo.write('?,?\n?,BOMBA\n') # FALSO, no hay ninguna bomba
        archivo.close()
        self.assertFalse(cargar_estado(estado_7, 'temp_test'))
    def test_cargar_estado_numero_incorrecto(self):
        estado_8: EstadoJuego = {}
        archivo = open('temp_test/tablero.txt', 'w')
        archivo.write('0,1\n1,-1\n')
        archivo.close()
        archivo = open('temp_test/tablero_visible.txt', 'w')
        archivo.write('?,2\n*,?\n') # FALSO, era 1
        archivo.close()
        self.assertFalse(cargar_estado(estado_8, 'temp_test'))
    def test_cargar_estado_no_hay_minas(self):
        estado_9: EstadoJuego = {}
        archivo = open('temp_test/tablero.txt', 'w')
        archivo.write('0,0\n0,0\n')
        archivo.close()
        archivo = open('temp_test/tablero_visible.txt', 'w')
        archivo.write('?,?\n?,?\n')
        archivo.close()
        self.assertFalse(cargar_estado(estado_9, 'temp_test'))
    def test_cargar_estado_tablero_no_tiene_sentido(self):
        estado_10: EstadoJuego = {}
        archivo = open('temp_test/tablero.txt', 'w')
        archivo.write('0,1\n-1,0\n') # los valores deberían ser '1,1\n -1,1' (posiciones adyacentes)
        archivo.close()
        archivo = open('temp_test/tablero_visible.txt', 'w')
        archivo.write('?,?\n?,?\n')
        archivo.close()
        self.assertFalse(cargar_estado(estado_10, 'temp_test'))
    def test_cargar_estado_valores_coherentes_juego_incompleto(self):
        estado_11: EstadoJuego = {}
        archivo = open('temp_test/tablero.txt', 'w')
        archivo.write('1,-1,1\n1,1,1\n0,0,0\n')
        archivo.close()
        archivo = open('temp_test/tablero_visible.txt', 'w')
        archivo.write('1,?,1\n?,?,?\n?,?,?\n')
        archivo.close()
        self.assertTrue(cargar_estado(estado_11, 'temp_test'))
        self.assertEqual(estado_11['filas'], 3)
        self.assertEqual(estado_11['columnas'], 3)
        self.assertEqual(estado_11['minas'], 1)
        self.assertEqual(estado_11['tablero'][1][1], 1)
        self.assertEqual(estado_11['tablero_visible'][0][0], '1')
        self.assertFalse(estado_11['juego_terminado'])
    def test_cargar_estado_simbolos_validos(self):
        estado_12: EstadoJuego = {}
        archivo = open('temp_test/tablero.txt', 'w')
        archivo.write('-1,1,0\n1,1,0\n0,0,0\n')
        archivo.close()
        archivo = open('temp_test/tablero_visible.txt', 'w')
        archivo.write('BOMBA,1,?\n*,?,?\n?,?,?\n')
        archivo.close()
        self.assertFalse(cargar_estado(estado_12, 'temp_test'))
    def test_cargar_estado_lineas_vacias(self):
        estado_13: EstadoJuego = {}
        archivo = open('temp_test/tablero.txt', 'w')
        archivo.write('\n0,0\n\n0,0\n\n')
        archivo.close()
        archivo = open('temp_test/tablero_visible.txt', 'w')
        archivo.write('\n?,?\n\n?,?\n\n')
        archivo.close()
        resultado = cargar_estado(estado_13, 'temp_test')
        self.assertFalse(resultado)
        self.assertNotIn('filas', estado_13)
    def test_cargar_estado_bandera_sin_mina(self):
        estado = {}
        archivo = open('temp_test/tablero.txt', 'w')
        archivo.write('0,0\n0,0\n')  # No hay minas
        archivo.close()
        archivo = open('temp_test/tablero_visible.txt', 'w')
        archivo.write('*,?\n?,?\n')  # Bandera en (0,0) pero no hay mina real
        archivo.close()
        self.assertFalse(cargar_estado(estado, 'temp_test'))
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main(verbosity=1)