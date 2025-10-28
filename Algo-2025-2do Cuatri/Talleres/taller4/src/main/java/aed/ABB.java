
import java.util.*;

// Todos los tipos de datos "Comparables" tienen el método compareTo()
// elem1.compareTo(elem2) devuelve un entero. Si es mayor a 0, entonces elem1 > elem2
public class ABB<T extends Comparable<T>> {
    private Nodo raiz;
    private int cant;

    private class Nodo {
        T valor;
        Nodo izq;
        Nodo der;
        Nodo padre;

        public Nodo(T v){
            this.valor = v;
            this.der = null;
            this.izq = null;
            this.padre = null;
        }
       
    }

    public ABB() {
        this.raiz = null;
    }

    public int cardinal() {
        return this.cant;

    }

    public T minimo(){
        Nodo actual = this.raiz;
        while (actual.izq != null){
            actual = actual.izq;
        }
        return actual.valor;
    }

    public T maximo(){
        Nodo actual = this.raiz;
        while (actual.der != null){
            actual = actual.der;
        }
        return actual.valor;
    }

    public void insertar(T elem){
        Nodo insertado = new Nodo(elem);
        
        if (this.raiz == null){
            this.raiz = insertado;
            this.cant ++;
            return;
        }
        Nodo actual = this.raiz;
        Nodo padreDeActual = null;
        while (actual != null){
            if (actual.valor.compareTo(elem) > 0) {
                padreDeActual = actual;
                actual = actual.izq;
            } else if (actual.valor.compareTo(elem) < 0){
                padreDeActual = actual;
                actual = actual.der;
            } else {
                return;
            }
        }
        insertado.padre = padreDeActual;

        if (insertado.padre.valor.compareTo(elem) > 0){
            padreDeActual.izq = insertado;
        }else{
            padreDeActual.der = insertado;
        }
        this.cant ++;
    }

    public boolean pertenece(T elem){
        Nodo actual = this.raiz;
        while (actual != null){
            if (actual.valor.compareTo(elem) > 0) {
                actual = actual.izq;
            }
            else if (actual.valor.compareTo(elem) < 0){
                actual = actual.der;
            }
            else{
                return true;
            }
        }
        return false;
    }

    public void eliminar(T elem){
        Nodo eliminado = this.raiz;

        while(eliminado != null){
            if (eliminado.valor.compareTo(elem) == 0){
                break;
            }
            else if (eliminado.valor.compareTo(elem) > 0) {
                eliminado = eliminado.izq;
            } else{
                eliminado = eliminado.der;
            }
        }

        if (eliminado == null){
            return;
        }

        if (eliminado.izq == null && eliminado.der == null){   //CASO ELIMINADO ES HOJA
            eliminadoEsHoja(eliminado);
            }
        //////////////////////////////////////////////////////////////////////////////////////////
        else if (eliminado.der == null || eliminado.izq == null){ //CASAO ELIMINADO TIENE UN HIJO
            eliminadoUnHijo(eliminado);
        } ////////////////////////////////////////////////////////////////////////////////////
        else{                                           // CASO ELIMINADO TIENE DOS HIJOS
            Nodo sucesor = eliminado.der;
            while(sucesor.izq != null){
                sucesor = sucesor.izq;
            }
            eliminado.valor = sucesor.valor;

            if (sucesor.izq == null && sucesor.der == null){
                eliminadoEsHoja(sucesor);
            }
            else {
                eliminadoUnHijo(sucesor);
            }
        }

        this.cant --;
    }

    private void eliminadoEsHoja(Nodo eliminado){
            if (eliminado.padre == null){
                this.raiz = null;
            }
            else {
                if (eliminado.padre.izq == eliminado){
                    eliminado.padre.izq = null;
                }
                else{
                    eliminado.padre.der = null;
                }
            }
    }
    
    private void eliminadoUnHijo(Nodo eliminado){
        Nodo hijo;
        if (eliminado.izq != null){
            hijo = eliminado.izq;
        } else{
            hijo = eliminado.der;
        }

        hijo.padre = eliminado.padre;

        if(eliminado.padre == null){
            this.raiz = hijo;
        } else if (eliminado.padre.izq == eliminado){
            eliminado.padre.izq = hijo;
        } else{
            eliminado.padre.der = hijo;
        }

    }


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
    }

}
