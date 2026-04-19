
import java.util.Arrays;

public class priPruebas {
    public static void main(String[] a) {

        // ? Crear un vector de 5 posiciones de numeros aleatorios
        // ? y luego ordenarlo de mayor a menor

        int arrayDeNumeros[] = new int[5];

        for (int i1 = 0; i1 < arrayDeNumeros.length; i1++) {
            arrayDeNumeros[i1] = (int) (Math.random() * 10) + 1;
        }
        System.out.println("Array de numeros: " + Arrays.toString(arrayDeNumeros));

        boolean hayCambios = true;

        // ! De MENOR a MAYOR
        for (int indExt = 0; indExt < arrayDeNumeros.length - 1 && hayCambios; indExt++) {
            hayCambios = false;

            for (int indInt = 0; indInt < arrayDeNumeros.length - indExt - 1; indInt++) {
                if (arrayDeNumeros[indInt] > arrayDeNumeros[indInt + 1]) {
                    int temporal = arrayDeNumeros[indInt];
                    arrayDeNumeros[indInt] = arrayDeNumeros[indInt + 1];
                    arrayDeNumeros[indInt + 1] = temporal;

                    hayCambios = true;
                    // * Este booleano si hay un cambio, va a hacer que la variable booleana de
                    // * afuera se vuelva a poner en true, despues de ponerse en false en el for
                    // * exterior. Si no hay cambios en el for interno, el for externo va a hacer
                    // * que la variable booleana sea False, entonces no va a volverse a ejecutar el
                    // * for.

                }
            }
        }

        System.out.println("Array ordenado de menor a mayor: " +
                Arrays.toString(arrayDeNumeros));

        // ! De MAYOR A MENOR
        // for (int indExt = 0; indExt < arrayDeNumeros.length - 1; indExt++) {

        // for (int indInt = 0; indInt < arrayDeNumeros.length - indExt - 1; indInt++) {

        // if (arrayDeNumeros[indInt] < arrayDeNumeros[indInt + 1]) {
        // int temporal = arrayDeNumeros[indInt];
        // arrayDeNumeros[indInt] = arrayDeNumeros[indInt + 1];
        // arrayDeNumeros[indInt + 1] = temporal;

        // hayCambios = true;
        // // * Este booleano si hay un cambio, va a hacer que la variable booleana de
        // // * afuera que es false, cambie a true por cada pasada en la que
        // efectivamente
        // // * haya un cambio. Si no, sale del if sin cambios y el boolean se queda en
        // // * false.
        // }
        // }
        // }

    }
}