package aed;

public class Recordatorio {
    private String _mensaje;
    private Fecha _fecha;
    private Horario _horario;
    public Recordatorio(String mensaje, Fecha fecha, Horario horario) {
        _mensaje = mensaje;
        _fecha = new Fecha(fecha.dia(), fecha.mes());
        _horario = new Horario(horario.hora(), horario.minutos());
    }

    public Horario horario() {
        return new Horario(_horario.hora(), _horario.minutos());
    }

    public Fecha fecha() {
        return  new Fecha(_fecha.dia(), _fecha.mes());
    }

    public String mensaje() {
        return _mensaje;
    }

    @Override
    public String toString() {
        return _mensaje + " @ " + _fecha + " " + _horario;
    }

    @Override
    public boolean equals(Object otro) {
        boolean noEsNull = (otro != null);
        boolean esMismaClase = noEsNull && (otro.getClass() == this.getClass());

        if (esMismaClase){
            Recordatorio nuevoRecordatorio = (Recordatorio) otro;
            return this.mensaje().equals(nuevoRecordatorio.mensaje()) &&
           this.fecha().equals(nuevoRecordatorio.fecha()) &&
           this.horario().equals(nuevoRecordatorio.horario());
        }
        return false;
    }

}
