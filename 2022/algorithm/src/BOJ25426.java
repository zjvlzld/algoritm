import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class BOJ25426 {
    public static void main(String args[]) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        long nums[]=new long[n];
        long tempAns=0;
        for(int i=0;i<n;i++){
            StringTokenizer st=new StringTokenizer(br.readLine());
            nums[i]=Integer.parseInt(st.nextToken());
            tempAns+=Long.parseLong(st.nextToken());
        }
        Arrays.sort(nums);
        for(int i=0;i<n;i++){
            long t=nums[i]*(i+1);
            tempAns+=t;
        }
        System.out.println(tempAns);
    }
}
