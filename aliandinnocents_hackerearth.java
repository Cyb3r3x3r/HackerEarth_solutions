import java.util.*;
public class aliandinnocents_hackerearth{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);         
        String name = s.nextLine();             //DDXDDD-DD
        char vowel = name.charAt(2);
        int a = (int)name.charAt(0) + (int)name.charAt(1);
        int b = (int)name.charAt(3) + (int)name.charAt(4);
        int c = (int)name.charAt(4) + (int)name.charAt(5);
        int d = (int)name.charAt(7) + (int)name.charAt(8);
        if(vowel == 'A' || vowel == 'E' || vowel == 'I' || vowel == 'O' || vowel == 'U' || vowel == 'Y'){
            System.out.println("invalid");
        }
        else if(a % 2 != 0 || b % 2 != 0 || c % 2 != 0 || d % 2 != 0){
            System.out.println("invalid");
        }
        else{
            System.out.println("valid");
        }
    }
}