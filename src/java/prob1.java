import java.util.ArrayList;

public class prob1 {
	public static void main(String[] args) {
		ArrayList<Integer> nums = new ArrayList<Integer>();
		for (int i = 0; i < 1000; i++) {
			if (i % 3 == 0 || i % 5 == 0) {
				nums.add(i);
			}
		}
		int sum = 0;
		for (int num : nums) {
			sum += num;
		}
		System.out.println(sum);
	}
}
