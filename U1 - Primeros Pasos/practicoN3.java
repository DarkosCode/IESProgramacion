import java.util.Scanner;
import java.text.DecimalFormat;

public class practicoN3 {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("#.#####");

        // ? Ej 1 - Potencia de un numero
        // System.out.println("Ingresar un numero base: ");
        // int base = teclado.nextInt();
        // System.out.println("Ingresar un numero exponente: ");
        // int exponente = teclado.nextInt();

        // double resultado = Math.pow(base, exponente);
        // System.out.println(base + " potenciado a la " + exponente + " es " + (int)
        // resultado);

        // ? Ej 2 - Valor absoluto de un numero
        // System.out.println("Ingresar un numero: ");
        // int valorConSigno = teclado.nextInt();
        // double valorAbsoluto = Math.abs(valorConSigno);
        // System.out.println("El valor absoluto de " + valorConSigno + " es " + (int)
        // valorAbsoluto);

        // ? Ej 3 - Cálculo de distancia entre dos puntos
        // * Distancia = raiz(x2−x1)² + (y2−y1)²

        // System.out.println("Ingresar la primer coordenada de un punto: ");
        // double x1erPunto = teclado.nextDouble();
        // System.out.println("Ingresar la segunda coordenada de un punto: ");
        // double y1erPunto = teclado.nextDouble();
        // System.out.println("Ingresar la primer coordenada del segundo punto: ");
        // double x2doPunto = teclado.nextDouble();
        // System.out.println("Ingresar la segunda coordenada del segundo punto: ");
        // double y2doPunto = teclado.nextDouble();

        // // double potencia1 = Math.pow((x1erPunto - x2doPunto), 2);

        // double distancia = Math.sqrt(Math.pow((x1erPunto - x2doPunto), 2) +
        // Math.pow((x2doPunto - y2doPunto), 2));
        // System.out.println("La distancia entre el punto " + "(" + x1erPunto + ", " +
        // y1erPunto + ") y el punto " + "("
        // + x2doPunto + ", " + y2doPunto + ") es: " + distancia);

        // ? Ej 4 - Ecuacion de segundo grado
        // * x=2a−b±b2−4ac​

        System.out.println("Ingresar el coeficiente a: ");
        double a = teclado.nextDouble();
        System.out.println("Ingresar el coeficiente b: ");
        double b = teclado.nextDouble();
        System.out.println("Ingresar el coeficiente c: ");
        double c = teclado.nextDouble();

        double divisor = 2 * a;
        double raiz = Math.sqrt((Math.pow(b, 2)) - (4 * a * c));

        double raicesPositivas = (-b + raiz) / divisor;
        double raicesNegativas = (-b - raiz) / divisor;

        if (raiz >= 0) {
            System.out.println("El primer resultado (+) es: " + df.format(raicesPositivas)
                    + ". Y el segundo resultado (-) es: " + df.format(raicesNegativas));
        } else {
            System.out.println("La raiz con los cocientes es inexistente debido a que es negativa");
        }

        // ? Ej 5 -

    }

}