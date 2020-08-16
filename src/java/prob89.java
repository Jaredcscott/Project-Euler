import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

/**
 *
 * @author jareds
 */
public class prob89 {
    
    public static int getValue(char letter1, char letter2) {
        switch (letter1) { 
            case 'I': 
                if (letter2 == 'V' || letter2 == 'X') {
                   return -1;
                }
                else {
                    return 1;
                }
            case 'V': 
                return 5; 
            case 'X':
                if (letter2 == 'L' || letter2 == 'C') {
                    return -10;
                }
                else {
                   return 10; 
                }
            case 'L': 
                return 50;  
            case 'C':
                if (letter2 == 'D' || letter2 == 'M') {
                    return -100;
                }
                else {
                    return 100;
                } 
            case 'D': 
                return 500; 
            case 'M': 
                return 1000;
        }
        return 0;
    }
    
    public static String minimize(String line, int value){
        StringBuilder minimal = new StringBuilder();
            while (value >= 1000) {
                minimal.append('M');
                value -= 1000;
            }
            if (value >= 900) {
                minimal.append("CM");
                value -= 900;
            }
            while (value >= 500) {
                minimal.append('D');
                value -= 500;
            }
            if (value >= 400) {
                minimal.append("CD");
                value -= 400;
            }
            while (value >= 100) {
                minimal.append('C');
                value -= 100;
            }
            if (value >= 90) {
                minimal.append("XC");
                value -= 90;
            }
            while (value >= 50) {
                minimal.append('L');
                value -= 50;
            }
            if (value >= 40) {
                minimal.append("XL");
                value -= 40;
            }
            while (value >= 10) {
                minimal.append('X');
                value -= 10;
            }
            if(value >= 9) {
                minimal.append("IX");
                value -= 9;
            }
            while (value >= 5) {
                minimal.append('V');
                value -= 5;
            }
            if (value >= 4) {
                minimal.append("IV");
                value -= 4;
            }
            while (value >= 1) {
                minimal.append('I');
                value -= 1;
            }
        return minimal.toString();
    }
        
    
    public static void main(String[] args) throws FileNotFoundException {
        String attempt = "IIIX";
        File file = new File("src/prob89.txt");
        Scanner in = new Scanner(file);
        int totalSaved = 0;
        int charSaved = 0;
        while (in.hasNextLine()) {
            String line = in.nextLine();
            int lineLength = line.length();
            int lineSum = 0;
            for (int i = 0; i < line.length(); i++) {
                if (i == line.length() - 1) {
                    lineSum += getValue(line.charAt(i), 'E');
                }
                else {
                   lineSum += getValue(line.charAt(i), line.charAt(i + 1)); 
                }
            }
            String minimal = minimize(line, lineSum); 
            int minimalLength = minimal.length();
            charSaved = lineLength - minimalLength; //
            totalSaved += charSaved;
            System.out.println(line + " Value: " + lineSum + "  :  " + minimize(line, lineSum) + " Char saved: " + charSaved);
        }
        System.out.println(totalSaved);
    }
    
}
