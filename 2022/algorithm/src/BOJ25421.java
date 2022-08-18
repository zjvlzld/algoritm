import java.util.Scanner;

public class BOJ25421 {
    public static void main(String args[]){
        int n=new Scanner(System.in).nextInt();
        int dp[][]=new int[n][10];
        for(int i=1;i<10;i++){
            dp[0][i]=1;
        }
        for(int i=1;i<n;i++){
            for(int j=1;j<10;j++){
                int t=0;
                for(int k=j-2;k<=j+2;k++){
                    if(k>0&&k<10){
                        t+=dp[i-1][k];
                        t%=987654321;
                    }
                }
                dp[i][j]=t;
            }
        }
        int ans=0;
        for(int i=0;i<10;i++){
            ans+=dp[n-1][i];
            ans%=987654321;
        }
        System.out.println(ans);

    }
}
