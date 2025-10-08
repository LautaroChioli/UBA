package aed;

public class ListaEnlazada<T> {
    private Nodo primero;
    private Nodo ultimo;
    private int longitud;

    private class Nodo {
        T valor;
        Nodo sig;
        Nodo ant;

        Nodo (T v) {valor = v;}
    }

    public ListaEnlazada() {
        primero = null;
        ultimo = null;
        longitud = 0;
    }

    public int longitud() {
        return this.longitud;
    }

    public void agregarAdelante(T elem) {
        Nodo nuevo = new Nodo(elem);
        if (primero == null){
            primero = nuevo;
            ultimo = nuevo;
            
        }
        else{
            nuevo.sig = primero;
            nuevo.ant = null;
            primero.ant = nuevo;
            primero = nuevo;

        }
        longitud ++;

    }

    public void agregarAtras(T elem) {
        Nodo nuevo = new Nodo(elem);
        if (primero == null){
            primero = nuevo;
            ultimo = nuevo;
        }else{
            nuevo.sig = null;
            nuevo.ant = ultimo;
            ultimo.sig = nuevo;
            ultimo = nuevo;
        }
        longitud ++;
    }

    public T obtener(int i) {
        int cont = 0;
        Nodo actual = primero;

        while (cont != i){
            actual = actual.sig;
            cont ++;
        }
        System.out.println("Obteniendo índice " + i + ", valor encontrado: " + actual.valor);
        return actual.valor;
    }

    public void eliminar(int i) {
        int cont = 0;
        Nodo actual = primero;
        if (longitud == 1){
        primero = null;
        ultimo = null;

        }else if(i == 0) {
        primero = primero.sig;
        primero.ant = null;

        }else if (i == longitud - 1) {
        ultimo = ultimo.ant;
        ultimo.sig = null;

        }else{
        while(cont != i){
            actual = actual.sig;
            cont ++;
        }
        actual.ant.sig = actual.sig;
        actual.sig.ant = actual.ant;}
        longitud --;


    }

    public void modificarPosicion(int indice, T elem) {
    }

    public ListaEnlazada(ListaEnlazada<T> lista) {
    }
    
    @Override
    public String toString() {
    }

    public class ListaIterador{
    	int pointer;
        

        public boolean haySiguiente() {
        }
        
        public boolean hayAnterior() {
        }

        public T siguiente() {
        }
        

        public T anterior() {
        }
    }

    public ListaIterador iterador() {
    }


}

