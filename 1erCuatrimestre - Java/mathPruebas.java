import java.util.Scanner;

public class mathPruebas {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        // ? 1er Ejercicio; ingresar n° y mostrar raiz cuadrada
        // System.out.println("Ingrese un numero para calcular su raiz cuadrada: ");
        // double numeritoIngresado = entrada.nextDouble();
        // double raiz = Math.sqrt(numeritoIngresado);
        // System.out.println("La raiz cuadrada del numero " + (int) numeritoIngresado +
        // " es " + raiz);

        // ? 2do Ejercicio; potencia
        // System.out.println("Ingrese el numero al que quiere potenciar: ");
        // double numeritoAPotenciar = entrada.nextDouble();
        // System.out.println("Ingrese la potencia: ");
        // double numPotenciador = entrada.nextDouble();
        // double potencia = Math.pow(numeritoAPotenciar, numPotenciador);
        // System.out
        // .println("El numero ingresado " + (int) numeritoAPotenciar + " potenciado a "
        // + (int) numPotenciador
        // + " es igual a " + potencia);
        // Esto como estoy usando el int para castear, si es decimal alguno de los
        // numeros no me lo va a mostrar

        // ! Este funciona igual con la potencia pero verifica y solo funciona si el
        // ! potenciador es mayor a 1
        // if (numPotenciador >= 1) {
        // double potencia = Math.pow(numeritoAPotenciar, numPotenciador);
        // System.out
        // .println("El numero ingresado " + (int) numeritoAPotenciar + " potenciado a "
        // + (int) numPotenciador
        // + " es igual a " + (int) potencia);
        // // los (int) son casts para que los numeros se impriman sin decimales en la
        // // consola (dado que en este ejercicio no necesito que se impriman con
        // // decimales)

        // } else {
        // System.out.println("El numero de la potencia es menor a 1");
        // }

        // ? Ejercicio de ecuacion rara
        System.out.println("Ingresa un valor para a");
        double a = entrada.nextDouble();
        System.out.println("Ingresa un valor para b");
        double b = entrada.nextDouble();
        System.out.println("Ingresa un valor para c");
        double c = entrada.nextDouble();

        // modularizando sqrt
        double sqrt = Math.sqrt(Math.pow(b, 2) - (4 * a * c));

        if (sqrt > 0) {
            double x = (-b + (Math.sqrt(Math.pow(b, 2) - (4 * a * c)))) / (2 * a);
            System.out.println(x);
            System.out.println("Dadas las variables a = " + a + ", b = " + b + " y c = "
                    + c
                    + " , encontramos que el valor de X = " + x);
        } else {
            System.out.println(
                    "Los numeros ingresados dan como resultado una raiz menor a 0, no se puede ejecutar el metodo");
        }
    }
}