import java.util.Arrays;
import java.util.Scanner;

public class BOJ11650 {
    static class Info implements Comparable<Info> {
        public int x;
        public int y;
        public Info(int a,int b){
            x=a;
            y=b;
        }
        @Override
        public  int compareTo(Info o) {
            if(this.x-o.x!=0){
                return this.x-o.x;
            }
            return this.y-o.y;
        }

        @Override
        public String toString() {
            return this.x+" "+this.y+"\n";
        }
    }
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        StringBuilder ans=new StringBuilder("");
        int n=sc.nextInt();
        Info[] nums=new Info[n];
        for(int i=0;i<n;i++){
            nums[i]=new Info(sc.nextInt(),sc.nextInt());
        }
        Arrays.sort(nums);
        for(Info i : nums) {
            ans.append(i.toString());
        }
        System.out.println(ans);
    }
}
