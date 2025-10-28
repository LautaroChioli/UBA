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
        int cont = 0;
        Nodo actual = primero;
        while(cont != indice){
            actual = actual.sig;
            cont ++;
        }
        actual.valor = elem;
    }

    public ListaEnlazada(ListaEnlazada<T> lista) {
        if (lista.primero == null){
            this.longitud = 0;  
            this.primero = null;
            this.ultimo = null;
            return;
        }
        this.primero = new Nodo(lista.primero.valor);

        Nodo ultimoNuevo = this.primero;
        Nodo actualNueva = lista.primero.sig;


        while (actualNueva != null){
            Nodo nuevo = new Nodo(actualNueva.valor);
            
            nuevo.ant = ultimoNuevo;
            ultimoNuevo.sig = nuevo;
            ultimoNuevo = nuevo;

            actualNueva = actualNueva.sig;
        }

        this.ultimo = ultimoNuevo;
        this.longitud = lista.longitud;
    }
    
    @Override
    public String toString() {
        StringBuffer cadena = new StringBuffer("[");
        Nodo actual = primero;
        while (actual != null){ 
            cadena.append(actual.valor);
            if (actual.sig != null){
                cadena.append(", ");
            }
            actual = actual.sig;
        }
        cadena.append("]");
        return cadena.toString();
    }

    public class ListaIterador{
    	int pointer;
        Iterador(){
            this.pointer = 0;
        }

        public boolean haySiguiente() {
            return pointer < longitud;
        }
        
        public boolean hayAnterior() {
            return pointer > 0;
        }

        public T siguiente() {
            T valorAntes = obtener(pointer);
            pointer ++;
            return valorAntes;
        }
        

        public T anterior() {
            pointer --;
            return obtener(pointer);
        }
    }

    public ListaIterador iterador() {
        return new ListaIterador();
    }


}

