package aed;

public class MergeSort { // O (E * log E)


    public static void mergeSort(NotaFinal [] array, int largo){
        if (largo <= 1){
            return;
        }

        int mitad = largo / 2;
        NotaFinal[] izq = new NotaFinal[mitad];            
        NotaFinal [] der = new NotaFinal [largo - mitad];       // creo nuevos arrays con largo de la mitad del anterior

        for (int i = 0; i < mitad; i++){
            izq[i] = array[i];
        }
        for (int i = mitad; i < largo; i++){
            der[i - mitad] = array[i];
        }

        mergeSort(izq, mitad); //divide toda la mitad izquierda
        mergeSort(der, largo - mitad); //diivide toda la mitad derecha

        merge(array, izq, der);
    }

    public static void merge(NotaFinal[] res, NotaFinal[] izq, NotaFinal[] der){
        int mitadIzq = izq.length;
        int mitadDer = der.length;
        int i = 0;
        int n = 0;
        int m = 0;
        
        while (i < mitadIzq && n < mitadDer){
            if(izq[i]._nota > der[n]._nota || izq[i]._nota == der[n]._nota && izq[i]._id > der[n]._id){
                res[m] = izq[i];
                i++;
            } else {
                res[m] = der[n];
                n++;
            }
            m++;
        }
        while (i < mitadIzq){
            res[m] = izq[i];
            m++;
            i++;
        }
        while(n < mitadDer){
            res[m] = der[n];
            m++;
            n++;
        }
    } 
}