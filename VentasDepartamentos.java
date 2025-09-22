import java.util.Scanner;

public class VentasDepartamentos {
    private static final String[] DEPARTAMENTOS = {"Ropa", "Deportes", "Juguetería"};
    private static final String[] MESES = {
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    };
    private static int[][] ventas = new int[DEPARTAMENTOS.length][MESES.length];
    
    public static void insertarVenta(int depto, int mes, int valor) {
        ventas[depto][mes] = valor;
    }
    
    public static int buscarVenta(int depto, int mes) {
        return ventas[depto][mes];
    }
    
    public static void eliminarVenta(int depto, int mes) {
        ventas[depto][mes] = 0; 
    }
    
    public static void mostrarVentas() {
        for (int i = 0; i < DEPARTAMENTOS.length; i++) {
            System.out.println("Departamento: " + DEPARTAMENTOS[i]);
            for (int j = 0; j < MESES.length; j++) {
                System.out.println("  " + MESES[j] + ": " + ventas[i][j]);
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        insertarVenta(0, 0, 5000); 
        insertarVenta(1, 2, 7000); 
        
        System.out.println("Venta en Ropa - Enero: " + buscarVenta(0, 0));
        
        eliminarVenta(1, 2); 
        
        mostrarVentas();
        
        scanner.close();
    }
}
