package vector;

public class main {
    public static void main(String[] args) {
        Vector v1 = new Vector(new int[]{1, 2, 3});
        Vector v2 = new Vector(new int[]{4, 5, 6});
        Vector r = v1.sumar(v2);
        if (r != null) {
            r.mostrar();
        }
    }
}
