import java.util.*;
public class divisibility_hackerearth{
    public static void main(String[] args){
        int arr[];
        Scanner s = new Scanner(System.in);
        int N = s.nextInt();
        arr = new int[N];
        for(int i = 0;i<N;i++){
            arr[i] = s.nextInt();
        }
        if(arr[N-1] % 10 == 0){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
    }
}