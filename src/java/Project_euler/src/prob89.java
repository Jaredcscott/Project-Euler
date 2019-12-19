import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author jareds
 */
public class prob89 {
    
    public static int getValue(char letter) {
        switch (letter) { 
            case 'I': 
                return 1; 
            case 'V': 
                return 5; 
            case 'X': 
                return 10; 
            case 'L': 
                return 50;  
            case 'C': 
                return 100; 
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
            while (value >= 500) {
                minimal.append('D');
                value -= 500;
            }
            while (value >= 100) {
                minimal.append('C');
                value -= 100;
            }
            while (value >= 50) {
                minimal.append('L');
                value -= 50;
            }
            while (value >= 10) {
                
                minimal.append('X');
                value -= 10;
            }
            if(value == 9) {
                minimal.append("IX");
                value -= 9;
            }
            while (value >= 5) {
                minimal.append('V');
                value -= 5;
            }
            if (value == 4) {
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
        int charSaved = 0;
        while (in.hasNextLine()) {
            String line = in.nextLine();
            int lineLength = line.length();
            int lineSum = 0;
            for (int i = 0; i < line.length(); i++) {
                lineSum += getValue(line.charAt(i));
            }
            
//            while (lineSum >= 1000) {
//                minimal.append('M');
//                lineSum -= 1000;
//            }
//            while (lineSum >= 500) {
//                minimal.append('D');
//                lineSum -= 500;
//            }
//            while (lineSum >= 100) {
//                minimal.append('C');
//                lineSum -= 100;
//            }
//            while (lineSum >= 50) {
//                minimal.append('L');
//                lineSum -= 50;
//            }
//            while (lineSum >= 10) {
//                
//                minimal.append('X');
//                lineSum -= 10;
//            }
//            if(lineSum == 9) {
//                minimal.append("IX");
//                lineSum -= 9;
//            }
//            else if (lineSum == 8) {
//                minimal.append("IIX");
//                lineSum -= 8;
//            }
//            while (lineSum >= 5) {
//                minimal.append('V');
//                lineSum -= 5;
//            }
//            while (lineSum >= 1) {
//                minimal.append('I');
//                lineSum -= 1;
//            }
            
            charSaved = lineLength; // - minimalLength
            System.out.println(line + " Value: " + lineSum + "  :  " + minimize(line, lineSum));
        }
    }
    
}
