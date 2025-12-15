package aed;

import java.util.ArrayList;

public class Estudiante implements Comparable<Estudiante> {
    public int id;
    public ArrayList<Integer> respuestas;
    public boolean entrego;
    public boolean sospechoso;
    public double nota;
    public int fila; // posición en el aula (fila)
    public int columna; // posición en el aula (columna)
    public int resueltos;

    // Constructor
    public Estudiante(int id, int largoCanonico, int ladoAula) {
        this.id = id;
        this.entrego = false;
        this.sospechoso = false;
        this.nota = 0.0;
        this.respuestas = new ArrayList<>();
        this.resueltos = 0;

        // Inicializamos todas las respuestas con -1
        for (int i = 0; i < largoCanonico; i++) {
            this.respuestas.add(-1);
        }

        // Calculamos su posición en el aula
        int cantAlumnosPorFila = ladoAula / 2;
        if (ladoAula % 2 != 0) {
            cantAlumnosPorFila++; // Si es impar, sumamos 1
        }
        this.fila = id / cantAlumnosPorFila;
        this.columna = id % cantAlumnosPorFila;
    }

    // Comparador
    @Override
    public int compareTo(Estudiante otro) {

        // Prioridades:

        // Primero: los que no entregaron van antes
        if (this.entrego && !otro.entrego) {
            return 1;
        }
        if (!this.entrego && otro.entrego) {
            return -1;
        }
        
        // Segundo (en caso de empate): nota menor antes
        if (this.nota < otro.nota) {
            return -1;
        }
        if (this.nota > otro.nota) {
            return 1;
        }
        
        // Tercero (en caso de empate en entrega y nota): desempata por id (menor id primero)
        return Integer.compare(this.id, otro.id);
    }
}