import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.StringTokenizer;

public class BOJ2479 {
    public static void main(String args[]) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        Long nums[]= new Long[n];
        StringTokenizer st= new StringTokenizer(br.readLine());
        for(int i=0;i<n;i++){
            nums[i]=Long.parseLong(st.nextToken());
        }
        Arrays.sort(nums, new Comparator<Long>() {
            @Override
            public int compare(Long o1, Long o2) {
                return (int)(Math.abs(o1)-Math.abs(o2));
            }
        });
        long ans=Long.MAX_VALUE;
        long x=0,y=0;
        for(int i=0;i<n-1;i++){
            if(Math.abs(nums[i]+nums[i+1])<ans){
                ans=Math.abs(nums[i]+nums[i+1]);
                x=nums[i];
                y=nums[i+1];
            }
        }
        if(x<y){
            System.out.println(x+" "+y);
        }
        else{
            System.out.println(y+" "+x);
        }
    }
}
