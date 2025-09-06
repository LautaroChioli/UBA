package aed;

public class Agenda {
    private Fecha _fecha;
    private ArregloRedimensionableDeRecordatorios _recordatorios;

    public Agenda(Fecha fechaActual) {
        _fecha = fechaActual;
        _recordatorios = new ArregloRedimensionableDeRecordatorios();
    }

    public void agregarRecordatorio(Recordatorio recordatorio) {
        _recordatorios.agregarAtras(recordatorio);
    }

    @Override
    public String toString() {
        String res = "";
        res += _fecha.toString() + "\n";
        res += "=====\n";
        for (int i = 0; i < _recordatorios.longitud(); i++){
            Recordatorio rec = _recordatorios.obtener(i);
            if (rec.fecha().equals(fechaActual())){
                res += rec.toString() + "\n";
            }
        } 
        return res;
    }

    public void incrementarDia() {
        _fecha.incrementarDia();
    }

    public Fecha fechaActual() {
        Fecha nuevaFecha = new Fecha(_fecha);
        return nuevaFecha;
    }

}
