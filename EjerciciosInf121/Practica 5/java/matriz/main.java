package matriz;
public class main {
    public static void main(String[] args) {
        Matriz m1 = new Matriz(new int[][]{{1, 2}, {3, 4}});
        Matriz m2 = new Matriz(new int[][]{{5, 6}, {7, 8}});
        Matriz m3 = m1.sumar(m2);
        if (m3 != null) {
            m3.mostrar();
        }
    }
}
    

