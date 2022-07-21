import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Stack;


public class Boj2494 {
    public static class info{
        static public int index;
        static public int height;

        public info(int i, int parseInt) {
            index=i;
            height=parseInt;
        }

    }
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(bf.readLine());
        StringTokenizer st=new StringTokenizer(bf.readLine()," ");
        Stack<info> stack=new Stack<info>();
        int size=0;
        stack.push(new info(1,Integer.parseInt(st.nextToken()) ) );
        System.out.printf("0 ");
        for(int i=1;i<n;i++){
            int get=Integer.parseInt(st.nextToken());
            while(!stack.empty() && stack.peek().height<get){
                stack.pop();
            }
            if(stack.empty()){
                System.out.printf("0 ");
            }
            else{
                System.out.printf("%d ",stack.peek().index);
            }
            stack.push(new info(i+1,get));
        }
    }
}
