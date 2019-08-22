public class prob6 {
	public static void main(String [] args) {
		double sumOfSquares = 0;
		double squareOfSums = 0;
		for (int i = 0; i <= 100; i++) {
			sumOfSquares += Math.pow(i,2);
			squareOfSums += i;
		}
		squareOfSums = Math.pow(squareOfSums, 2);
		double result = squareOfSums - sumOfSquares;
		System.out.printf("Result: %f", result);
	}
}
