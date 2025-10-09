import javax.swing.JOptionPane;

public class PiePapTijera {
    public static void main(String[] a) {

        // ? PIEDRA PAPEL O TIJERA

        // System.out.println(numeroComputadora);
        // System.out.println(eleccionComputadora);
        // System.out.println(eleccionUsuario);

        int winsComputadora = 0;
        int winsUsuario = 0;
        int empates = 0;

        while (winsComputadora < 3 && winsUsuario < 3) {
            // Se va a frenar el codigo cuando uno llegue a 3 victorias.

            // ! parte de eleccion del usuario
            String eleccionUsuario = JOptionPane.showInputDialog(null, "Ingrese piedra papel o tijera:",
                    "Piedra, Papel o Tijera", JOptionPane.QUESTION_MESSAGE);
            if (eleccionUsuario == null) {
                JOptionPane.showMessageDialog(null, "Juego cancelado");
                return;
            }
            if (eleccionUsuario.toLowerCase().equals("piedra") ||
                    eleccionUsuario.toLowerCase().equals("papel") ||
                    eleccionUsuario.toLowerCase().equals("tijera")) {

                // ! parte de eleccion de la computadora
                String eleccionComputadora = null;
                int numeroComputadora = (int) (Math.random() * 3) + 1;

                if (numeroComputadora == 1) {
                    eleccionComputadora = "piedra";
                } else if (numeroComputadora == 2) {
                    eleccionComputadora = "papel";
                } else if (numeroComputadora == 3) {
                    eleccionComputadora = "tijera";
                }

                JOptionPane.showMessageDialog(null,
                        "El usuario eligió: " + eleccionUsuario.toUpperCase() +
                                "\nLa computadora eligió: " + eleccionComputadora.toUpperCase(),
                        "ELECCIONES", JOptionPane.INFORMATION_MESSAGE);

                if (eleccionComputadora.equals(eleccionUsuario.toLowerCase())) {
                    JOptionPane.showMessageDialog(null, "¡Empate!");
                    empates++;
                } else if ((eleccionComputadora.equals("piedra") && eleccionUsuario.toLowerCase().equals("tijera"))
                        || (eleccionComputadora.equals("papel") && eleccionUsuario.toLowerCase().equals("piedra"))
                        || (eleccionComputadora.equals("tijera") && eleccionUsuario.toLowerCase().equals("papel"))) {
                    winsComputadora++;
                    JOptionPane.showMessageDialog(null, "Victoria para la computadora!");
                    JOptionPane.showMessageDialog(null,
                            "Usuario: " + winsUsuario + "\nComputadora: " + winsComputadora, "MARCADOR",
                            JOptionPane.INFORMATION_MESSAGE);
                } else if ((eleccionComputadora.equals("piedra") && eleccionUsuario.toLowerCase().equals("papel"))
                        || (eleccionComputadora.equals("papel") && eleccionUsuario.toLowerCase().equals("tijera"))
                        || (eleccionComputadora.equals("tijera") && eleccionUsuario.toLowerCase().equals("piedra"))) {
                    winsUsuario++;
                    JOptionPane.showMessageDialog(null, "Victoria para el usuario!");
                    JOptionPane.showMessageDialog(null,
                            ("Usuario: " + winsUsuario + "\nComputadora: " + winsComputadora),
                            "MARCADOR", JOptionPane.INFORMATION_MESSAGE);
                }
            } else {
                JOptionPane.showMessageDialog(null,
                        "El valor ingresado es incorrecto, debe ser piedra, papel o tijera");
            }

        }
        JOptionPane.showMessageDialog(null,
                "Termino la partida! Hubieron " + empates + " empates. El usuario consiguio "
                        + winsUsuario + " victorias y la computadora consiguio " + winsComputadora + " victorias",
                "RESULTADO DE LA PARTIDA:", JOptionPane.INFORMATION_MESSAGE);

    }
}