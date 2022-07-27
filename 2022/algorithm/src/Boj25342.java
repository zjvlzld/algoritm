import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Boj25342
{
    public static long gcd(long a,long b){
        if(a<b){
            return gcd(b,a);
        }
        if(b==0){
            return a;
        }
        return gcd(b,a%b);

    }

    public static void main(String args[]) throws IOException {
        StringBuilder ans=new StringBuilder();
        BufferedReader bf=new BufferedReader(new InputStreamReader(System.in));
        int T=Integer.parseInt(bf.readLine());
        int[] sosu = new int[100001];
        for(int i=2;i<100001;i++){
            if(sosu[i]==0){
                sosu[i]=1;
                for(int j=i+i;j<100001;j+=i){
                    sosu[i]=2;
                }
            }
        }
        for(int test=0;test<T;test++){
            long n=Long.parseLong(bf.readLine());
            long now=n*(n-1)*(n-2)/gcd(n*(n-1),n-2);
            // System.out.println(now);
            for(long i=n-2;i>=1;i--){
                long temp=n*(n-1)*i/gcd(n*(n-1),i);
                if(now<temp){
                    now=temp;
                }
                if(sosu[(int)i]==1){
                    break;
                }
            }
            n--;
            for(long i=n-2;i>=1;i--){
                long temp=n*(n-1)*i/gcd(n*(n-1),i);
                if(now<temp){
                    now=temp;
                }
                if(sosu[(int)i]==1){
                    break;
                }
            }
            ans.append(now).append("\n");
//            System.out.println(now);
        }
        System.out.println(ans);

    }
}
