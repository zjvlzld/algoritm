import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Boj1160  {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(bf.readLine());
        int N=Integer.parseInt(st.nextToken());
        int M=Integer.parseInt(st.nextToken());
        int m[][]=new int[N][N];//값을 받을 변수
        int dp[][]=new int[N][N];//0,0부터 x,y까지의 합
        for(int i=0;i<N;i++) {
            st = new StringTokenizer(bf.readLine());
            for (int j = 0; j < N; j++) {
                m[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        for(int i=0;i<N;i++) {
            for(int j=0;j<N;j++){
                if(i==0){
                    if(j==0){
                        dp[i][j]=m[i][j];//0,0은 그냥 m[0][0]
                    }
                    else{
                        dp[i][j]=dp[i][j-1]+m[i][j];//맨 위의 경우 옆까지의 합 + 나
                    }
                }
                else{
                    if(j==0){
                        dp[i][j]=dp[i-1][j]+m[i][j];//맨 왼쪽의 경우 위까지의 합 + 나
                    }
                    else {
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + m[i][j];//점화식
                    }
                }
            }
        }
        for(int i=0;i<M;i++){
            st=new StringTokenizer(bf.readLine());
            int sY=Integer.parseInt(st.nextToken())-1;
            int sX=Integer.parseInt(st.nextToken())-1;
            int eY=Integer.parseInt(st.nextToken())-1;
            int eX=Integer.parseInt(st.nextToken())-1;
            int ans=dp[eY][eX];
            if(sX-1>=0 && sY-1>=0){
                ans+=dp[sY-1][sX-1];
            }
            if(sX-1>=0){
                ans-=dp[eY][sX-1];
            }
            if(sY-1>=0){
                ans-=dp[sY-1][eX];
            }
            System.out.println(ans);
        }
    }
}
