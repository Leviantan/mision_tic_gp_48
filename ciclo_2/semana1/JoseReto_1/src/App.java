public class App {
    public static void main(String[] args) throws Exception {
        
        BecaUniversitaria becaUniversitaria = new BecaUniversitaria();
        System.out.println(becaUniversitaria.calcularInteresSimple());
        System.out.println(becaUniversitaria.calcularInteresCompuesto());
        System.out.println(becaUniversitaria.compararInversion());
    }
    
}

class BecaUniversitaria{
    //atributos
    
    //tiempo
    private int tiempo;
    //valor beca u
    private double monto;
    //valor interes que se aplica al proyecto
    private double interes;


    //constructores nuevo proyecto con valores
    public BecaUniversitaria(){
        tiempo = 0;
        monto = 0;
        interes = 0;
    }

    public BecaUniversitaria(int pTiempo, double pMonto, double pInteres){
        this.tiempo = pTiempo;
        this.monto = pMonto;
        this.interes = pInteres;
    }

    //los metodos

    //calcula y retorna el interes simple, monto - tiempo
    // interes simple generado

    public double calcularInteresSimple(){
        double interesSimple = monto * (interes/100) * tiempo;
        return  Math.round(interesSimple);
    }

    //calcula y retorno el interes compuesto, monto - tiempo
    // interes compuesto generado

    public double calcularInteresCompuesto(){
        double interesCompuesto = monto * (Math.pow(1+interes/100, tiempo));
        return Math.round(interesCompuesto);
    }

    
    public String compararInversion(int pTiempo, double pMonto, double pInteres){
        this.tiempo = pTiempo;
        this.monto = pMonto;
        this.interes = pInteres;

        //calular diferencia entre interes compuesto y el interes simple
        double diferencia = calcularInteresCompuesto() - calcularInteresSimple();
        if(diferencia != 0){
            return "La diferencia entre la proyección de interés compuesto e interés simple es: $" + diferencia;
        }else{
            return "No se obtuvo diferencia entre las proyecciones, revisar los parámetros de entrada.";
        }

    }

    public String compararInversion(){
        double diferencia = 0;

        //calcula difrencia de las tasas de interes
        diferencia = calcularInteresCompuesto() - calcularInteresSimple();

        //revisar la diferencia
        if(diferencia != 0){
            return "La diferencia entre la proyección de interés compuesto e interés simple es: $" + diferencia;
        }else{
            return "No se obtuvo diferencia entre las proyecciones, revisar los parámetros de entrada.";
        }      

    }
}