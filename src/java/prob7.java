import java.util.ArrayList;

public class prob7 {
	public static void main(String[] args) {
		ArrayList<Integer> primes = new ArrayList<>();
		ArrayList<Integer> factors = new ArrayList<>();
		int curNum = 1;
		while (primes.size() < 10001) {
			factors.clear();
			for (int i = 1; i <= curNum; i++) {
				if (curNum % i == 0) {
					factors.add(i);
				}
			}
			if (factors.size() == 2) {
				primes.add(curNum);
			}
			curNum++;
		}
		System.out.println(primes.get(primes.size() - 1));
	}
}
