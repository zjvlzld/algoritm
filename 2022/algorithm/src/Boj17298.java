import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Boj17298
{
    static class Info {
        int num;
        int idnex;
        public Info(int a,int b){
            num=b;
            idnex=a;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(bf.readLine());
        int nums[]=new int[n];
        int ans[]=new int[n];

        StringTokenizer st=new StringTokenizer(bf.readLine());
        for(int i=0;i<n;i++){
            nums[i]=Integer.parseInt(st.nextToken());
        }
        Stack<Info> stack=new Stack<Info>();
        stack.push(new Info(0,nums[0]));
        for(int i=1;i<n;i++){
            while(!stack.isEmpty()&&stack.peek().num<nums[i]){
                ans[stack.peek().idnex]=nums[i];
                stack.pop();
            }
            stack.push(new Info(i,nums[i]));
        }
        for(int i=0;i<n;i++){
            if(ans[i]!=0)
                System.out.printf("%d ",ans[i]);
            else
                System.out.printf("-1 ");
        }
    }
}
