
import java.io.BufferedReader;
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
        
    
    public static void main(String[] args) {
        String attempt = "IIIX";
        Scanner in = new Scanner("prob89.txt");
        while (in.hasNextLine()) {
            System.out.println(in.nextLine());
        }
//        for (int i = 0; i < attempt.length(); i++) {
//            System.out.println(getValue(attempt.charAt(i)));
//        }
    }
    
}
