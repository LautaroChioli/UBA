package aed;
import java.util.ArrayList;

public class Edr {

    private ArrayList<Estudiante> estudiantes; // array de estudiantes
    private ArrayList<Integer> canonico; // plantilla del examen
    private Heap puntajeMin; // heap de puntajes
    private int ladoAula;
    private int cantEstudiantes;
    private int cantSospechosos;

    public Edr(int LadoAula, int Cant_estudiantes, int[] ExamenCanonico) {
        this.ladoAula = LadoAula;
        this.cantEstudiantes = Cant_estudiantes;
        this.cantSospechosos = 0;

        // Creamos el var canonico
        this.canonico = new ArrayList<>();
        for (int i = 0; i < ExamenCanonico.length; i++) { // O (R)
            this.canonico.add(ExamenCanonico[i]);
        }

        // Creamos el var estudiantes y el heap
        this.estudiantes = new ArrayList<>(); // O (E)
        this.puntajeMin = new Heap(Cant_estudiantes, estudiantes); // O (E)
        for (int i = 0; i < Cant_estudiantes; i++) { // O(E * R)
            Estudiante e = new Estudiante(i, ExamenCanonico.length, LadoAula);
            estudiantes.add(e); // O (R) por estudiante -> O (E * R)

            Heap.HeapStruct hs = new Heap.HeapStruct(i, false, 0.0);
            puntajeMin.agregar(hs); // O(1) por estudiante, porque no hace sift up ni sift down  -> O (E)
        }

    } // Complejidad Total: O (R) + O (E) + O (E) + O (E * R) = O (E * R)


//-------------------------------------------------NOTAS--------------------------------------------------------------------------


    public double[] notas(){
        // construimos el array resultado de tamaño igual a la cantidad de estudiantes
        double[] res = new double[cantEstudiantes]; // O (E)
        // recorremos la lista de estudiantes por id y copiamos la nota
        for (int i = 0; i < cantEstudiantes; i++) { // O (E)
            Estudiante e = estudiantes.get(i); // O (1)
            res[e.id] = e.nota; // O (1)
        }
        return res;
    } // Complejidad total: O(E)


//------------------------------------------------COPIARSE------------------------------------------------------------------------


    public void copiarse(int estudiante) {
        Estudiante est = estudiantes.get(estudiante); // O (1)
        int MayorRespuestasDiferentes = -1; // O (1)
        int idMVecinoMasDiferente = -1; // O (1)
        ArrayList<Integer> candidatos = vecinos(est); // O (1) -> la cantidad de vecinos siempre está acotada

        for (int vecinoID : candidatos){ // máximo 5 vecinos -> O (1) pero a cada vecino le recorremos su examen -> O (R)
            Estudiante vecino = estudiantes.get(vecinoID);
            int cont = 0;
            for (int i = 0; i < est.respuestas.size(); i++){ // O (R)
                if (vecino.respuestas.get(i) != -1 && est.respuestas.get(i) == -1){
                    cont++;
                }
            }
            if (cont > MayorRespuestasDiferentes || (cont == MayorRespuestasDiferentes && vecino.id > idMVecinoMasDiferente && cont != 0)){
                MayorRespuestasDiferentes = cont;
                idMVecinoMasDiferente = vecino.id;
            }
        }

        if (idMVecinoMasDiferente == -1 || MayorRespuestasDiferentes == 0){
            return;
        }

        Estudiante vecino = estudiantes.get(idMVecinoMasDiferente);

        for (int i = 0; i < est.respuestas.size(); i++){ // O (R)
            if (vecino.respuestas.get(i) != -1 && est.respuestas.get(i) == -1) {
                est.respuestas.set(i, vecino.respuestas.get(i));
                est.resueltos++;
                if (vecino.respuestas.get(i) == canonico.get(i)) {
                    est.nota += 100.0 / canonico.size();
                }
                puntajeMin.cambioDeNota(est.handleHeap, est.nota); // O (log E)
                break;
            }
        }
    }

    private ArrayList<Integer> vecinos(Estudiante est) { // Todo este método es O (1) puesto que la cantidad de vecinos posibles son acotadas y los cálculos de posiciones también se consiguen en O (1)
        ArrayList<Integer> vecs = new ArrayList<>();
        int cantAlumnosPorFila = ladoAula / 2;
        if (ladoAula % 2 != 0) {
            cantAlumnosPorFila += 1;
        }

        int indiceAsiento = est.id;

        // Misma fila: Asiento - 1
        if (estudiantes.get(indiceAsiento - 1).fila == est.fila) {
            int idVec = indiceAsiento - 1;
            if (idVec < cantEstudiantes) {
                vecs.add(idVec);
            }
        }
        // Misma fila: Asiento + 1
        if (indiceAsiento + 1 < cantEstudiantes && estudiantes.get(indiceAsiento + 1).fila == est.fila) {
            int idVec = indiceAsiento + 1;
            if (idVec < cantEstudiantes) {
                vecs.add(idVec);
            }
        }

        // Fila adelante
        int filaAdelante = est.fila - 1;
        if(filaAdelante >= 0){
            // Fila atrás: Mismo Asiento
            int idVecMismoAsiento = indiceAsiento - cantAlumnosPorFila;
            vecs.add(idVecMismoAsiento);
        }
        return vecs;
    } // Complejidad Total: O (R) + O (R) + O (log E) = 2 * O (R) + O (log E) = O (R + log E)


//-----------------------------------------------RESOLVER----------------------------------------------------------------


    public void resolver(int estudiante, int NroEjercicio, int res) {
        Estudiante e = estudiantes.get(estudiante); // O(1)
        e.respuestas.set(NroEjercicio, res); // O(1)
        e.resueltos += 1; // O(1)

        if (res == canonico.get(NroEjercicio)) { // O(1)
            e.nota += 100.0 / canonico.size(); // O(1)
        }
        puntajeMin.cambioDeNota(e.handleHeap, e.nota); // O (log E)
    } // Complejidad Total: O (log E)


//------------------------------------------------CONSULTAR DARK WEB-------------------------------------------------------


    public void consultarDarkWeb(int n, int[] examenDW) {
        ArrayList<Heap.HeapStruct> nPeores = new ArrayList<>(n); // O (n)

        // Metemos a los n peores al array nuevo. Hay que sacarlos si o si del heap.
        for (int i = 0; i < n; i++) { // O (n * log E)
            Heap.HeapStruct minimo = puntajeMin.consultarMinimo(); // O (1)
            if (minimo == null || minimo.entrego) {
                break;
            }
            minimo = puntajeMin.sacarMinimo(); // O (log E)
            nPeores.add(minimo);
        }

        // Reescribimos los datos de esos n peores
        for (Heap.HeapStruct elem : nPeores) { // O (n)
            Estudiante e = estudiantes.get(elem.id);
            e.resueltos = examenDW.length;
            e.nota = 0;

            for (int k = 0; k < examenDW.length; k++) { // O (R)
                e.respuestas.set(k, examenDW[k]);
                if (examenDW[k] == canonico.get(k)) {
                    e.nota += 100.0 / canonico.size();
                }
            } // -> O (n * R)
            // Actualizamos su nota en el heap al reinsertarlos
            elem.nota = e.nota;
            puntajeMin.agregar(elem); // reinsertar -> O (log E)
        }
    } // Complejidad Total: O (n * log E) + O (n * R) + O (n * log E) = O (n * (R + log E))

 
//-------------------------------------------------ENTREGAR-------------------------------------------------------------


    public void entregar(int estudiante) { // O (log E)
        Estudiante e = estudiantes.get(estudiante); // O (1)
        e.entrego = true; // O (1)
        puntajeMin.cambioDeEstado(e.handleHeap); // O (log E)
    } // Complejidad Total: O (log E)


//-----------------------------------------------------CORREGIR---------------------------------------------------------


    public NotaFinal[] corregir() {
        NotaFinal[] notas = new NotaFinal[cantEstudiantes - cantSospechosos]; // O (E)
        int pos = 0;
        for (int i = 0; i < cantEstudiantes; i++) { // O (E)
            Estudiante e = estudiantes.get(i);
            if (!e.sospechoso && e.entrego) { //ver si en el requiere está que hayan entregado
                notas[pos] = new NotaFinal(e.nota, e.id); // O (1)
                pos++;
            }
        }

        MergeSort.mergeSort(notas, pos); // O (E * log E)

        return notas;
    } // Complejidad Total: O (E) + O (E * log E) = O (E * log E)


//-------------------------------------------------------CHEQUEAR COPIAS-------------------------------------------------


    public int[] chequearCopias() {
        cantSospechosos = 0;
        int cantRespuestas = canonico.size();

        int[][] examenUniversal = new int[cantRespuestas][10]; // O (10 * R) = O (R)

        // Iteramos alumno por alumno y vamos completando la matriz con los ejercicios que fueron haciendo
        for (int i = 0; i < cantEstudiantes; i++){ // O (E)
            Estudiante est = estudiantes.get(i);
            for (int j = 0; j < cantRespuestas ; j++){ // O (R)
                int res = est.respuestas.get(j);

                if(res != -1){
                    examenUniversal[j][res]++;
                }
            }
        } // -> O (E * R)

        ArrayList<Integer> sospechosos = new ArrayList<>(); // O (1)

        // Detectamos los sospechosos
        for (int i = 0; i < cantEstudiantes; i++){ // O (E)
            Estudiante est = estudiantes.get(i);
            if (cantEstudiantes > 1) {
                int contador = 0;

                for (int j = 0; j < cantRespuestas; j++){ // O (R)
    
                    int res = est.respuestas.get(j);

                    if(res != -1){
                        int respuestasAEjercicio = examenUniversal[j][res] - 1;
                        if(respuestasAEjercicio >= (0.25 * (cantEstudiantes - 1))){
                            contador++;
                        }
                    }
                }

                // Si es sospechosos lo agregamos
                if(contador == est.resueltos && est.resueltos > 0){ // O (1)
                    sospechosos.add(est.id);
                    cantSospechosos += 1;
                    est.sospechoso = true;
                }
            }
        }

        int[] resultado = new int[sospechosos.size()]; // O (E) en el peor caso
        for (int i = 0; i < sospechosos.size(); i++){
            resultado[i] = sospechosos.get(i);
        }
        return resultado;
    } // Complejidad total: O (R + E * R + E * R + E) = O (E * R)
}