package aed;

import java.util.ArrayList;

public class Heap {
    private ArrayList<HeapStruct> array;
    private int cantidad; // número de elementos en el heap
    private ArrayList<Estudiante> estudiantes; // lista de estudiantes para actualizar los handles

    public Heap(int capacidad, ArrayList<Estudiante> estudiantes) { // Crearlo -> O (E)
        this.array = new ArrayList<>(estudiantes.size()); // array de tamaño a lo sumo |estudiantes|
        this.cantidad = 0;
        this.estudiantes = estudiantes;
    }

    public void agregar(HeapStruct elem) { // O (log E)
        if (cantidad < array.size()) {
            array.set(cantidad, elem);
        } else {
            array.add(elem); // O(1)
        }
        estudiantes.get(elem.id).handleHeap = cantidad;
        siftUp(cantidad); // O (log E)
        cantidad++;
    }

    public HeapStruct consultarMinimo() { // O (1)
        if (cantidad == 0) {
            return null;
        }
        return array.get(0);
    }

    public HeapStruct sacarMinimo() { // O (log E)
        if (cantidad == 0) {
            return null;
        }
        HeapStruct minimo = array.get(0);
        estudiantes.get(minimo.id).handleHeap = -1;
        // mover último al primero
        if (cantidad == 1) {
            array.remove(0);
            cantidad = 0;
            return minimo;
        }
        HeapStruct ultimo = array.get(cantidad - 1);
        array.set(0, ultimo);
        estudiantes.get(ultimo.id).handleHeap = 0;

        // quitamos el último
        array.remove(cantidad - 1);
        cantidad--;

        // reordenamos
        siftDown(0);

        return minimo;
    }

    public void actualizar(int posicion) { // O (log E)
        if (posicion < 0 || posicion >= cantidad) {
            return;
        }
        siftUp(posicion);
        siftDown(posicion);
    }

    private void siftUp(int i) { // O (log E)
        int padre = (i - 1) / 2;
        while (i > 0 && comparar(array.get(i), array.get(padre)) < 0) {
            swap(i, padre);
            i = padre;
            padre = (i - 1) / 2;
        }
    }

    private void siftDown(int i) { // O (log E)
        int menor = i;
        boolean sePuedeOrdenar = true;
        while (sePuedeOrdenar) {
            int hijoIzq = 2 * i + 1;
            int hijoDer = 2 * i + 2;
            menor = i;

            if (hijoIzq < cantidad && comparar(array.get(hijoIzq), array.get(menor)) < 0) {
                menor = hijoIzq;
            }
            if (hijoDer < cantidad && comparar(array.get(hijoDer), array.get(menor)) < 0) {
                menor = hijoDer;
            }

            if (menor != i) {
                swap(i, menor);
                i = menor;
            } else {
                sePuedeOrdenar = false;
            }
        }
    }

    private void swap(int i, int k) { // O (1)
        HeapStruct elem1 = array.get(i);
        HeapStruct elem2 = array.get(k);
        array.set(i, elem2);
        array.set(k, elem1);

        // actualizar handles
        estudiantes.get(array.get(i).id).handleHeap = i;
        estudiantes.get(array.get(k).id).handleHeap = k;
    }

    private int comparar(HeapStruct a, HeapStruct b) { // Comparador -> O (1)
        // 1) Prioridad: quien NO entregó primero
        if (!a.entrego && b.entrego) return -1;
        if (a.entrego && !b.entrego) return 1;

        // 2) Nota ascendente
        if (a.nota < b.nota) return -1;
        if (a.nota > b.nota) return 1;

        // 3) Si empataron en estado de entrega y nota, desempate por id ascendente
        if (a.id < b.id) return -1;
        if (a.id > b.id) return 1;

        return 0; // serían iguales
    }

    public void cambioDeEstado(int posicion) { // O (log E)
        if (posicion < 0 || posicion >= cantidad) {
            return;
        }
        array.get(posicion).entrego = true; // O (1)
        actualizar(posicion); // reordena en O (log E)
    }

    public void cambioDeNota(int posicion, double nuevaNota) { // O (log E)
        if (posicion < 0 || posicion >= cantidad) {
            return;
        }
        array.get(posicion).nota = nuevaNota; // O (1)
        actualizar(posicion); // reordena en O (log E)
    }

    // clase interna del struct del Heap
    public static class HeapStruct {
        public boolean entrego;
        public double nota;
        public int id;

        public HeapStruct(int idEstudiante, boolean entrego, double nota) {
            this.id = idEstudiante;
            this.entrego = entrego;
            this.nota = nota;
        }
    }

    // clase interna del Handle que referencia posición en el Heap
    public static class HandleHeap implements Handle<Integer> {
        private int posicion;

        public HandleHeap(int pos) {
            this.posicion = pos;
        }

        @Override
        public Integer valor() {
            return posicion;
        }

        @Override
        public void eliminar() {
            // el Handle no elimina elementos del Heap, entonces no debe implementarse
        }

        public void setPosicion(int pos) {
            this.posicion = pos;
        }
    }
}