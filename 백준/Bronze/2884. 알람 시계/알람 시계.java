import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int H = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        
        int total = (H * 60 + M -45 + 24 * 60) % (24 * 60);
                
        int newH = total / 60;
        int newM = total % 60;
        
        System.out.println(newH + " " + newM);
        
    }
}