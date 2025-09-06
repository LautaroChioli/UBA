package aed;

class ArregloRedimensionableDeRecordatorios {
    private Recordatorio[] _arreglo; 
    public ArregloRedimensionableDeRecordatorios() {
        _arreglo = new Recordatorio[0];
    }

    public int longitud() {
        return _arreglo.length;
    }

    public void agregarAtras(Recordatorio i) {
        Recordatorio[] nuevoArreglo = new Recordatorio[_arreglo.length + 1];
        for (int k = 0; k < _arreglo.length; k++){
            nuevoArreglo[k] = _arreglo[k];
        } 
        nuevoArreglo[_arreglo.length] = i;
        _arreglo = nuevoArreglo;
    }

    public Recordatorio obtener(int i) {
        return _arreglo[i];
    }

    public void quitarAtras() {
        Recordatorio[] nuevoArreglo = new Recordatorio[_arreglo.length - 1];
        for (int i = 0; i < _arreglo.length - 1; i++){
            nuevoArreglo[i] = _arreglo[i];
        }
        _arreglo = nuevoArreglo;
    }

    public void modificarPosicion(int indice, Recordatorio valor) {
        _arreglo[indice] = valor;
    }

    public ArregloRedimensionableDeRecordatorios(ArregloRedimensionableDeRecordatorios vector) {
        this._arreglo = new Recordatorio[vector._arreglo.length];
        for (int i = 0; i < _arreglo.length; i++) {
            this._arreglo[i] = new Recordatorio(vector.obtener(i).mensaje(), vector.obtener(i).fecha(), vector.obtener(i).horario());
        }
    }

    public ArregloRedimensionableDeRecordatorios copiar() {
        return new ArregloRedimensionableDeRecordatorios(this);
    }
}
