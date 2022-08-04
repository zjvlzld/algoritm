import javax.swing.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.security.PublicKey;
import java.util.StringTokenizer;

public class BOJ17281 {
    public static int game;
    public static int[] order={0,0,0,0,0,0,0,0,0};
    public static int[] used={1,0,0,0,0,0,0,0,0};
    public static int[][] score;
    public static int ans=Integer.MIN_VALUE;
    public static void mkOrd(int d){
        if(d==9){
            simulate();
        }
        if(d==3) mkOrd(d+1);
        else{
            for(int i=0;i<9;i++){
                if(used[i]==0){
                    order[d]=i;
                    used[i]=1;
                    mkOrd(d+1);
                    used[i]=0;
                }
            }
        }
    }


    public static void simulate(){

        int nowSc=0;
        int now=0;
        int set=0;

        while(set<game){
            int out=0;
            int one=0;
            int two=0;
            int three=0;
            while(out<3){
                switch (score[set][order[now]]){
                    case 0:
                        out++;
                        break;
                    case 1:
                        nowSc+=three;
                        three=two;
                        two=one;
                        one=1;
                        break;
                    case 2:
                        nowSc+=three+two;
                        three=one;
                        two=1;
                        one=0;
                        break;
                    case 3:
                        nowSc+=three+two+one;

                        three=1;
                        two=0;
                        one=0;
                        break;
                    case 4:
                        nowSc+=three+two+one+1;
                        one=two=three=0;
                        break;
                }
                now++;
                now=now%9;
            }
            set++;
        }
        if(nowSc>ans){
            ans=nowSc;
        }
    }


    public static void main(String args[]) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        game=Integer.parseInt(br.readLine());
        score=new int[game][9];
        for(int i=0;i<game;i++){
            StringTokenizer st=new StringTokenizer(br.readLine());
            for(int j=0;j<9;j++){
                score[i][j]=Integer.parseInt(st.nextToken());
            }
        }
        mkOrd(0);
        System.out.println(ans);
    }
}
