package aed;

public class NotaFinal implements Comparable<NotaFinal> {
    public double _nota;
    public int _id;

    public NotaFinal(double nota, int id){
        _nota = nota;
        _id = id;
    }

    public int compareTo(NotaFinal otra){
        if (otra._id != this._id){
            return this._id - otra._id;
        }
        return Double.compare(this._nota, otra._nota);
    }

    @Override
    public boolean equals(Object otra) {
        // Comparamos por contenido: dos NotaFinal son iguales si tienen misma nota y mismo id.
        // Tuvimos que implementarlo porque en los tests se compara igualdad lógica y no referencia de objetos.
        boolean otraNoEsNull = otra != null;
        boolean esObjetoDeLaMismaClase = otraNoEsNull && (otra.getClass() == this.getClass());
        int otro_id = 0;
        double otra_nota = 0.0;
        if (esObjetoDeLaMismaClase) {
            otro_id = ((NotaFinal) otra)._id;
            otra_nota = ((NotaFinal) otra)._nota;
        }
        return esObjetoDeLaMismaClase && (_id == otro_id && _nota == otra_nota);
    }
}