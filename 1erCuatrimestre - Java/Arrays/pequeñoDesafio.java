import java.util.Scanner;

public class pequeñoDesafio {
    public static void main(String[] args) {
        // ? Programa desafío. "Adivina la palabra"
        // Crear dos vectores de string uno con las pistas y uno con las respuestas.
        // Cuando el usuario quiera jugar el programa le muestra una pista aleatoria
        // (elegir una posición aleatoria), el usuario ingresa la respuesta. El programa
        // le avisa si acertó o no en la respuesta.

        Scanner teclado = new Scanner(System.in);

        String componentesDePC[] = {
                "Disco Solido",
                "MotherBoard",
                "GPU",
                "Procesador",
                "Memoria RAM",
                "Gabinete" };

        String pistas[] = {
                "Almacena datos de la computadora, a gran velocidad.",
                "El lugar donde se conecta todo.",
                "Al que le gusta jugar o editar, tiene que tener una buena...",
                "El cerebro de la computadora.",
                "Generalmente se compra por sus GB, y su frecuencia.",
                "Simplemente donde se guardan todas las partes." };

        System.out.println("Bienvenido al juego de las adivinanzas!, hoy con tematica: PCs");
        System.out.println("Recuerda que solo tienes 3 intentos por pieza, y que no importa mayusculas o minusculas.");
        System.out.println("Tienes " + componentesDePC.length
                + " piezas por adivinar. ¿Cual quieres intentar jugar? (Recuerda introducir un numero)");
        int eleccionNumerica = teclado.nextInt();
        teclado.nextLine();

        if (eleccionNumerica > 0 && eleccionNumerica <= componentesDePC.length) {
            String pistaElegida = pistas[eleccionNumerica - 1];

            System.out.println("Bien, elegiste la pieza numero " + eleccionNumerica);
            System.out.println("La pista para que intentes adivinar esa pieza es: " + pistaElegida);
            System.out.println("Que componente de Computadora crees que es?");

            for (int contadorIntentos = 0; contadorIntentos < 3; contadorIntentos++) {
                String eleccionDePieza = teclado.nextLine();

                if (eleccionDePieza.trim().toLowerCase()
                        .equals(componentesDePC[eleccionNumerica - 1].trim().toLowerCase())) {
                    System.out.println("Ganaste!, acertaste la pieza");
                    break;
                } else {
                    System.out.println(
                            "Incorrecto!, No es esa la pieza, o la escribiste mal. Intenta nuevamente, te queda "
                                    + (3 - (contadorIntentos + 1)) + " intentos.");
                }
            }

        } else {
            System.out.println("No existe esa posicion! Intenta jugar de nuevo.");
        }

    }
}