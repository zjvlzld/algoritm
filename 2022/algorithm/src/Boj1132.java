import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Boj1132
{
    static class Info implements Comparable<Info> {
        long num=0;
        boolean first=false;


        @Override
        public int compareTo(Info o) {
            if(num>o.num){
                return 1;
            }
            if(num==o.num){
                return 0;
            }
            else
            {
                return -1;
            }
        }
    }
    static public void main(String args[]) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(bf.readLine());
        Info cal[]=new Info[10];
        for(int i=0;i<10;i++){
            cal[i]=new Info();
        }
        for(int t=0;t<n;t++) {
            String s1 = bf.readLine();
            cal[(int) (s1.charAt(0) - 'A')].num += Math.pow(10, s1.length() - 1 - 0);
            cal[(int) (s1.charAt(0) - 'A')].first=true;
            for (int i = 1; i < s1.length(); i++) {
                cal[(int) (s1.charAt(i) - 'A')].num += Math.pow(10, s1.length() - 1 - i);
            }
        }
        long ans=0;
        Arrays.sort(cal);
        int used[]=new int[10];

        for(int i=0;i<10;i++){
            if(cal[i].first){
                for(int j=1;j<10;j++){
                    if(used[j]==0){
                        ans+=cal[i].num*(long)j;
                        used[j]=1;
                        break;
                    }
                }
            }
            else {
                for(int j=0;j<10;j++){
                    if(used[j]==0){
                        ans+=cal[i].num*(long)j;
                        used[j]=1;
                        break;
                    }
                }
            }
        }
        System.out.println(ans);

    }
}
