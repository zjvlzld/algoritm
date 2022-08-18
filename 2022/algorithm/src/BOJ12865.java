import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class BOJ12865 {
    static int N;
    static int K;
    static int[][] stuff;
    static int[][] dp;
    static int ans=0;

    public static void main(String args[]) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken());
        K=Integer.parseInt(st.nextToken());
        stuff=new int[N][2];
        dp=new int[N][K+1];
        for(int i=0;i<N;i++){
            st=new StringTokenizer(br.readLine());
            stuff[i][0]=Integer.parseInt(st.nextToken());
            stuff[i][1]=Integer.parseInt(st.nextToken());
        }
        Arrays.sort(stuff, (( o1, o2)->{//람다식
            if(o1[0]-o2[0]!=0){
                return o1[0]-o2[0];
            }
            return o2[1]-o1[1];
        }));
        if(stuff[0][0]<=K) {
            dp[0][stuff[0][0]] = stuff[0][1];
            ans =stuff[0][1];
        }
        for(int i=1;i<N;i++){
            if(stuff[i][0]<=K) {
                dp[i][stuff[i][0]] = stuff[i][1];
                if (dp[i][stuff[i][0]] < dp[i - 1][stuff[i][0]]) {
                    dp[i][stuff[i][0]] = dp[i - 1][stuff[i][0]];
                }
                if (ans < dp[i][stuff[i][0]]) {
                    ans = dp[i][stuff[i][0]];
                }
            }
            for(int j=1;j<K+1;j++){
                if(dp[i-1][j]!=0){
                    if(j+stuff[i][0]<=K){
                        dp[i][j+stuff[i][0]]=dp[i-1][j]+stuff[i][1];
                        if(dp[i][j+stuff[i][0]]<dp[i-1][j+stuff[i][0]]){
                            dp[i][j+stuff[i][0]]=dp[i-1][j+stuff[i][0]];
                        }
                        if(ans<dp[i][j+stuff[i][0]]){
                            ans=dp[i][j+stuff[i][0]];
                        }
                    }
                }
            }
            for(int j=1;j<K+1;j++){
                if(dp[i][j]<dp[i-1][j]){
                    dp[i][j]=dp[i-1][j];
                }
            }
        }/*
        for(int[] i:dp){
            for(int j:i){
                System.out.print(j+" ");
            }
            System.out.println();
        }*/
        System.out.println(ans);
    }
}
