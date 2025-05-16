import java.util.Scanner;

public class practicoN2 {
    public static void main(String[] arg) {
        Scanner teclado = new Scanner(System.in);

        // ? Correr estos programas, ver y mostrar que hacen
        // !
        // for (int i = 2; i <= 50; i++) {
        // boolean esPrimo = true;
        // // System.out.println(i);
        // for (int j = 2; j <= i / 2; j++) {
        // // System.out.println(j);
        // if (i % j == 0) {
        // esPrimo = false;
        // break;
        // }
        // }
        // if (esPrimo) {
        // System.out.println(i + " es primo");
        // }
        // }

        // !
        // int suma = 0;

        // for (int i = 1; i <= 100; i++) {
        // if (i % 3 == 0 || i % 5 == 0) {
        // suma += i;
        // }
        // }
        // System.out.println("La suma de los multiplos de 3 y 5 es: " + suma);

        // ? Ejercicios de aplicacion

        // ! Tabla de Multiplicar de un Número
        // System.out.println("Ingresar el numero a multiplicar: ");
        // int numeroIngresado = teclado.nextInt();
        // int i = 1;
        // while (i <= 10) {
        // System.out.println(numeroIngresado + " por " + i + " es " + (numeroIngresado
        // * i));
        // i++;
        // }

        // ! Tabla de Potencias de un Número
        // System.out.println("Ingresar el numero a potenciar: ");
        // double numeroIngresado = teclado.nextInt();
        // for (int i = 1; i < 10; i++) {
        // System.out.println((int) numeroIngresado + " a la " + (int) i + " es " +
        // (Math.pow(numeroIngresado, i)));
        // }

        // ! Tabla de numeros Pares de forma Creciente
        // System.out.println("Los numeros pares de forma Creciente↗ del 0 al 200 son:
        // ");
        // for (int i = 0; i <= 200; i++) {
        // if (i % 2 == 0) {
        // System.out.print(" / " + i);
        // }
        // }
        // System.out.println(" ");

        // ! Tabla de numeros Pares de forma Decreciente
        // System.out.println("Los numeros pares de forma Decreciente↘ del 200 al 0 son:
        // ");
        // for (int i = 200; i >= 0; i--) {
        // if (i % 2 == 0) {
        // System.out.print(" / " + i);
        // }
        // }

        // ! Imprimir números pares hasta un número dado
        // System.out.println("Introducir DESDE que numero se quieren obtener numeros
        // pares ");
        // int inicioDePares = teclado.nextInt();
        // System.out.println("Introducir HASTA que numero se quieren obtener numeros
        // pares ");
        // int limiteDePares = teclado.nextInt();
        // System.out.println("La lista de numeros pares desde " + inicioDePares + "
        // hasta el " + limiteDePares + " es: ");

        // for (; inicioDePares <= limiteDePares; inicioDePares++) {
        // if (inicioDePares % 2 == 0) {
        // System.out.print(" / " + inicioDePares);
        // }
        // }

        // ! Imprimir números primos hasta un número dado
        System.out.println("Introducir DESDE que numero se quieren obtener numeros primos ");
        int inicioDePrimos = teclado.nextInt();
        System.out.println("Introducir HASTA que numero se quieren obtener numeros pares ");
        int limiteDePrimos = teclado.nextInt();
        System.out.println(
                "La lista de numeros primos desde " + inicioDePrimos + " hasta el " + limiteDePrimos + " es: ");

        for (int i = inicioDePrimos; i <= limiteDePrimos; i++) {
            boolean esPrimo = true;
            if (i <= 1) {
                esPrimo = false;
            } else {
                for (int j = 2; j <= Math.sqrt(i); j++) { // Mejor optimización: hasta la raíz cuadrada
                    if (i % j == 0) {
                        esPrimo = false;
                        break;
                    }
                }
            }
            if (esPrimo) {
                System.out.print(i + " ");
            }

        }

    }
}
