
import java.util.ArrayList;
import java.util.Arrays;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author jareds
 */
public class prob32 {
    public static String isPandigital(Long num) {
        boolean dupNums = false;
        String numString = "" + num;
        boolean[] nums = new boolean[10];
        if ( numString.length() == 10 ) {
            for (int i = 0 ; i <numString.length(); i ++) {
                char c = numString.charAt(i);
                Integer index = Character.getNumericValue(c);
                if(!nums[index]) {
                    nums[index] = true;
                }
                else {
                    dupNums = true;
                }
            }
        }
        else {
            return "Failure!";
        }
        return !dupNums ? "Sucess! " + numString : "Failure!";
    }
    public static void main(String[] args) {
        ArrayList<Long> numsToCheck = new ArrayList<Long>();
        numsToCheck.add(2348157690l);
        numsToCheck.add(1264538779l);
        numsToCheck.add(234815590l);
        
        
        for(Long num : numsToCheck) {
            System.out.println(isPandigital(num));
        }   
    }
}
