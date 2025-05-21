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

        // System.out.println("Ingresar el coeficiente a: ");
        // double a = teclado.nextDouble();
        // System.out.println("Ingresar el coeficiente b: ");
        // double b = teclado.nextDouble();
        // System.out.println("Ingresar el coeficiente c: ");
        // double c = teclado.nextDouble();

        // double divisor = 2 * a;
        // double raiz = Math.sqrt((Math.pow(b, 2)) - (4 * a * c));

        // double raicesPositivas = (-b + raiz) / divisor;
        // double raicesNegativas = (-b - raiz) / divisor;

        // if (raiz >= 0) {
        // System.out.println("El primer resultado (+) es: " +
        // df.format(raicesPositivas)
        // + ". Y el segundo resultado (-) es: " + df.format(raicesNegativas));
        // } else {
        // System.out.println("La raiz con los cocientes es inexistente debido a que es
        // negativa");
        // }

        // ? Ej 5 - Simulacion de Dados
        /// * Simulá el lanzamiento de dos dados utilizando Math.random(), y mostrá el
        // resultado de ambos lanzamientos y su suma. Simulá 1000 lanzamientos y contá
        // cuántas veces se obtiene cada posible suma (entre 2 y 12).

        // int dado1;
        // int dado2;
        // int rango = (12 - 2) + 1;
        // int i;

        // for (i = 0; i < 20; i++) {
        // dado1 = (int) (Math.random() * rango) + 2;
        // dado2 = (int) (Math.random() * rango) + 2;
        // System.out.println("Los dados tirados dieron " + dado1 + " y " + dado2);
        // }

        // System.out.println("Los dados se tiraron " + i + " veces.");
        // System.out.println(Math.random());

        // ? Ej 6 - Hipotenusa de un triangulo
        // * */ a² + b² = c²
        System.out.println("Ingresar el primer cateto (a): ");
        double cateto1 = teclado.nextDouble();
        System.out.println("Ingresar el segundo cateto (b): ");
        double cateto2 = teclado.nextDouble();
        double pitagoras = Math.pow(cateto1, 2) + Math.pow(cateto2, 2);
        double Hipotenusa = Math.sqrt(pitagoras);
        System.out.println("La hipotenusa del triangulo rectangulo es: " + Hipotenusa);
    }

}