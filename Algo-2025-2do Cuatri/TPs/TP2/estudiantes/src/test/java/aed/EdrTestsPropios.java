package aed;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;

class EdrTestsPropios {
    Edr edr;
    int d_aula;
    int cant_alumnos;
    int[] solucion;

    @Test
    void sin_sospechosos_examen_largo_y_aula_grande() {
        d_aula = 7;
        cant_alumnos = 25;
        int[] solucion = new int[]{0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4}; // examen de 25 ejercicios
        edr = new Edr(d_aula, cant_alumnos, solucion);

        // Algunos alumnos resuelven ciertos ejercicios correctamente
        edr.resolver(0, 0, 0);
        edr.resolver(0, 1, 1);
        edr.resolver(0, 2, 2);

        edr.resolver(1, 0, 0);
        edr.resolver(1, 3, 3);
        edr.resolver(1, 4, 4);

        edr.resolver(2, 1, 1);
        edr.resolver(2, 5, 5);
        edr.resolver(2, 6, 6);

        edr.resolver(3, 2, 2);
        edr.resolver(3, 7, 7);
        edr.resolver(3, 8, 8);

        edr.resolver(4, 3, 3);
        edr.resolver(4, 9, 9);

        
        // Alumno 5 intenta copiarse dos veces
        edr.copiarse(5); 
        edr.copiarse(5); 

        // Estos alumnos no tienen vecinos válidos (ya sea porque no hay como el caso de 20 o porque no tienen vecinos con ejercicios realizados como el caso del 12), así que no deberían poder copiarse
        edr.copiarse(12); 
        edr.copiarse(12); 
        edr.copiarse(12); 
        edr.copiarse(20); 

        // Chequeo de notas: los primeros alumnos suman puntos según lo que resolvieron. Todos los que no resolvieron ejercicios tienen 0.0
        double[] notas_obtenidas = edr.notas();
        double[] notas_esperadas = new double[] {12.0, 12.0, 12.0, 12.0, 8.0, 8.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
        assertTrue(Arrays.equals(notas_esperadas, notas_obtenidas));

        // Todos entregan el examen
        for (int i = 0; i < cant_alumnos; i++) {
            edr.entregar(i);
        }

        // A pesar de haberse presenciado copias, la cantidad de respuestas no llega nunca al 25% del resto del alummnado, puesto que la mayoría no resolvió
        int[] copiones = edr.chequearCopias();
        assertTrue(Arrays.equals(new int[]{}, copiones));

        NotaFinal[] notasFinales = edr.corregir();
        NotaFinal[] notas_finales_esperadas = {
            new NotaFinal(12.0, 3),
            new NotaFinal(12.0, 2),
            new NotaFinal(12.0, 1),
            new NotaFinal(12.0, 0),
            new NotaFinal(8.0, 5),
            new NotaFinal(8.0, 4),
            new NotaFinal(0.0, 24),
            new NotaFinal(0.0, 23),
            new NotaFinal(0.0, 22),
            new NotaFinal(0.0, 21),
            new NotaFinal(0.0, 20),
            new NotaFinal(0.0, 19),
            new NotaFinal(0.0, 18),
            new NotaFinal(0.0, 17),
            new NotaFinal(0.0, 16),
            new NotaFinal(0.0, 15),
            new NotaFinal(0.0, 14),
            new NotaFinal(0.0, 13),
            new NotaFinal(0.0, 12),
            new NotaFinal(0.0, 11),
            new NotaFinal(0.0, 10),
            new NotaFinal(0.0, 9),
            new NotaFinal(0.0, 8),
            new NotaFinal(0.0, 7),
            new NotaFinal(0.0, 6)
        };
        assertTrue(Arrays.equals(notas_finales_esperadas, notasFinales));
    }

    @Test
    void todos_resuelven_bien_sin_llamar_a_copiarse() {

        d_aula = 8;
        cant_alumnos = 5;
        int[] solucion = new int[]{0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4};
        edr = new Edr(d_aula, cant_alumnos, solucion);

        // Cada alumno resuelve correctamente todos los ejercicios
        for(int alumno = 0; alumno < cant_alumnos; alumno++){
            for(int ejercicio = 0; ejercicio < solucion.length; ejercicio++){
                edr.resolver(alumno, ejercicio, solucion[ejercicio]);
            }
        }

        // Todos deberían tener nota 100
        double[] notas_obtenidas = edr.notas();
        double[] notas_esperadas = new double[cant_alumnos];
        Arrays.fill(notas_esperadas, 100.0);
        assertTrue(Arrays.equals(notas_esperadas, notas_obtenidas));

        // Todos entregan
        for(int i = 0; i < cant_alumnos; i++)
            edr.entregar(i);

        // Como todos entregaron el mismo examen perfecto -> son todos sospechosos
        int[] copiones = edr.chequearCopias();
        assertTrue(Arrays.equals(new int[]{0,1,2,3,4}, copiones));

        // Si todos son sospechosos -> corregir devuelve un array vacío
        NotaFinal[] nota_final = edr.corregir();
        NotaFinal[] esperado = new NotaFinal[]{};
        assertTrue(Arrays.equals(esperado, nota_final));
    }

    @Test
    void aula_minima() {

        // Caso borde: aula de 1 x 1
        d_aula = 1;
        cant_alumnos = 1;
        solucion = new int[]{0,1,2,3,4,5,6,7,8,9};

        edr = new Edr(d_aula, cant_alumnos, solucion);

        // El único alumno resuelve todo perfectamente
        for(int ejercicio = 0; ejercicio < solucion.length; ejercicio++){
            edr.resolver(0, ejercicio, solucion[ejercicio]);
        }

        // Nota total: 100
        double[] notas_obtenidas = edr.notas();
        double[] notas_esperadas = new double[]{100.0};
        assertTrue(Arrays.equals(notas_esperadas, notas_obtenidas));
        
        edr.entregar(0);
       

        // El alumno no es sospechoso por caso borde a pesar de cumplir el requisito del 25%
        assertTrue(Arrays.equals(new int[]{}, edr.chequearCopias()));

        // El alumno no es sopechoso y tiene su nota
        NotaFinal[] nota_final = edr.corregir();
        NotaFinal[] esperado = new NotaFinal[]{new NotaFinal(100.0, 0)};
        assertTrue(Arrays.equals(esperado, nota_final));
    }
    @Test
    void copia_adelante_borde_izquierdo(){
        d_aula = 2;                                                             //   0  -
        cant_alumnos = 2;                                                       //   1  -     aula creada
        solucion = new int[]{0,1,2,3,4,5,6,7,8,9};                              

        edr = new Edr(d_aula, cant_alumnos, solucion);

        // alumno de adelante resuelve el primer ejercicio correctamente
        edr.resolver(0, 0, 0);
        // alumno de atras se copia el ejercicio correcto
        edr.copiarse(1);

        double[] notas = edr.notas();
        double[] notas_esperadas = new double[]{10.0, 10.0};
        //ambos tienen el primer ejecicio correcto
        assertTrue(Arrays.equals(notas, notas_esperadas));

        // ambos entregan
        edr.entregar(0);
        edr.entregar(1);

        // los dos son sospechosos
        int[] copiones = edr.chequearCopias();
        int[] copiones_esperados = new int[]{0, 1};
        assertTrue(Arrays.equals(copiones_esperados, copiones));

        // corregir devuelve vacío
        NotaFinal[] obtenido = edr.corregir();
        NotaFinal[] esperado = new NotaFinal[]{};
        assertTrue(Arrays.equals(esperado, obtenido));
    }

    @Test
    void copia_adelante_borde_derecho(){    
        d_aula = 3;                                                     //  0  -  1
        cant_alumnos = 4;                                               //  2  -  3
        solucion = new int[]{0,1,2,3,4,5,6,7,8,9};                      //  -  -  -

        edr = new Edr(d_aula, cant_alumnos, solucion);
        //alumno de adelante resuleve el segundo ejercicio correctamente
        edr.resolver(1, 1, 1);
        //alumno de atras copia el ejercicio
        edr.copiarse(3);
        //ambos tienen el ejercicio correcto
        double[] notas = edr.notas();
        double[] notas_esperadas = new double[]{0.0, 10.0, 0.0, 10.0};
        assertTrue(Arrays.equals(notas, notas_esperadas));

        // todos entregan
        edr.entregar(0);
        edr.entregar(1);
        edr.entregar(2);
        edr.entregar(3);

        // los que resolvieron ejercicios (el 1 por buena fe, el 3 por copiarse) aparecen como sospechosos
        int[] copiones = edr.chequearCopias();
        int[] copiones_esperados = new int[]{1, 3};
        assertTrue(Arrays.equals(copiones_esperados, copiones));

        // corregir devuelve vacío
        NotaFinal[] obtenido = edr.corregir();
        NotaFinal[] esperado = new NotaFinal[]{
            new NotaFinal(0.0, 2),
            new NotaFinal(0.0, 0)
        };
        assertTrue(Arrays.equals(esperado, obtenido));
        
    }

    @Test
    void todos_con_dark_web_con_examen_incorrecto() {

        d_aula = 4;
        cant_alumnos = 4;
        solucion = new int[]{0,1,2,3,4,5,6,7,8,9}; // examen de 10 ejercicios
        edr = new Edr(d_aula, cant_alumnos, solucion);

        // Examen de la "dark web" completo con todos los ejercicios incorrectos
        int[] darkweb = new int[]{9,9,9,9,9,9,9,9,9,8};
        edr.consultarDarkWeb(cant_alumnos, darkweb);

        // Entregan todos
        for (int i = 0; i < cant_alumnos; i++) {
            edr.entregar(i);
        }

        // Notas: todos tienen el examen completo pero con todas las respuestas erróneas
        assertTrue(Arrays.equals(new double[]{0.0, 0.0, 0.0, 0.0}, edr.notas()));

        // Todos tienen el mismo examen -> todos sospechosos
        assertTrue(Arrays.equals(new int[]{0,1,2,3}, edr.chequearCopias()));

        // Todos sospechosos -> corregir devuelve vacío
        NotaFinal[] obtenido = edr.corregir();
        NotaFinal[] esperado = new NotaFinal[]{};
        assertTrue(Arrays.equals(esperado, obtenido));
    }

    @Test
    void copiarse_mas_veces_de_lo_necesario(){    
        d_aula = 2;
        cant_alumnos = 2; 
        solucion = new int[]{0};

        edr = new Edr(d_aula, cant_alumnos, solucion);
        // alumno 0 resuelve el ejercicio bien
        edr.resolver(0, 0, 0);
        // alumno 1 se copia una vez mas de lo necesario (no deberia pasar nada)
        edr.copiarse(1);
        edr.copiarse(1);

        // ambos sacan 100
        double[] notas = edr.notas();
        double[] notas_esperadas = new double[]{100.0, 100.0};
        assertTrue(Arrays.equals(notas, notas_esperadas));

        // los dos son sospechosos
        int[] copiones = edr.chequearCopias();
        int[] copiones_esperados = new int[]{0, 1};
        assertTrue(Arrays.equals(copiones_esperados, copiones));

        // esperamos que corregir devuelva un array vacío
        NotaFinal[] obtenido = edr.corregir();
        NotaFinal[] esperado = new NotaFinal[]{};
        assertTrue(Arrays.equals(esperado, obtenido));
    }

    @Test
    void se_copia_sin_vecinos(){    
        d_aula = 2;                                                     //  0  
        cant_alumnos = 2;                                               //  1  
        solucion = new int[]{0,1,2};                      //  -  

        edr = new Edr(d_aula, cant_alumnos, solucion);
        //alumno 1 resuelve todo bien
        edr.resolver(1, 0, 0);
        edr.resolver(1, 1, 1);
        edr.resolver(1, 2, 2);
        //alumno 0 se intenta copiar pero no tiene ningun vecino
        edr.copiarse(0);

        //alumno 0 no suma nota, pues no pudo copiarse
        double[] notas = edr.notas();
        double[] notas_esperadas = new double[]{0.0, 100.0};
        assertTrue(Arrays.equals(notas, notas_esperadas));

        // ambos entregan
        edr.entregar(0);
        edr.entregar(1);

        //ninguno es sospechoso
        int[] copiones = edr.chequearCopias();
        int[] copiones_esperados = new int[]{};
        assertTrue(Arrays.equals(copiones_esperados, copiones));

        // todos reciben sus notas
        NotaFinal[] obtenido = edr.corregir();
        NotaFinal[] esperado = new NotaFinal[]{
            new NotaFinal(100.0, 1),
            new NotaFinal(0.0, 0)
        };
        assertTrue(Arrays.equals(esperado, obtenido));
    }

    @Test
    void alumno_se_copia_de_alguien_que_accedio_a_la_dark_web() {
        d_aula = 5;
        cant_alumnos = 15;
        solucion = new int[]{0,1,2,3,4,5,6,7,8,9};

        edr = new Edr(d_aula, cant_alumnos, solucion);

        // el estudiante 0 resuelve bien un ejercicio
        edr.resolver(0, 0, 0);

        // todos los estudiantes salvo el 0 toman el examen de la darkweb (el cual sólo tiene una respuesta bien)
        int[] examenDark = new int[]{1,0,0,0,0,0,0,7,0,0};
        edr.consultarDarkWeb(cant_alumnos - 1, examenDark);

        // el estudiante 0 intenta copiarse (se copia un ejercicio mal resuelto)
        edr.copiarse(0);

        // verificamos las notas
        double[] notas_obtenidas = edr.notas();
        double[] notas_esperadas = new double[]{10.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0};
        assertTrue(Arrays.equals(notas_obtenidas, notas_esperadas));

        // Todos entregan
        for(int i = 0; i < cant_alumnos; i++){
            edr.entregar(i);
        }

        // Todos los estudiantes que accedieron a la darkweb cumplen los requisitos de haberse copiado (aun teniendo casi todos los ejercicios mal)
        // A pesar de haberse copiado, el estudiante 0 no comple los requisitos de sospechoso, puesto que en el ejercicio 0 puso una respuesta diferente al resto
        int[] copiones = edr.chequearCopias();
        int[] copiones_esperados = new int[]{1,2,3,4,5,6,7,8,9,10,11,12,13,14};
        assertTrue(Arrays.equals(copiones_esperados, copiones));

        // el estudiante 0 es el único que aparecerá en corregir
        NotaFinal[] nota_final = edr.corregir();
        NotaFinal[] esperado = new NotaFinal[]{new NotaFinal(10.0, 0)};
        assertTrue(Arrays.equals(esperado, nota_final));
    }
}