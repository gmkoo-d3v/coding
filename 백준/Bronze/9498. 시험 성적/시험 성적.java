import java.io.*;

public class Main{
    public static void main(String[] args) throws Exception{
        int score = Integer.parseInt(new BufferedReader(new InputStreamReader(System.in)).readLine());
        char[] group = {'F','F','F','F','F','F','D','C','B','A','A'};
        System.out.print(group[score / 10]);    
    }
}