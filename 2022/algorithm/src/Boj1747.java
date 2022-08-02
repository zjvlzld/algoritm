import java.util.Scanner;

public class Boj1747 {
    public static void main(String args[]){
        Scanner sc= new Scanner(System.in);
        long s=sc.nextLong();
        long e=sc.nextLong();
        long ans=0;
        long sosu[]=new long[(int)Math.sqrt(100000000000000l)+1];
        sosu[2]=1;
        long temp=2*2;
        while(temp<=e){
            if(temp>=s){
                ans++;
            }
            if(temp>Long.MAX_VALUE/2){
                break;
            }
            temp*=2;
        }
        for(long i=3;i<sosu.length;i+=2){
            if(sosu[(int)i]==0){
                sosu[(int)i]=1;
                temp=i*i;
                while(temp<=e){
                    if(temp>=s){
                        ans++;
                    }
                    if(temp> Long.MAX_VALUE/i){
                        break;
                    }
                    temp*=i;
                }

                for(long j=i;j< sosu.length;j+=i){
                    sosu[(int)j]=1;
                }
            }
        }
        System.out.println(ans);
    }
}
