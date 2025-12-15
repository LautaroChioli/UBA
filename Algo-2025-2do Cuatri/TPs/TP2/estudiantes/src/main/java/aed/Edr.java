package aed;
import java.util.ArrayList;

public class Edr {

    private ArrayList<Estudiante> estudiantes; // array de estudiantes
    private ArrayList<Integer> canonico; // plantilla del examen
    private Heap<Estudiante> puntajeMin; // heap de puntajes
    private int ladoAula; // representa el lado del aula
    private int cantEstudiantes; // representa la cantidad de estudiantes que hay en el aula
    private int cantSospechosos; // representa la cantidad de estudiantes sospechosos que hay 
    private ArrayList<Handle<Estudiante>> handles; // array de Handles que referencian la posición de cada estudiante en el heap

    public Edr(int LadoAula, int Cant_estudiantes, int[] ExamenCanonico) {
        this.ladoAula = LadoAula;
        this.cantEstudiantes = Cant_estudiantes;
        this.cantSospechosos = 0;

        // Creamos el var canonico
        this.canonico = new ArrayList<>();
        for (int i = 0; i < ExamenCanonico.length; i++) { // O(R)
            this.canonico.add(ExamenCanonico[i]);
        }

        // Creamos el var estudiantes
        this.estudiantes = new ArrayList<>(); // O(E)
        for (int i = 0; i < cantEstudiantes; i++) { // O(E * R)
            Estudiante e = new Estudiante(i, ExamenCanonico.length, ladoAula);
            estudiantes.add(e);
        }

        // Array de Handles
        this.handles = new ArrayList<>(cantEstudiantes); // O(E)
        for (int i = 0; i < cantEstudiantes; i++) { // O(E)
            handles.add(null); // O(1)
        }

        // Creamos el heap genérico con insertarRapido
        this.puntajeMin = new Heap<>(cantEstudiantes);// O(E)
        for (Estudiante e : estudiantes) { // O(E)
            Handle<Estudiante> h = puntajeMin.insertarRapido(e); // O(1)
            handles.set(e.id, h); // O(1)
        }
    } // Complejidad Total: O(R) + O(E) + O(E * R) + O(E) + O(E) + O(E) + O(E) = O(E * R)


//-------------------------------------------------NOTAS--------------------------------------------------------------------------


    public double[] notas(){
        // Construimos el array resultado de tamaño igual a la cantidad de estudiantes
        double[] res = new double[cantEstudiantes]; // O(E)
        // Recorremos la lista de estudiantes por id y copiamos la nota
        for (int i = 0; i < cantEstudiantes; i++) { // O(E)
            res[i] = estudiantes.get(i).nota; // O(1)
        }
        return res;
    } // Complejidad total: O(E) + O(E) = O(E)


//------------------------------------------------COPIARSE------------------------------------------------------------------------


    public void copiarse(int estudiante) {
        Estudiante est = estudiantes.get(estudiante); // O(1)
        int MayorRespuestasDiferentes = -1; // O(1)
        int idMVecinoMasDiferente = -1; // O(1)
        ArrayList<Integer> candidatos = vecinos(est); // O(1) -> la cantidad de vecinos siempre está acotada

        // Contamos cuantas respuestas distintas a las del estudiante tiene cada vecino
        for (int vecinoID : candidatos){ // máximo acotado de vecinos -> O(1) pero a cada vecino le recorremos su examen -> O(R)
            Estudiante vecino = estudiantes.get(vecinoID);
            int cont = 0;
            for (int i = 0; i < est.respuestas.size(); i++){ // O(R)
                if (vecino.respuestas.get(i) != -1 && est.respuestas.get(i) == -1){
                    cont++;
                }
            }
            // Si el vecino actual tiene mas respuestas distintas, pasa a ser el que mas diferencias tiene y si empatan, se elige el de mayor ID
            if (cont > MayorRespuestasDiferentes || (cont == MayorRespuestasDiferentes && vecino.id > idMVecinoMasDiferente && cont != 0)){ // O(1)
                MayorRespuestasDiferentes = cont;
                idMVecinoMasDiferente = vecino.id;
            }
        }
        
        // Si no encontramos a nadie con respuestas distintas no hacemos nada
        if (idMVecinoMasDiferente == -1 || MayorRespuestasDiferentes == 0){ // O(1)
            return;
        }

        Estudiante vecino = estudiantes.get(idMVecinoMasDiferente);

        // Copiamos la primer respuesta distinta del vecino elegido
        for (int i = 0; i < est.respuestas.size(); i++){ // O(R)
            if (vecino.respuestas.get(i) != -1 && est.respuestas.get(i) == -1) {
                est.respuestas.set(i, vecino.respuestas.get(i));
                // Si la respuesta es correcta sumamos nota
                est.resueltos++;
                if (vecino.respuestas.get(i) == canonico.get(i)) {
                    est.nota += 100.0 / canonico.size();
                }
                // Actualizamos el heap usando el handle
                handles.get(est.id).actualizarValor(est); // O(log E) -> Edr llama al método definido en la interface del Handle (no sabe cómo se implementa el método dentro de la clase HandleHeap)
                break;
            }
        }
    }

    // Verificamos los vecinos disponibles del estudiante y los insertamos en el array
    private ArrayList<Integer> vecinos(Estudiante est) { // Todo este método es O(1) puesto que la cantidad de vecinos posibles son acotadas y los cálculos de sus posiciones también se consiguen en O(1)
        ArrayList<Integer> vecs = new ArrayList<>();
        int cantAlumnosPorFila = ladoAula / 2;
        if (ladoAula % 2 != 0) {
            cantAlumnosPorFila += 1;
        }

        int indiceAsiento = est.id;

        // Misma fila: asiento - 1
        if (indiceAsiento != 0 && estudiantes.get(indiceAsiento - 1).fila == est.fila) {
            int idVec = indiceAsiento - 1;
            if (idVec < cantEstudiantes) {
                vecs.add(idVec);
            }
        }
        // Misma fila: asiento + 1
        if (indiceAsiento + 1 < cantEstudiantes && estudiantes.get(indiceAsiento + 1).fila == est.fila) {
            int idVec = indiceAsiento + 1;
            if (idVec < cantEstudiantes) {
                vecs.add(idVec);
            }
        }

        // Fila adelante
        int filaAdelante = est.fila - 1;
        if(filaAdelante >= 0){
            // Fila adelante: mismo asiento
            int idVecMismoAsiento = indiceAsiento - cantAlumnosPorFila;
            vecs.add(idVecMismoAsiento);
        }
        return vecs;
    } // Complejidad Total: O(R) + O(R + log E) = O(R + log E)


//-----------------------------------------------RESOLVER----------------------------------------------------------------


    public void resolver(int estudiante, int NroEjercicio, int res) {
        // Modificamos la respuesta del estudiante
        Estudiante e = estudiantes.get(estudiante); // O(1)
        e.respuestas.set(NroEjercicio, res); // O(1)
        e.resueltos++;
        // Si la respuesta es correcta sumamos nota
        if (res == canonico.get(NroEjercicio)) { // O(1)
            e.nota += 100.0 / canonico.size(); // O(1)
        }
        // Actualizamos el heap usando el handle correspondiente
        handles.get(estudiante).actualizarValor(e); // O(log E) -> Edr llama al método definido en la interface del Handle (no sabe cómo se implementa el método dentro de la clase HandleHeap)
    } // Complejidad Total: O(log E)


//------------------------------------------------CONSULTAR DARK WEB-------------------------------------------------------


    public void consultarDarkWeb(int n, int[] examenDW) {
        // Creamos un nuevo array, donde meteremos a los n peores (sacándolos del heap)
        ArrayList<Estudiante> nPeores = new ArrayList<>(n); // O(n)
        for (int i = 0; i < n; i++) { // O(n * log E)
            Estudiante minimo = puntajeMin.consultarMinimo(); // O(1)
            if (minimo == null || minimo.entrego) {
                break;
            }
            minimo = puntajeMin.sacarMinimo(); // O(log E)
            nPeores.add(minimo);
        }

        // Actualizamos los datos de esos n peores
        for (Estudiante e : nPeores) { // O(n)
            e.resueltos = examenDW.length;
            e.nota = 0;

            for (int k = 0; k < examenDW.length; k++) { // O(R)
                e.respuestas.set(k, examenDW[k]);
                if (examenDW[k] == canonico.get(k)) {
                    e.nota += 100.0 / canonico.size();
                }
            }
            // Agregamos el estudiante actualizado al heap (su handle se actualiza automáticamente dentro del método 'agregar')
            Handle<Estudiante> h = puntajeMin.agregar(e); // O(log E)
            handles.set(e.id, h); // O(1)
        } // Complejidad del for anidado: O(n * (R + log E))
    } // Complejidad Total: O(n) + O(n * log E) + O(n * (R + log E)) = O(n * (1 + log E + R + log E)) = O(n * (R + log E))

 
//-------------------------------------------------ENTREGAR-------------------------------------------------------------


    public void entregar(int estudiante) { // O(log E)
        // Marcamos que el estudiante entregó y acutalizamos el heap
        Estudiante e = estudiantes.get(estudiante); // O(1)
        e.entrego = true; // O(1)
        handles.get(estudiante).actualizarValor(e); // O(log E) -> Edr llama al método definido en la interface del Handle (no sabe cómo se implementa el método dentro de la clase HandleHeap)
    } // Complejidad Total: O(log E)


//-----------------------------------------------------CORREGIR---------------------------------------------------------


    public NotaFinal[] corregir() {
        int n = cantEstudiantes - cantSospechosos;
        NotaFinal[] notas = new NotaFinal[n]; // O(E) en el peor caso
        int pos = n - 1;
        // Le cargamos al array las notas de los estudiantes que hayan entregado y no sean sospechosos
        while (puntajeMin.consultarMinimo() != null && pos >= 0) { // O(E)
            Estudiante e = puntajeMin.sacarMinimo(); // O(log E)
            if (!e.sospechoso) { // O(1)
                notas[pos] = new NotaFinal(e.nota, e.id); // O(1)
                pos--;
            }
        }
        return notas;
    } // Complejidad Total: O(E) + O(E * log E) = O(E * log E)


//-------------------------------------------------------CHEQUEAR COPIAS-------------------------------------------------


    public int[] chequearCopias() {
        int cantRespuestas = canonico.size();

        // Armamos una matriz que contiene la cantidad de veces que se puso la misma respuesta en cada ejercicio, recorriendo todos los estudiantes
        int[][] examenUniversal = new int[cantRespuestas][10]; // O(10 * R) = O(R)

        // Iteramos alumno por alumno y vamos completando la matriz con los ejercicios y respuestas que fueron realizando
        for (int i = 0; i < cantEstudiantes; i++){ // O(E)
            Estudiante est = estudiantes.get(i);
            for (int j = 0; j < cantRespuestas ; j++){ // O(R)
                int res = est.respuestas.get(j); // O(1)

                if(res != -1){
                    examenUniversal[j][res]++; // O(1)
                }
            }
        } // Complejidad del for anidado: O(E * R)

        ArrayList<Integer> sospechosos = new ArrayList<>(); // O(1)

        // Detectamos los sospechosos
        for (int i = 0; i < cantEstudiantes; i++){ // O(E)
            Estudiante est = estudiantes.get(i);
            if (cantEstudiantes > 1) {
                int contador = 0;

                for (int j = 0; j < cantRespuestas; j++){ // O(R)
                    int res = est.respuestas.get(j);
                    if(res != -1){
                        int respuestasAEjercicio = examenUniversal[j][res] - 1; // O(1)
                        if(respuestasAEjercicio >= (0.25 * (cantEstudiantes - 1))){
                            contador++; // O(1)
                        }
                    }
                }

                // Si es sospechosos lo agregamos
                if(contador == est.resueltos && est.resueltos > 0){ // O(1)
                    sospechosos.add(est.id);
                    cantSospechosos += 1;
                    est.sospechoso = true;
                }
            }
        } // Complejidad del for anidado: O(E * R)

        // Convertimos el array de sospechosos a uno de tamaño fijo
        int[] resultado = new int[sospechosos.size()]; // O(E) en el peor caso
        for (int i = 0; i < sospechosos.size(); i++){ // O(E)
            resultado[i] = sospechosos.get(i);
        }
        return resultado;
    } // Complejidad total: O(R) + O(E * R) + O(E * R) + O(E) + O(E) = O(E * R)
}