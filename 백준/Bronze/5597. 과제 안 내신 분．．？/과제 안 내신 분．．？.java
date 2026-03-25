import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        ArrayList<Integer> studentNumbers =new ArrayList<>();

        for(int i = 1; i <= 30; i++){
            studentNumbers.add(i);
        }
        for(int i = 0; i < 28; i++){
            int submitted = Integer.parseInt(br.readLine());
            studentNumbers.remove(Integer.valueOf(submitted));
        }
        System.out.println(studentNumbers.get(0));
        System.out.println(studentNumbers.get(1));


    }
}

