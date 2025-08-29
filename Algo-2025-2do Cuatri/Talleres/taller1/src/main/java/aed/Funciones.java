package aed;

class Funciones {

/***  Primera parte: Funciones en java ***/

    int cuadrado(int x) {
        return x * x;
    }

    double distancia(double x, double y) {
        return Math.sqrt(x * x + y * y);
    }

    boolean esPar(int n) {
        if (n%2 == 0) {
            return true;
        }
        else{
            return false;
        }
    }

    boolean esBisiesto(int n) {
        if (n%400 == 0) {
            return true;
        }
        else if (n%100 == 0) {
            return false;
        }
        else if (n%4 == 0){
            return true;
        }
        else{
            return false;
        }
    }

    int factorialIterativo(int n) {
        int res = 1;
        if (n == 0){
            return 1;
        }
        for (int m = n; m > 0; m--){
            res *= m;
        }
        return res;
    }

    int factorialRecursivo(int n) {
        int res = n;
        if (n == 0 || n == 1){
            return 1;
        }
        res *= factorialRecursivo(n - 1);
        return res;
        
        }

        
    


    boolean esPrimo(int n) {
        int res = 0;
        for (int divisor = n - 1; divisor > 0; divisor--){
            if (n%divisor == 0){
                res += 1;
            }
            
            }
        if (res == 1){
            return true;
        }
        return false;
        }
        
    

    int sumatoria(int[] numeros) {
        int res = 0;
        for (int i = 0; i < numeros.length; i++){
            res += numeros[i];

        }
        return res;
    }

    int busqueda(int[] numeros, int buscado) {
        int res = 0;
        for (int i = 0; i < numeros.length; i++){
            if (numeros[i] == buscado){
                res = i;
            }
        }
        return res;
    }

    boolean tienePrimo(int[] numeros) {
        for (int i = 0; i < numeros.length;i++){
            if (esPrimo(numeros[i])){
                return true;
            }
        }
        return false;
    }

    boolean todosPares(int[] numeros) {
         for (int i = 0; i < numeros.length;i++){
            if (! esPar(numeros[i])){
                return false;
            }
        }
        return true;
    }

    boolean esPrefijo(String s1, String s2) {
        if (s1.length() > s2.length()){
                return false;
            }
        for (int i = 0; i < s1.length(); i++){
            
            if (s1.charAt(i) != s2.charAt(i)){
                return false;
            }
        }
        return true;
    }

    boolean esSufijo(String s1, String s2) {
       if (s1.length() > s2.length()){
                return false;
            }
        for (int i = 0; i < s1.length(); i++){
            if (s1.charAt(s1.length() - 1 - i) != s2.charAt(s2.length() -i -1)){
                return false;
            }
        }
        
        return true;
    }
    

/***  Segunda parte: Debugging ***/

    boolean xor(boolean a, boolean b) {
        return (a || b) && !(a && b);
    }

    boolean iguales(int[] xs, int[] ys) {
        boolean res = true;
        if (xs.length != ys.length){
            return false;
        }
        for (int i = 0; i < xs.length; i++) {
            if (xs[i] != ys[i]) {
                res = false;
            }
        }
        return res;
    }

    boolean ordenado(int[] xs) {
        boolean res = true;
        for (int i = 0; i < xs.length - 1; i++) {
            if (xs[i] > xs [i+1]) {
                res = false;
            }
        }
        return res;
    }

    int maximo(int[] xs) {
        int res = xs[0];
        for (int i = 1; i < xs.length; i++) {
            if (xs[i] > res){
                res = xs[i];
            } 
        }
        return res;
    }

    boolean todosPositivos(int[] xs) {
        boolean res = true;
        for (int x : xs) {
            if (x <= 0) {
                res = false;
            }
        }
        return res;
    }

}
