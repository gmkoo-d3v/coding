import java.util.Scanner;

public class Main{
    public static void main(String[] args) throws Exception{
        Scanner sc = new Scanner(System.in);
        int X=sc.nextInt();
        int N=sc.nextInt();
        int a=0;
        int b=0;
        int total=0;
        for (int i=0;i<N;i++){
            a=sc.nextInt();
            b=sc.nextInt();
            total += a*b;
        }
        if (X==total){
            System.out.println("Yes");
        }else{
            System.out.println("No");
        }
        sc.close();
        
        
    }
}