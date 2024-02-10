import java.util.*;
public class factorial_hackerearth{
    public static void main(String[] args){
        int fact=1;
        Scanner s = new Scanner(System.in);
        int N = Integer.parseInt(s.nextLine());
        if(N>=1 && N<=10){
            while(N>=1){
                fact = fact * N;
                N--;
            }
            System.out.print(fact);
        }
        else{
            System.exit(0);
        }
    }
}