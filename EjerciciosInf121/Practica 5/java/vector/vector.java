package vector;
class Vector {
    private int[] e;

    public Vector(int[] e) {
        this.e = e;
    }
    public Vector sumar(Vector o) {
        if (t() != o.t()) {
            return null;
        }
        int[] r = new int[t()];
        for (int i = 0; i < t(); i++) {
            r[i] = e[i] + o.e[i];
        }
        return new Vector(r);
    }
    public int t() {
        int c = 0;
        for (int _ : e) {
            c++;
        }
        return c;
    }
    public void mostrar() {
        for (int i = 0; i < t(); i++) {
            System.out.print(e[i] + " ");
        }
        System.out.println();
    }
}
