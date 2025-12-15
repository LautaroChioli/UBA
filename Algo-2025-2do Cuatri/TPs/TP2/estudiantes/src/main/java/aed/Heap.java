package aed;

import java.util.ArrayList;

public class Heap<T extends Comparable<T>> {
    private ArrayList<HandleHeap> array; // elementos del heap genérico
    private int cantidad; // número de elementos en el heap

    public Heap(int capacidad) { // Crearlo -> O(E)
        this.array = new ArrayList<>(capacidad); // array de tamaño |estudiantes|
        this.cantidad = 0;
    }

    // Método para inserción rápida (sin ordenar) en el heap
    public Handle<T> insertarRapido(T elem) { // O(1)
        HandleHeap handle = new HandleHeap(elem, cantidad); // O(1)
        if (cantidad < array.size()) {
            array.set(cantidad, handle);
        } else {
            array.add(handle);
        }
        cantidad++; // incrementamos la cantidad de elementos
        return handle;
    }

    // Método para agregar elementos y posteriormente ordenarlos (sólo utilizado en el método consultarDarkWeb)
    public Handle<T> agregar(T elem) { // O(log E)
        HandleHeap handle = new HandleHeap(elem, cantidad);
        // Insertamos en la siguiente posición libre del heap
        if (cantidad < array.size()) {
            array.set(cantidad, handle); // O(1)
        } else {
            array.add(handle); // O(1)
        }
        // Reordenamos
        siftUp(cantidad); // O(log E)
        cantidad++; // O(1)
        return handle;
    }

    public T consultarMinimo() { // O(1) 
        if (cantidad == 0) {
            return null;
        }
        return array.get(0).valor();
    }

    public T sacarMinimo() { // O(log E)
        if (cantidad == 0) {
            return null;
        }

        T minimo = array.get(0).valor();
        HandleHeap ultimo = array.get(cantidad - 1);

        array.set(0, ultimo); // llevamos ultimo elem a la raiz
        ultimo.posicion = 0;
        cantidad--; // reducimos antes de siftDown

        siftDown(0); // reordenamos en O(log E)

        return minimo;
    }

    private void siftUp(int i) { // O(log E)
        int padre = (i - 1) / 2;

        // Este ciclo se ejecuta a lo sumo la altura del heap veces -> O(log E)
        while (i > 0 && array.get(i).valor().compareTo(array.get(padre).valor()) < 0) {
            swap(i, padre); // O(1)
            i = padre; // O(1)
            padre = (i - 1) / 2; // O(1)
        }
    }

    private void siftDown(int i) { // O(log E)
        boolean continuar = true; // O(1)

        while (continuar) { // O(log E)
            int hijoIzq = 2 * i + 1;
            int hijoDer = 2 * i + 2;
            int menor = i;

            // Buscamos el menor de los tres índices
            if (hijoIzq < cantidad && array.get(hijoIzq).valor().compareTo(array.get(menor).valor()) < 0) { // O(1)
                menor = hijoIzq;
            }
            if (hijoDer < cantidad && array.get(hijoDer).valor().compareTo(array.get(menor).valor()) < 0) { // O(1)
                menor = hijoDer;
            }

            //Si el menor no es el actual, swapeamos
            if (menor != i) { // O(1)
                swap(i, menor); // O(1)
                i = menor;
            } else {
                continuar = false;
            }
        }
    }

    private void swap(int i, int j) { // O(1)

        HandleHeap temp1 = array.get(i);
        HandleHeap temp2 = array.get(j);

        // Swap de elementos
        array.set(i, temp2);
        array.set(j, temp1);

        // Actualizamos la posición de cada handle
        temp1.posicion = j;
        temp2.posicion = i;
    }

    // Método privado que sólo es invocado por un handle al cambiar su valor
    // Ahora el Edr no lo llama directamente porque el reordenamiento del heap debe ser una operación interna del mismo heap
    private void actualizar(HandleHeap h) { // O(log E)
        int pos = h.posicion;
        siftUp(pos);
        siftDown(pos);
    }

    // Clase interna y privada que implementa los handles del heap
    // Guarda el valor genérico de tipo T y la posición actual de ese valor dentro del array del heap
    // Ahora el Edr no llama a la clase HandleHeap, sino que interactúa con la interface Handle (ahora nunca visualiza ni crea un HandleHeap)
    private class HandleHeap implements Handle<T> {
        private T valor; // Valor almacenado en el heap
        private int posicion; // Índice actual en el array del heap

        // Constructor privado para ser llamado en el heap
        private HandleHeap(T valor, int pos) {
            this.valor = valor;
            this.posicion = pos;
        }

        @Override
        public T valor() { // Devuelve el valor asociado al handle
            return valor;
        }

        @Override
        public void actualizarValor(T nuevoValor) { // Cambia el valor del handle y luego el heap decide como reordenarse
            this.valor = nuevoValor;
            Heap.this.actualizar(this);
        }
    }
}