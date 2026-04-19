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
        // System.out.println("Introduce el primer numero a comparar: ");
        // int numero1 = entradaTeclado.nextInt();
        // System.out.println("Introduce el segundo numero a comparar: ");
        // int numero2 = entradaTeclado.nextInt();
        // System.out.println("Introduce el tercer numero a comparar: ");
        // int numero3 = entradaTeclado.nextInt();

        // if (numero1 >= numero3 && numero2 >= numero3) {
        // if (numero1 >= numero2) {
        // System.out.println(numero1 + " " + numero2 + " " + numero3);
        // } else {
        // System.out.println(numero2 + " " + numero1 + " " + numero3);
        // }
        // } else if (numero1 >= numero2 && numero3 >= numero2) {
        // if (numero1 >= numero3) {
        // System.out.println(numero1 + " " + numero3 + " " + numero2);
        // } else {
        // System.out.println(numero3 + " " + numero1 + " " + numero2);
        // }
        // } else if (numero2 >= numero1 && numero3 >= numero1) {
        // if (numero2 >= numero3) {
        // System.out.println(numero2 + " " + numero3 + " " + numero1);
        // } else {
        // System.out.println(numero3 + " " + numero2 + " " + numero1);
        // }
        // }

        // ? Pedir un número entre 0 y 9.999 y decir cuantas cifras tiene, sin String
        // System.out.println("Introduce un numero entre 0 y 9999999999 para contar sus
        // cifras: ");
        // // maximo 10 cifras que es lo que soporta int
        // int numero = entradaTeclado.nextInt();
        // int copiaParaContar = numero;
        // int contador = 0;

        // if (numero == 0) {
        // System.out.println("El numero " + numero + " tiene " + contador + " cifras");
        // } else if (numero > 0) {
        // while (copiaParaContar != 0) {
        // contador++;
        // copiaParaContar /= 10;
        // }
        // System.out.println("El numero " + numero + " tiene " + contador + " cifras");
        // }

        /*
         * metodo de contar las cifras con string
         * int numero = 12345;
         * String numeroStr = String.valueOf(numero);
         * int cantidadCifras = numeroStr.length();
         * System.out.println("El número " + numero + " tiene " + cantidadCifras +
         * " cifras.");
         */

        // ? Pedir un número entre 0 y 9.999 y mostrarlo con las cifras al revés.
        System.out.println("Introduce un numero entre 0 y 99999 para mostrarlo al reves: ");
        int numeroOriginal = entradaTeclado.nextInt();
        if (numeroOriginal <= 99999) {
            int numero = numeroOriginal;
            int numeroRevertido = 0;

            while (numero > 0) {
                // Obtener la última cifra del número
                int ultimaCifra = numero % 10;
                // 245 -> 24.5 -> el resto es 5
                // 24 -> resto 4
                // 2 -> resto 2

                // Agregar la última cifra al número revertido, multiplicándolo por 10 para
                // "desplazar" las cifras anteriores
                numeroRevertido = numeroRevertido * 10 + ultimaCifra;
                // 0 * 10 + 5 = 5
                // 5 * 10 + 4 = 54
                // 54 * 10 + 2 = 542

                // Eliminar la última cifra del número original dividiéndolo por 10
                numero /= 10;
                // 245 /10 = 24
                // 24 /10 = 2
                // 2 /10 = 0 -> se corta el while
            }

            System.out.println("El número original es: " + numeroOriginal);
            System.out.println("El número invertido es: " + numeroRevertido);
        } else {
            System.out.println("El numero no esta entre 0 y 99999");
        }

        // ? Pedir el día, mes y año de una fecha correcta y mostrar la fecha del día
        // ? siguiente. suponer que todos los meses tienen 30 días
        // System.out.println("Introduce el año");
        // int año = entradaTeclado.nextInt();

        // System.out.println("Introduce el numero de mes");
        // int mes = entradaTeclado.nextInt();

        // System.out.println("Introduce el numero de dia");
        // int dia = entradaTeclado.nextInt();

        // if (dia <= 29) {
        // int siguiente = dia + 1;
        // System.out.println("La fecha del dia siguiente al indicado es; el dia " +
        // siguiente + " del mes " + mes
        // + " del año " + año);
        // } else if (dia == 30) {
        // if (mes != 12) {
        // dia = 1;
        // mes = mes + 1;
        // System.out.println("La fecha del dia siguiente al indicado es; el dia " + dia
        // + " del mes " + mes
        // + " del año " + año);

        // } else if (mes == 12) {
        // dia = 1;
        // mes = 1;
        // año = año + 1;
        // System.out.println("La fecha del dia siguiente al indicado es; el dia " + dia
        // + " del mes " + mes
        // + " del año " + año);
        // }
        // } else if (dia >= 31) {
        // System.out.println("No existen fechas con meses mayores a 30 dias");
        // }

    }

}
