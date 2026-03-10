import java.io.*;


public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String S = br.readLine();
        int[] result = new int[26];
        
        for(int i = 0; i < 26; i++){
            result[i] = -1;
        }
        
        for(int i = 0; i < S.length(); i++){
            int index = S.charAt(i) - 'a';
            
            if(result[index] == -1){
                result[index] = i;
            }
        }
        
        for(int i = 0; i < 26; i++){
            System.out.print(result[i] + " ");
        }
    }
}
