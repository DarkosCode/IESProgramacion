
// ! Siempre es buena practica importar las clases con sus metodos al principio del codigo
// Sin sintaxis, simplemente lenguaje coloquial-instrucciones
public class Ejercicios {
    public static void main(String[] args) {
        // ! EjercicioParImpar
        /*
         * Scanner teclado = new Scanner(System.in);
         * System.out.println("Ingrese un numero");
         * int num = teclado.nextInt();
         * // if (num % 2 == 0)
         * // System.out.println("El numero es PAR");
         * // else
         * // System.out.println("El numero es IMPAR");
         * // * ↑ Debido a que el if solo esta usando una condicion, una sola linea
         * // * (System.out)
         * // * no hace falta abrir llaves en el if, si fueran mas (un bloque); si.
         * 
         * String esParOImpar = num % 2 == 0 ? "El numero es par" :
         * "El numero es Impar";
         * System.out.println(esParOImpar);
         */

        // ! Ejercicio de notas alumnos
        // Scanner teclado = new Scanner(System.in);
        // System.out.println("Ingrese el nombre del alumno");
        // String NombreIngresado = teclado.nextLine();
        // System.out.println("Ingrese la nota del alumno");
        // int Nota = teclado.nextInt();

        // if (Nota >= 0 && Nota <= 10) {
        // if (Nota >= 6)
        // System.out.println("El alumno " + NombreIngresado + " SI esta aprobado");
        // else
        // System.out.println("El alumno " + NombreIngresado + " NO esta aprobado");
        // } else {
        // System.out.println("No es una nota valida entre 1 y 10");
        // }

        // ! Año bisiesto
        int año = 2008;
        if ((año % 4 == 0 && año % 100 != 0) || (año % 400 == 00)) {
            System.out.println("Es bisiesto");
        } else {
            System.out.println("NO es un año bisiesto");
        }

    }
}