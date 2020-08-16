
import java.math.BigInteger;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author jareds
 */

public class prob55 {
    
    public static boolean isPalindrome(BigInteger num) {
        String numS = "" + num;
        if (numS.length() == 1) {
            return true;
        }
        else {
            int endInd = numS.length()-1;
            for (int i = 0; i < (numS.length()/2) ; i++) {
                if (numS.charAt(i) != numS.charAt(endInd)) {
                    return false;
                }
                endInd -= 1;
                
            }
            return true;
        }
    }
    
    public static BigInteger iterate(BigInteger num, int curIteration) {
        String numS = "" + num;
        String numR = "";
        for(int j = numS.length() - 1; j >= 0; j--) {
            numR += numS.charAt(j);
        }
        BigInteger num2 = new BigInteger(numR);
        return (num.add(num2));
    }
    
    public static void main(String[] args) {
        int nums = 0;
        for (int i = 1; i <= 10000; i++) {
            int iterations = 0;
            BigInteger curNum = new BigInteger("" + i);
            boolean isPalin = false;
            while (iterations <= 50 && !isPalin) {
                curNum = iterate(curNum, iterations);
                isPalin = isPalindrome(curNum);
                if(isPalin) {
                     
                }
                if (!isPalin && iterations == 50) {
                   System.out.println("No Palindrome found with seed: " + i);
                   nums += 1;
                }
                iterations += 1;
            } 
        }
        System.out.println(nums);
    }
}
