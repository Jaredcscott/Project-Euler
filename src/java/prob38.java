import java.util.ArrayList;

/**
 *
 * @author jareds
 */
public class prob38 {
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
        ArrayList<Long> numsFound = new ArrayList<Long>();
        Long maxNum = 0l;
        boolean nine = false;
        boolean breakBool = false;
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < 10000 ; i++) {
            for (int j = 1; j <= 100 ; j++) {
                for (int k = 1; k <= j; k++) {
                    int prod = i * k;
                    String prodS = "" + prod;
                    sb.append(prodS);
                    if (sb.length() > 15) {
                        breakBool = true;
                        break;
                    }
                    Long numLong = Long.parseLong(sb.toString());
                    if (nine) {
                        //System.out.println(k);
                    }
                    
                    String numS = numLong + "";
                    if (numS.length() == 9 && isPandigital(numLong)) {
                        if (!(numsFound.contains(numLong))) {
                            numsFound.add(numLong);
                            if (numLong > maxNum) {
                                maxNum = numLong;
                            }
                            //System.out.println(numLong);
                        }
                        
                    }
                }
                if (nine) {
                    System.out.println(sb);
                }
                
                sb.delete(0, sb.length());
                if (breakBool) {
                    break;
                }
            }
            breakBool = false;
        }
        System.out.println(maxNum);
    }   
}
