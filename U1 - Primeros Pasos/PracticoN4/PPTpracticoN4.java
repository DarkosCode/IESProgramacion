import java.util.Scanner;

public class PPTpracticoN4 {
    public static void main(String[] a) {
        Scanner teclado = new Scanner(System.in);

        // ? PIEDRA PAPEL O TIJERA

        // System.out.println(numeroComputadora);
        // System.out.println(eleccionComputadora);
        // System.out.println(eleccionUsuario);

        int winsComputadora = 0;
        int winsUsuario = 0;
        int empates = 0;

        while ((winsComputadora <= 3) || (winsUsuario <= 3)) {

            // ! parte de eleccion del usuario
            System.out.println("Ingrese piedra papel o tijera: ");
            String eleccionUsuario = teclado.nextLine();

            // ! parte de eleccion de la computadora
            String eleccionComputadora = null;
            int numeroComputadora = (int) (Math.random() * 3) + 1;
            System.out.println(numeroComputadora);

            if (numeroComputadora == 1) {
                eleccionComputadora = "piedra";
            } else if (numeroComputadora == 2) {
                eleccionComputadora = "papel";
            } else if (numeroComputadora == 3) {
                eleccionComputadora = "tijera";
            }

            if (eleccionUsuario.toLowerCase().equals("piedra") || eleccionUsuario.toLowerCase().equals("papel")
                    || eleccionUsuario.toLowerCase().equals("tijera")) {
                if (eleccionComputadora.equals(eleccionUsuario.toLowerCase())) {
                    System.out.println("Empate!");
                    empates++;
                    System.out.println("Usuario: " + winsUsuario + " Computadora: " + winsComputadora);
                } else if (eleccionComputadora.equals("piedra") && eleccionUsuario.toLowerCase().equals("tijera")) {
                    winsComputadora++;
                    System.out.println("El usuario eligio " + eleccionUsuario + " y la computadora "
                            + eleccionComputadora + ". Victoria para la computadora!");
                    System.out.println("Usuario: " + winsUsuario + " Computadora: " + winsComputadora);
                } else if (eleccionComputadora.equals("piedra") && eleccionUsuario.toLowerCase().equals("papel")) {
                    winsUsuario++;
                    System.out.println("El usuario eligio " + eleccionUsuario + " y la computadora "
                            + eleccionComputadora + ". Victoria para el usuario!");
                    System.out.println("Usuario: " + winsUsuario + " Computadora: " + winsComputadora);
                } else if (eleccionComputadora.equals("papel") && eleccionUsuario.toLowerCase().equals("piedra")) {
                    winsComputadora++;
                    System.out.println("El usuario eligio " + eleccionUsuario + " y la computadora "
                            + eleccionComputadora + ". Victoria para la computadora!");
                    System.out.println("Usuario: " + winsUsuario + " Computadora: " + winsComputadora);
                } else if (eleccionComputadora.equals("papel") && eleccionUsuario.toLowerCase().equals("tijera")) {
                    winsUsuario++;
                    System.out.println("El usuario eligio " + eleccionUsuario + " y la  computadora "
                            + eleccionComputadora + ". Victoria para el usuario!");
                    System.out.println("Usuario: " + winsUsuario + " Computadora: " + winsComputadora);
                } else {
                    System.out.println("Algo ingresado esta mal");
                }
            } else {
                System.out.println("El valor ingresado es incorrecto, debe ser piedra, papel o tijera");
                break;
            }
        }

        System.out.println("Termino la partida! Hubieron " + empates + " empates. El usuario consiguio " + winsUsuario
                + " victorias y la computadora consiguio " + winsComputadora);
    }
}