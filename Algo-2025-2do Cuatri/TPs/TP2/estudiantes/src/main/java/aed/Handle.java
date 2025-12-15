package aed;

public interface Handle<T> {
    /**
     * Devuelve el valor del elemento
     */
    public T valor();

    /**
     * Dado un valor, lo reubica en el heap
     */
    public void actualizarValor(T valor);
}