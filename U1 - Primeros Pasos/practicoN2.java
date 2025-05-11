public class practicoN2 {
    public static void main(String[] arg) {

        // ? Correr este programa y ver y mostrar que hace
        for (int i = 2; i <= 50; i++) {
            boolean esPrimo = true;
            // System.out.println(i);
            for (int j = 2; j <= i / 2; j++) {
                // System.out.println(j);
                if (i % j == 0) {
                    esPrimo = false;
                    break;
                }
            }
            if (esPrimo) {
                System.out.println(i + " es primo");
            }
        }

    }

}