import java.util.Scanner;

public class practicoN1 {
    // cambiar nombre de archivo
    public static void main(String[] a) {
        Scanner entradaTeclado = new Scanner(System.in);

        // ? Pedir el radio de un círculo y calcular su área. A=PI*r^2.
        // System.out.println("Introduce el radio del circulo: ");
        // double radioDeCirculo = entradaTeclado.nextDouble();
        // double calculadorDeArea = Math.PI * (radioDeCirculo * radioDeCirculo);
        // System.out.println("El radio del circulo es: " + calculadorDeArea);

        // ? Pedir un número e indicar si es positivo o negativo.
        // System.out.println("Introduce el numero para verificar su signo: ");
        // int numero = entradaTeclado.nextInt();
        // if (numero < 0) {
        // System.out.println("El numero " + numero + " es negativo");
        // } else if (numero > 0) {
        // System.out.println("El numero " + numero + " es positivo");
        // } else {
        // System.out.println("El numero " + numero + " es de valor neutro");
        // }

        // ? Pedir dos números y decir cual es el mayor o si son iguales.
        // System.out.println("Introduce el primer numero a comparar: ");
        // int numero1 = entradaTeclado.nextInt();
        // System.out.println("Introduce el segundo numero a comparar: ");
        // int numero2 = entradaTeclado.nextInt();

        // if (numero1 == numero2) {
        // System.out.println("Los numeros " + numero1 + " y " + numero2 + " son
        // iguales");
        // } else if (numero1 > numero2) {
        // System.out.println("El numero " + numero1 + " es mayor que " + numero2);
        // } else {
        // System.out.println("El numero " + numero2 + " es mayor que " + numero1);
        // }

        // ? Pedir tres números y mostrarlos ordenados de mayor a menor.
        System.out.println("Introduce el primer numero a comparar: ");
        int numero1 = entradaTeclado.nextInt();
        System.out.println("Introduce el segundo numero a comparar: ");
        int numero2 = entradaTeclado.nextInt();
        System.out.println("Introduce el tercer numero a comparar: ");
        int numero3 = entradaTeclado.nextInt();

        if (numero1 >= numero3 && numero2 >= numero3) {
            if (numero1 >= numero2) {
                System.out.println(numero1 + " " + numero2 + " " + numero3);
            } else {
                System.out.println(numero2 + " " + numero1 + " " + numero3);
            }
        } else if (numero1 >= numero2 && numero3 >= numero2) {
            if (numero1 >= numero3) {
                System.out.println(numero1 + " " + numero3 + " " + numero2);
            } else {
                System.out.println(numero3 + " " + numero1 + " " + numero2);
            }
        } else if (numero2 >= numero1 && numero3 >= numero1) {
            if (numero2 >= numero3) {
                System.out.println(numero2 + " " + numero3 + " " + numero1);
            } else {
                System.out.println(numero3 + " " + numero2 + " " + numero1);
            }
        }
        // else if (numero1 == numero2 || numero1 == numero3 || numero2 == numero3) {}

    }

}
