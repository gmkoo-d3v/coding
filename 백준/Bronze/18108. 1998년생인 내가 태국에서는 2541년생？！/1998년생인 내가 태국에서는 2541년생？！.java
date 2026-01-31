import java.util.Scanner;

public class Main{
    public static int convertAD(int ThaiYear){
        return ThaiYear - 543;
    }
    public static void main(String[] args){
        Scanner sc =new Scanner(System.in);
        int thaiYear = sc.nextInt();
        System.out.println(convertAD(thaiYear));
        sc.close();
    }
    
}