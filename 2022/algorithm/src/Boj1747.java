import java.util.Scanner;

public class Boj1747 {
    public static void main(String args[]){
        Scanner sc= new Scanner(System.in);
        long s=sc.nextLong();
        long e=sc.nextLong();
        int ans=0;
        int sosu[]=new int[(int)Math.sqrt(e)+2];
        sosu[2]=0;
        long temp=2*2;
        while(temp<=e){
            if(temp>=s){
                ans++;
            }
            temp*=(long)2;
        }
        for(int i=3;i<(int)Math.sqrt(e)+2;i+=2){
            if(sosu[i]==0){
                sosu[i]=1;
                temp=(long)i*i;
                while(temp<=e){
                    if(temp>=s){
                        ans++;
                    }
                    temp*=i;
                }
                if((long)i*i>e){
                    break;
                }
                for(int j=i;j<(int)Math.sqrt(e)+2;j+=i){
                    sosu[j]=1;
                }
            }
        }
        System.out.println(ans);
    }
}
