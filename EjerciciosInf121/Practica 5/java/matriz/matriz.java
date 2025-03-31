package matriz;
class Matriz {
    private int[][] e;
    public Matriz(int[][] e) {
        this.e = e;
    }
    public Matriz sumar(Matriz o) {
        if (filas() != o.filas() || columnas() != o.columnas()) {
            return null;
        }
        int[][] r = new int[filas()][columnas()];
        for (int i = 0; i < filas(); i++) {
            for (int j = 0; j < columnas(); j++) {
                r[i][j] = e[i][j] + o.e[i][j];
            }
        }
        return new Matriz(r);
    }
    public int filas() {
        int c = 0;
        for (int[] _ : e) {
            c++;
        }
        return c;
    }
    public int columnas() {
        int c = 0;
        for (int _ : e[0]) {
            c++;
        }
        return c;
    }
    public void mostrar() {
        for (int i = 0; i < filas(); i++) {
            for (int j = 0; j < columnas(); j++) {
                System.out.print(e[i][j] + " ");
            }
            System.out.println();
        }
    }
}
