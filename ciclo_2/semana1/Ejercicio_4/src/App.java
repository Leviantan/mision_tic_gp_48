public class App {
    public static void main(String[] args) throws Exception {
        
        // Ciclo de for

        /*
            for (inicializacion; condicion; incremento) {
                instrucciones
            }
        */
        
        /*
        for (int i = 0; i < 100; i++) {
            System.out.println("Numero es: " + i);
        }
        */

        // Ciclo de while

        /*
        var numero = 0;
        while (numero < 100){
            if (numero > 10) {
                break;
            }
            System.out.println("numero while es: " + numero);
            numero++;
        }
        */

        // Ciclo do while
        // solo imprimir desde el numero 100 hasta el numero 120.

        var numero2 = 0;
        do {
            if ((numero2 >= 100) && (numero2 <= 120)){
                System.out.println("Numero do while es: " + numero2);
            }
            numero2++;
        } while (numero2 < 200);
    }
}
