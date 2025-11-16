package aed;

import java.util.ArrayList;

public class Estudiante {
    public int id;
    public ArrayList<Integer> respuestas;
    public boolean entrego;
    public boolean sospechoso;
    public double nota;
    public int resueltos;
    public int fila; // posición en el aula
    public int columna; // posición en el aula
    public int handleHeap; // posición en el heap

    // Constructor
    public Estudiante(int id, int largoCanonico, int ladoAula) {
        this.id = id;
        this.entrego = false;
        this.sospechoso = false;
        this.nota = 0;
        this.resueltos = 0;
        this.respuestas = new ArrayList<>();

        // inicializar todas las respuestas con -1
        for (int i = 0; i < largoCanonico; i++) {
            this.respuestas.add(-1);
        }

        // calcular posición en el aula
        int cantAlumnosPorFila = ladoAula / 2;
        if (ladoAula % 2 != 0) {
            cantAlumnosPorFila++; // si impar, sumamos 1
        }
        this.fila = id / cantAlumnosPorFila;
        this.columna = id % cantAlumnosPorFila;
        this.handleHeap = -1; // inicialmente no tiene posición en el heap
    }

    // Verificar si otro estudiante es vecino
    public boolean esVecino(Estudiante otro) {
        // vecinos horizontales (separación de 1 asiento)
        if (this.fila == otro.fila && (this.columna - otro.columna == 2 || otro.columna - this.columna == 2)) {
            return true;
        }

        // vecinos verticales (separación de una fila)
        if (this.columna == otro.columna && (this.fila - otro.fila == 1 || otro.fila - this.fila == 1)) {
            return true;
        }
        return false;
    }
}