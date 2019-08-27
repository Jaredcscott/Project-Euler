public class prob9 {
    public static void main(String[] args){
        int product = 0;
        for (int i = 0; i < 1000; i++) {
            for (int j = 0; j < 1000; j++) {
                for (int k = 0; k < 1000; k++) {
                    if ((i * i) + (j * j) == (k * k) && i < j && i < k && j < k) {
                        if ((i + j + k) == 1000) {
                            product = i * j * k;
                            System.out.println("Pythagorean triplet found : " + i + "," + j + "," + k);
                            System.out.println("Solution: " + product);
                        }
                    }
                }
            }
        }
    }
}
