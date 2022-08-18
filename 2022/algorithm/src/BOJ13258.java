import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ13258 {
    public static void main(String ...asdf) throws IOException {
        BufferedReader br=new  BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        StringTokenizer st=new StringTokenizer(br.readLine());
        int nums[]=new int[n];
        for(int i=0;i<n;i++){
            nums[i]=Integer.parseInt(st.nextToken());
        }
        st=new StringTokenizer(br.readLine());
        int a=Integer.parseInt(st.nextToken());
        int b=Integer.parseInt(st.nextToken());
        long ans=0;
        for(int i=0;i<n;i++){
            ans+=(long)1;
            nums[i]-=(long)a;
            if(nums[i]<=0) continue;
            if(nums[i]%b != 0) ans++;
            ans+=(long)nums[i]/b;
        }
        System.out.println(ans);
    }

}
