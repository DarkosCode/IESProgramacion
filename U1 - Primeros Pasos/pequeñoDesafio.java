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
                "Memoria RAM" };

        String pistas[] = {
                "Almacena datos de la computadora, a gran velocidad",
                "El lugar donde se conecta todo",
                "Al que le gusta jugar o editar, tiene que tener una buena",
                "El cerebro de la computadora",
                "Generalmente se compra por sus GB, y su frecuencia" };

        int eleccionAleatoria = (int) (Math.random() * componentesDePC.length);

    }
}