
public class probandoClases {

    public static void main(String[] args) {
        AñoBisiesto añito = new AñoBisiesto(2001);

        añito.verificarAño();
        añito.info();
    }

    class AñoBisiesto {
        int año;

        // * Constructor de la clase
        public AñoBisiesto(int año) {
            this.año = año;
        }

        // * Metodo de la clase
        public void verificarAño() {
            if ((año % 4 == 0 && año % 100 != 0) || (año % 400 == 00)) {
                System.out.println("Es bisiesto");
            } else {
                System.out.println("NO es un año bisiesto");
            }
        }

        public void info() {
            System.out.println("El año elegido a verificar es: " + this.año);
        }

    }
}