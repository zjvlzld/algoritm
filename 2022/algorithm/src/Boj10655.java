import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Boj10655 {
    public static void main(String args[]) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        int [][] pos =new int[n][2];
        int ans=0;
        int max=0;
        StringTokenizer st=new StringTokenizer(br.readLine());
        pos[0][0]=Integer.parseInt(st.nextToken());
        pos[0][1]=Integer.parseInt(st.nextToken());
        for(int i=1;i<n;i++){
            st=new StringTokenizer(br.readLine());
            pos[i][0]=Integer.parseInt(st.nextToken());
            pos[i][1]=Integer.parseInt(st.nextToken());
            ans+=Math.abs(pos[i][0]-pos[i-1][0])+Math.abs(pos[i][1]-pos[i-1][1]);
        }
        for(int i=1;i<n-1;i++){
            int temp= Math.abs(pos[i][0]-pos[i-1][0])+Math.abs(pos[i][1]-pos[i-1][1])+Math.abs(pos[i][0]-pos[i+1][0])+Math.abs(pos[i][1]-pos[i+1][1])-Math.abs(pos[i-1][0]-pos[i+1][0])-Math.abs(pos[i-1][1]-pos[i+1][1]);
            if(max<temp){
                max=temp;
            }
        }
        System.out.println(ans-max);
    }
}
