import java.io.*;
import java.util.StringTokenizer;

public class Boj25287 {

    public static void main(String[] args) throws IOException {
        BufferedReader bw = new BufferedReader(new InputStreamReader(System.in));
        int T=Integer.parseInt(bw.readLine());
        StringBuilder ans=new StringBuilder();
        for(int test=0;test<T;test++){
            int n=Integer.parseInt(bw.readLine());
            String put="YES\n";
            StringTokenizer st=new StringTokenizer(bw.readLine());
            if(n==1){
                ans.append(put);
                continue;
            }
            int[] nums=new int[n];
            nums[0]=Integer.parseInt(st.nextToken());
            if(nums[0]>n-nums[0]+1){
                nums[0]=n-nums[0]+1;
            }
            for(int i=1;i<n;i++){
                nums[i]=Integer.parseInt(st.nextToken());
                int small,big;
                if(nums[i]<n-nums[i]+1){
                    small=nums[i];
                    big=n-nums[i]+1;
                }
                else{
                    big=nums[i];
                    small=n-nums[i]+1;
                }
                if(small<nums[i-1]){
                    nums[i]=big;
                }
                else{
                    nums[i]=small;
                }
                if(nums[i]<nums[i-1]){
                    put="NO\n";
                    break;
                }
            }
            ans.append(put);
        }
        System.out.println(ans);
   }
}