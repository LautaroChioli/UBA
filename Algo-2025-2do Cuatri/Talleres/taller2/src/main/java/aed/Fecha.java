package aed;

public class Fecha {
    private int _diaFecha;
    private int _mesFecha;

    public Fecha(int dia, int mes) {
        _diaFecha = dia;
        _mesFecha = mes;
    }

    public Fecha(Fecha fecha) {
        _diaFecha = fecha._diaFecha;
        _mesFecha = fecha._mesFecha;
    }

    public Integer dia() {

        return _diaFecha;
    }

    public Integer mes() {
        return _mesFecha;
    }

    public String toString() {
        return _diaFecha + "/" + _mesFecha;
    }

    @Override
    public boolean equals(Object otra) {
        boolean otraNoNull = otra != null;
        boolean esMismaClase = otraNoNull && otra.getClass() == this.getClass();

        if (esMismaClase) {
            Fecha otraFecha = (Fecha) otra;
            return this._diaFecha == otraFecha._diaFecha && this._mesFecha == otraFecha._mesFecha;
        }
        return false;
    }

    public void incrementarDia() {
        _diaFecha++;

        if (_diaFecha == 32 && _mesFecha == 12){
            _diaFecha = 1;
            _mesFecha = 1;
        }
        if (_diaFecha > diasEnMes(_mesFecha)) {
            _diaFecha = 1;
            _mesFecha++;
        
        }
    }

    private int diasEnMes(int mes) {
        int dias[] = {
                // ene, feb, mar, abr, may, jun
                31, 28, 31, 30, 31, 30,
                // jul, ago, sep, oct, nov, dic
                31, 31, 30, 31, 30, 31
        };
        return dias[mes - 1];
    }

}
