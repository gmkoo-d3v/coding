import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb =new StringBuilder();
        String line;
        
        while ((line = br.readLine()) != null  ) {
            String[] ar =line.split(" ");
            int A = Integer.parseInt(ar[0]);
            int B = Integer.parseInt(ar[1]);
            
            sb.append(A+B).append("\n");
        }
        System.out.print(sb);
    }
}