import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        int N = Integer.parseInt(br.readLine());
        
        for (int a = 1; a <=N; a++){
            for (int b = 0; b <a; b++){
            sb.append("*");
            }
            sb.append("\n");
        }
        System.out.println(sb);
        
    }
}
