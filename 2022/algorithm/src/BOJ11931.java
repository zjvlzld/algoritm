import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class BOJ11931 {
    public static void main(String args[]){
        StringBuilder ans=new StringBuilder("");
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int nums[]=new int[n];
        for(int i=0;i<n;i++){
            nums[i]=sc.nextInt();
        }
        Arrays.sort(nums);

        for(int i=n-1;i>=0;i--){
            ans.append(nums[i]).append("\n");
        }
        System.out.println(ans);
    }
}
