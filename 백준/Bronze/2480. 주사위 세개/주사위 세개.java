import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        
        int a = Integer.parseInt(input[0]);
        int b = Integer.parseInt(input[1]);
        int c = Integer.parseInt(input[2]);
        
        System.out.println(calculatePrize(a,b,c));
    }
    
    private static int calculatePrize(int a,int b,int c){
        if (a==b && b==c){
            return 10000+a*1000;
        }
        if (a==b || b==c || a==c){
            int same =(a==b) ? a: (b==c)? b:a;
            return 1000+same*100;
        }
        return Math.max(a,Math.max(b,c))*100;
    }
}