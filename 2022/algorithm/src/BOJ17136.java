import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ17136 {
    public static int map[][]=new int[10][10];
    public static int ans=Integer.MAX_VALUE;
    public static int nowCount=0;
    public static int[] count=new int[6];

    public static void fill(int y,int x, int l,int digit){
        for(int i=0;i<l;i++){
            for(int j=0;j<l;j++){
                map[y+i][x+j]=digit;
            }
        }
    }
    public static boolean check(int y,int x,int l){
        for(int i=0;i<l;i++){
            for(int j=0;j<l;j++){
                if(y+i>9||x+j>9||map[y+i][x+j]!=1){
                    return false;
                }
            }
        }
        return true;
    }
    public static void cal(int y,int x){
        if(count[1]+count[2]+count[3]+count[4]+count[5]>ans){
            return;
        }
        if(count[1]>5||count[2]>5||count[3]>5||count[4]>5||count[5]>5)
        {
            return;
        }
        if (x == 10) {
            cal(y+1,0);
            return;
        }
        if(y==10){
            if(ans>count[1]+count[2]+count[3]+count[4]+count[5]){
                ans=count[1]+count[2]+count[3]+count[4]+count[5];
            }
            return;
        }
        if(map[y][x]==0){
            cal(y,x+1);
        }
        for(int c=5;c>0;c--){
            if(check(y,x,c)){
                fill(y,x,c,0);
                count[c]++;
                cal(y,x+1);
                count[c]--;
                fill(y,x,c,1);
            }
        }
    }
    public static void main(String ttt[]) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        for(int i=0;i<10;i++){
            StringTokenizer st=new StringTokenizer(br.readLine());
            for(int j=0;j<10;j++){
                map[i][j]=Integer.parseInt(st.nextToken());
            }
        }
        cal(0,0);
        if(ans!=Integer.MAX_VALUE) {
            System.out.println(ans);
        }
        else{
            System.out.println(-1);
        }
    }
}
