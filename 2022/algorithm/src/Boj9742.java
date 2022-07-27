import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Boj9742 {

    public static int used[];
    public static int n;
    public static String s;
    public static char str[];
    public static int p=0;
    public static void get(int now){
        if(p>n){
            return;
        }
        if(now==s.length()){
            p++;
            if(p==n){
                System.out.printf("%s %d = %s\n",s,n,String.valueOf(str));
            }
            return;
        }
        for(int i=0;i<s.length();i++){
            if(used[i]==0){
                used[i]=1;
                str[now]=s.charAt(i);
                get(now+1);
                used[i]=0;
            }
        }
    }
    public static void main(String args[]) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String in;
        while ((in=bf.readLine())!=null) {
            StringTokenizer st= new StringTokenizer(in);
            s=st.nextToken();
            str=new char[s.length()];
            used=new int[s.length()];
            n=Integer.parseInt(st.nextToken());
            p=0;
            int com=1;
            for(int i=1;i<s.length()+1;i++){
                com*=i;
            }
            if(n>com){
                System.out.printf("%s %d = %s\n",s,n,"No permutation");
            }
            else{
                get(0);
            }
        }
    }

}
