import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        while(true){
            String line = br.readLine();
            if (line == null) {
                break;
            } else {
                StringTokenizer st = new StringTokenizer(line);
                int A = Integer.parseInt(st.nextToken());
                int B = Integer.parseInt(st.nextToken());
            
                if (A == 0 && B == 0) {
                    break;
                } else {
                    sb.append(A+B).append("\n");
                }
            }
            
        }
        System.out.print(sb.toString());
        
    }
}