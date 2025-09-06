package aed;

public class Horario {
    private int _hora;
    private int _minutos;

    public Horario(int hora, int minutos) {
        _hora = hora;
        _minutos = minutos;
    }

    public int hora() {
        return _hora;
    }

    public int minutos() {
        // Implementar
        return _minutos;
    }

    @Override
    public String toString() {
        
        return _hora + ":" + _minutos;
    }

    @Override
    public boolean equals(Object otro) {
        boolean noEsNulo = otro!= null;
        boolean esMismaClase = otro.getClass() == this.getClass() && noEsNulo;

        if (esMismaClase){
            Horario otroHorario = (Horario) otro;
            return otroHorario._hora == this._hora && otroHorario._minutos == this._minutos;
        }

        return false;
    }

}
