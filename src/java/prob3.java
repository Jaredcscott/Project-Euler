import java.util.ArrayList;
import java.util.Collections;

public class prob3 {
	public static void main(String[] args) {
		ArrayList<Long> factors = new ArrayList<Long>();
		long num = 600851475143L;
		for (long i = 1; i <= Math.sqrt(num); i++) {
			if (num % i == 0 && factors.contains(i) == false && factors.contains(num/i) == false) {
				factors.add(i);
				factors.add(num/i);				
			}
		}
		Collections.sort(factors);
		ArrayList<Long> primeFactors = new ArrayList<Long>();
		ArrayList<Long> factorFactors =  new ArrayList<Long>();
		for (long factor : factors) {
			factorFactors.clear();
			for (long j = 1; j <= Math.sqrt(factor); j++) {
				if (factor % j == 0 && factorFactors.contains(j) == false) {
					factorFactors.add(j);
				}
			}

			if (factorFactors.size() == 1 && primeFactors.contains(factor) == false) {
				primeFactors.add(factor);
			}
		}
		System.out.println(Collections.max(primeFactors));
	}
}
