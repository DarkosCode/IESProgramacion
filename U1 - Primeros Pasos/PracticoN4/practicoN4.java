import java.util.Scanner;

public class practicoN4 {
    public static void main(String[] args) {

        Scanner entradaTeclado = new Scanner(System.in);

        // // ? 1. Muestre la longitud de una cadena de caracteres ingresado x teclado.
        // System.out.println("Ingrese una palabra o cadena de texto: ");
        // String ingresado = entradaTeclado.nextLine();
        // int contadorCaracteres = ingresado.length();
        // System.out.println("La cadena de caracteres: " + ingresado + " tiene " +
        // contadorCaracteres + " caracteres");

        // // ? 2. Elimina los espacios de una cadena ingresada.
        // System.out.println();
        // System.out.println("2 - ELIMINAR ESPACIOS DE UNA CADENA");
        // // * Con replace
        // String ingresadoSinEspacios;
        // if (ingresado.contains(" ")) {
        // ingresadoSinEspacios = ingresado.replace(" ", "");
        // } else {
        // ingresadoSinEspacios = ingresado;
        // }
        // System.out.println(ingresado + " → " + ingresadoSinEspacios);

        // // ? 3: Cuenta las vocales de una String ingresada.
        // System.out.println();
        // System.out.println("3 - CONTAR VOCALES DE LA CADENA");

        // // * Con un for
        // int contadorDeVocales = 0;
        // if (ingresado.toLowerCase().contains("a") ||
        // ingresado.toLowerCase().contains("e")
        // || ingresado.toLowerCase().contains("i") ||
        // ingresado.toLowerCase().contains("o")
        // || ingresado.toLowerCase().contains("u")) {
        // for (int v = 0; v < ingresado.length(); v++) {
        // if (ingresado.charAt(v) == 'a' || ingresado.charAt(v) == 'e' ||
        // ingresado.charAt(v) == 'i'
        // || ingresado.charAt(v) == 'o' || ingresado.charAt(v) == 'u') {
        // contadorDeVocales++;
        // }
        // }
        // }
        // System.out.println("El string: \"" + ingresado + "\" tiene " +
        // contadorDeVocales + " vocales.");

        // // ? 4 Transforma una cadena a mayúsculas.
        // System.out.println();
        // System.out.println("4 - TRANSFORMAR CADENA A MAYUSCULAS");
        // String ingEnMayusculas = ingresado.toUpperCase();
        // System.out.println(ingresado + " → " + ingEnMayusculas);

        // // ? 5: Compara dos cadenas ingresadas por teclado. Determinar sI son
        // iguales.
        // System.out.println();
        // System.out.println("5 - COMPARAR DOS STRING A VER SI SON IGUALES");
        // System.out.println("Ingresar el segundo string: ");
        // String S2Ingresado = entradaTeclado.nextLine();
        // if (ingresado.equalsIgnoreCase(S2Ingresado.toLowerCase())) {
        // System.out.println("Las dos cadenas ingresadas SON IGUALES");
        // } else {
        // System.out.println("Las cadenas ingresadas SON DISTINTAS");

        // }

        // // ? 6 Ingresar un nombre por teclado y mostrar con que letra comienza.
        // System.out.println();
        // System.out.println("6 - INGRESAR UN NOMBRE Y MOSTRAR SU INICIAL");
        // System.out.println("Ingresar un nombre: ");
        // String nombre = entradaTeclado.nextLine();
        // System.out.println("La primer letra de " + nombre.trim() + " es: " +
        // nombre.trim().charAt(0));

        // // ? 7. Ingresar una cadena que contenga un punto y muestre lo que hay
        // después
        // // ? del punto.
        // System.out.println();
        // System.out.println("7 - INGRESAR UNA CADENA CON PUNTO, MOSTRAR LO
        // SIGUIENTE");
        // System.out.println("Ingresar una cadena con punto y texto despues del punto:
        // ");
        // String cadenaConPunto = entradaTeclado.nextLine();
        // if (cadenaConPunto.contains(".")) {
        // int indiceDelPunto = cadenaConPunto.indexOf(".");
        // String AfterPunto = cadenaConPunto.substring(indiceDelPunto + 1);
        // System.out.println("La cadena despues del punto es: \"" + AfterPunto.trim() +
        // "\"");
        // } else {
        // System.out.println("La cadena no contiene un punto, ingresar otra.");
        // }

        // ? 8. contar la cantidad de palabras de una string.
        // System.out.println();
        // System.out.println("8 - INGRESAR UNA CADENA PARA CONTAR LAS PALABRAS");
        // System.out.println("Ingresar una cadena preferentemente de varias palabras:
        // ");
        // String cadenaPalabras = entradaTeclado.nextLine();
        // int contadorPalabras = 0;
        // boolean dentroDePalabra = false;

        // for (int cc = 0; cc < cadenaPalabras.length(); cc++) {
        // char caracterActual = cadenaPalabras.charAt(cc);

        // if (caracterActual != ' ') {
        // if (!dentroDePalabra) {
        // contadorPalabras++;
        // dentroDePalabra = true;
        // }
        // } else {
        // dentroDePalabra = false;
        // }
        // }

        // System.out.println("La cadena tiene " + contadorPalabras + " palabras.");

        // ? 9. Ingresar una dirección de correo y verificar que la longitud no supere
        // ? los 12 caracteres. Tenga un @ y termine en . Com
        System.out.println();
        System.out.println("9 - INGRESAR UNA DIRECCION DE CORREO Y VERIFICAR: (<12), @ y .Com");
        System.out.println("Ingresar una direccion de correo electronico: ");
        String correo = entradaTeclado.nextLine();

        String correoHastaArroba = correo.trim().substring(0, correo.indexOf("@"));
        // System.out.println(correoHastaArroba);
        // System.out.println(correo.trim().length());
        // System.out.println(correo.indexOf("l"));
        // System.out.println(correo.charAt((correo.length() - 5)));

        if (correoHastaArroba.length() <= 12 && correo.contains("@") && correo.contains(".com")) {
            System.out.println("El correo: " + correo + " es valido");
        } else {
            System.out
                    .println("El correo: " + correo
                            + " no tiene @, tiene mas de 12 caracteres o no termina con \".com\"");
        }

        // ? 10. El usuario ingresa una cadena hasta verificar que tenga longitud mayor
        // ? que 8 y la primera letra comience en mayúscula, en este caso mostrará el
        // ? mensaje "cadena correcta".
        // ? Si no cumple alguna de las condiciones mostrará el mensaje "cadena
        // ? incorrecta, vuelva a ingresar".

    }
}