/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

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
        int maxNum = 0;
        int num = 192;
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < 4; i++) {
            int prod = num * i;
            sb.append("" + prod);
        }
        
        System.out.println(sb.toString());
        System.out.println(isPandigital(Long.parseLong(sb.toString())));
    }
    
}
