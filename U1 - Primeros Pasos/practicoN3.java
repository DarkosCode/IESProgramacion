import java.util.Scanner;

public class practicoN3 {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        // ? Ej 1 - Potencia de un numero
        // System.out.println("Ingresar un numero base: ");
        // int base = teclado.nextInt();
        // System.out.println("Ingresar un numero exponente: ");
        // int exponente = teclado.nextInt();

        // double resultado = Math.pow(base, exponente);
        // System.out.println(base + " potenciado a la " + exponente + " es " + (int)
        // resultado);

        // ? Ej 2 - Valor absoluto de un numero
        System.out.println("Ingresar un numero: ");
        int valorConSigno = teclado.nextInt();
        double valorAbsoluto = Math.abs(valorConSigno);
        System.out.println("El valor absoluto de " + valorConSigno + " es " + (int) valorAbsoluto);

    }

}