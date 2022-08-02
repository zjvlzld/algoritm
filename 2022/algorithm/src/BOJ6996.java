import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ6996 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int test=Integer.parseInt(br.readLine());
        for(int T=1;T <test+1;T++) {
            boolean check=true;
            int count[] = new int[(int) 'z' - (int) 'a' + 1];
            StringTokenizer st = new StringTokenizer(br.readLine());
            String first = st.nextToken();
            for (int i = 0; i < first.length(); i++) {
                count[(int) first.charAt(i) - (int) 'a']++;
            }
            String second = st.nextToken();
            for (int i = 0; i < second.length(); i++) {
                count[(int) second.charAt(i) - (int) 'a']--;
            }
            for (int i = 0; i < (int) 'z' - (int) 'a' + 1; i++) {
                if (count[i] != 0) {
                    System.out.println(first + " & " + second + " are NOT anagrams.");
                    check=false;
                    break;
                }
            }
            if(check){
                System.out.println(first + " & " + second + " are anagrams.");
            }
        }
    }
}
