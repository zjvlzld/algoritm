import java.util.Scanner;

public class BOJ25418 {
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int s=sc.nextInt();
        int e=sc.nextInt();
        int dp[]=new int[e+1];
        dp[s]=1;
        for(int i=s+1;i<e+1;i++){
            dp[i]=dp[i-1]+1;
            if(i%2==0&&dp[i/2]!=0){
                dp[i]=dp[i/2]+1;
            }
        }
        System.out.println(dp[e]-1);
    }
}
