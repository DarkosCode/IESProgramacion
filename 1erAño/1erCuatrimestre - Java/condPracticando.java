import java.util.Scanner;
import javax.swing.JOptionPane; // clase que tiene los metodos para mostrar ventanas

public class condPracticando {

    public static void main(String[] a) {
        Scanner teclado = new Scanner(System.in);

        // ! Ciclo de repeticion for
        // ? Tomar 10 numeros y mostrarlos
        // for (int i = 1; i <= 100; i++) {
        // System.out.println("El numero es: " + i);

        // ? Verificar esos 10 numeros y mostrar los pares
        // if (i % 2 == 0) {
        // System.out.println("El numero es: " + i);
        // }

        // }

        // ? Ingresar 10 caracteres y mostrarlos, decir letra por letra si es o no vocal
        System.out.println("Ingresa caracteres para verificar si son o no vocales: ");
        String caracter = teclado.nextLine().toLowerCase();
        int vocales = 0;
        int consonantes = 0;
        int cantidad;
        for (cantidad = 0; cantidad < caracter.length(); cantidad++) {
            if (caracter.charAt(cantidad) == 'a' || caracter.charAt(cantidad) == 'e' || caracter.charAt(cantidad) == 'i'
                    || caracter.charAt(cantidad) == 'o' || caracter.charAt(cantidad) == 'u') {
                System.out.println("El caracter: " + caracter.charAt(cantidad) + " SI es una vocal");
                vocales++;
            } else {
                System.out.println("El caracter: " + caracter.charAt(cantidad) + " NO es una vocal");
                consonantes++;
            }
        }

        // System.out.println(
        // "De los " + cantidad + " caracteres ingresados, hay " + vocales + " Vocales y
        // "
        // + consonantes
        // + " que NO son Vocales");

        JOptionPane.showMessageDialog(
                null, // Componente para determinar la posicion del cuadro
                "De los " + cantidad + " caracteres ingresados, hay " + vocales + " Vocales y "
                        + consonantes + " que NO son Vocales", // Argumento de que mensaje mostrar
                "Resultado del análisis", // Titulo del cuadro de mensaje a mostrar
                JOptionPane.INFORMATION_MESSAGE); // Tipo de icono en el cuadro de mensaje

    }
}
