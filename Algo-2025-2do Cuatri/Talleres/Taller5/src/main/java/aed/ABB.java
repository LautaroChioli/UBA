
public class ABB<T extends Comparable<T>> {
    private Nodo raiz;
    private int cant;


    private class Nodo {
       T valor;
        Nodo izq;
        Nodo der;
        Nodo padre;
        HandleABB handle;

        public Nodo(T v){
            this.valor = v;
            this.der = null;
            this.izq = null;
            this.padre = null;
            this.handle = null;
        }
       

    }

    public class HandleABB {
        private Nodo nodoReferenciado;
        private ABB<T> arbol;

        public HandleABB(ABB<T> arbol, Nodo nodo) {
            this.arbol = arbol;
            this.nodoReferenciado = nodo;
        }
        
        public T valor() {
            return nodoReferenciado.valor;
        }

        public void eliminar(){
            arbol.eliminarNodoDirecto(nodoReferenciado);
        }}

    private void eliminarNodoDirecto(Nodo nodoAEliminar) {
        if (nodoAEliminar == null) {
            return;
        }

        if (nodoAEliminar.izq == null && nodoAEliminar.der == null) {
            enlazar(nodoAEliminar,null); 
            cant--;
        }

        else if (nodoAEliminar.izq == null) {
            enlazar(nodoAEliminar, nodoAEliminar.der);
            cant--;
        } 
        else if (nodoAEliminar.der == null) {
            enlazar(nodoAEliminar, nodoAEliminar.izq);
            cant--;
        }

        else {
            Nodo sucesor = encontrarMinimo(nodoAEliminar.der);
            nodoAEliminar.valor = sucesor.valor;

            HandleABB handleDelNodoAEliminar = nodoAEliminar.handle;
            HandleABB handleDelSucesor = sucesor.handle;

            handleDelNodoAEliminar.nodoReferenciado = sucesor;
            handleDelSucesor.nodoReferenciado = nodoAEliminar;

            nodoAEliminar.handle = handleDelSucesor;
            sucesor.handle = handleDelNodoAEliminar;

            eliminarNodoDirecto(sucesor);
        }
    }
    private void enlazar(Nodo nodoViejo, Nodo nodoNuevo) {
        
        if (nodoViejo.padre == null) {
            this.raiz = nodoNuevo;
        } 
        else if (nodoViejo == nodoViejo.padre.izq) {
            nodoViejo.padre.izq = nodoNuevo;
        } 
        else {
            nodoViejo.padre.der = nodoNuevo;
        }
        if (nodoNuevo != null) {
            nodoNuevo.padre = nodoViejo.padre;
        }
    }

    private Nodo encontrarMinimo(Nodo nodo) {
        while (nodo.izq != null) {
            nodo = nodo.izq;
        }
        return nodo;
    }
    

    public ABB() {
       this.raiz = null;
    }

    public T minimo(){
         Nodo actual = this.raiz;
        while (actual.izq != null){
            actual = actual.izq;
        }
        return actual.valor;
    }

    public HandleABB insertar(T elem){
        Nodo padre = null;
        Nodo actual = this.raiz;

        while (actual != null) {
            padre = actual;
            int comp = elem.compareTo(actual.valor);

            if (comp < 0) {
                actual = actual.izq;
            } else if (comp > 0) {
                actual = actual.der;
            } else {
                return new HandleABB(this, actual);
            }
        }
        Nodo nuevoNodo = new Nodo(elem);
        HandleABB nuevoHandle = new HandleABB(this, nuevoNodo);
        nuevoNodo.handle = nuevoHandle;
        nuevoNodo.padre = padre;

        if (padre == null) {
            this.raiz = nuevoNodo; 
        } else if (elem.compareTo(padre.valor) < 0) {
            padre.izq = nuevoNodo;
        } else {
            padre.der = nuevoNodo;
        }

        this.cant++;
        return nuevoHandle;
    }

    private Nodo buscarNodo(T elem) {
        Nodo actual = this.raiz;
        while (actual != null) {
            int comp = elem.compareTo(actual.valor);
            if (comp == 0) {
                return actual; 
            } else if (comp < 0) {
                actual = actual.izq; 
            } else {
                actual = actual.der; 
            }
        }
        return null; 
    }
    public int cardinal() {
        return this.cant;

    }
    public T maximo(){
        Nodo actual = this.raiz;
        while (actual.der != null){
            actual = actual.der;
        }
        return actual.valor;
    }

    public boolean pertenece(T elem){
        return buscarNodo(elem) != null;
    }

    public void eliminar(T elem){
        Nodo nodoAEliminar = buscarNodo(elem);
        if (nodoAEliminar != null) {
            eliminarNodoDirecto(nodoAEliminar);
        }
    }

    @Override
    public String toString(){
         StringBuffer res = new StringBuffer("{");

        if (this.raiz == null){
            res.append("}");
            return res.toString();
        }

        busquedaRecursiva(this.raiz, res);

        res.delete(res.length() - 1, res.length());
        res.append("}");
        return res.toString();

    }
    private void busquedaRecursiva(Nodo actual, StringBuffer res){
        if (actual == null){
            return;
        }

        busquedaRecursiva(actual.izq, res);

        res.append(actual.valor.toString());
        res.append(",");

        busquedaRecursiva(actual.der, res);
    }


    public class ABB_Iterador {
         private Nodo _actual;

       public ABB_Iterador() {
            if (ABB.this.raiz == null) {
                this._actual = null;
            } else {
                Nodo nodo = ABB.this.raiz;
                while (nodo.izq != null) {
                    nodo = nodo.izq;
                }
                this._actual = nodo;
            }
        }
        public boolean haySiguiente() {            
            return this._actual != null;
        }
    
        public T siguiente() {
            T valor = this._actual.valor;
            Nodo nodoAnterior = this._actual;

            if (nodoAnterior.der != null){
                this._actual = nodoAnterior.der;
                while (this._actual.izq != null){
                    this._actual = this._actual.izq;
                }
            }
            else {
                Nodo hijo = nodoAnterior;
                Nodo padre = nodoAnterior.padre;

                while (padre != null && hijo == padre.der){
                    hijo = padre;
                    padre = padre.padre;
                }
                this._actual = padre;
            }
            return valor;
        }

    }

    public ABB_Iterador iterador() {
        return new ABB_Iterador();
    }}


