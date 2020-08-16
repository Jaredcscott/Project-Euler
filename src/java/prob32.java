import java.util.ArrayList;
import java.util.Arrays;
import java.util.Hashtable;

/**
 *
 * @author jareds
 */
public class prob32 {
    public static boolean isPandigital(Long num) {
        boolean dupNums = false;
        String numString = "" + num;
        boolean[] nums = new boolean[9];
        if ( numString.length() == 9 ) {
            for (int i = 1 ; i <= numString.length(); i++) {
                char c = numString.charAt(i-1);
                Integer index = Character.getNumericValue(c);
                if (index == 0) {
                    return false;
                }
                //System.out.println(index);
                if(!nums[index-1]) {
                    nums[index-1] = true;
                }
                else {
                    //System.out.println(index);
                    dupNums = true;
                }
            }
        }
        else {
            return false; //"Failure!"
        }
        return !dupNums ; //? "Sucess! " + numString : "Failure!"
    }
    
    
    public static void main(String[] args) {
        ArrayList<Long> numsToCheck = new ArrayList<Long>();
        numsToCheck.add(2348157690l);
        numsToCheck.add(217843568l);
        numsToCheck.add(391867254l);
        int sum = 0;
        ArrayList<Integer> numsFound = new ArrayList<Integer>();
        for (int i = 1; i < 10000; i++) {
            for (int j = 0 ; j < 10000; j++) {
                int num = i * j;
                String numS = "" + i + "" + j + "" + num;
                if (numS.length() == 9) {
                    if( isPandigital(Long.parseLong(numS)) ) {
                        //System.out.println(Long.parseLong(numS));
                        if (!numsFound.contains(num)) {
                            sum += num;
                            numsFound.add(num);
                        }
                        else {
                            //System.out.println(num);
                        }
                    }
                } 
            }
        }
        System.out.println(sum);
    }
}
