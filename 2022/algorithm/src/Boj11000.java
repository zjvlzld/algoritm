import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;
import java.util.Arrays;
public class Boj11000 {


    static class Class implements Comparable{
        public int start;
        public int end;
        public Class(int i, int j){
            this.start=i;
            this.end=j;
        }
        @Override
        public int compareTo(Object o){
            Class c=(Class)o;
            return this.start-c.start;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(bf.readLine());
        Class[] c = new Class[n];
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
        int ans=0;
        for(int i=0;i<n;i++){
            StringTokenizer st=new StringTokenizer(bf.readLine());
            int a=Integer.parseInt(st.nextToken());
            int b=Integer.parseInt(st.nextToken());
            c[i]=new Class(a,b);
        }
        Arrays.sort(c);
        for(int i=0;i<n;i++){
            if(pq.isEmpty()){
                ans++;
                pq.add(c[i].end);
            }
            else{
                if(pq.peek()<=c[i].start){
                    pq.poll();
                    pq.add(c[i].end);
                }
                else{
                    ans++;
                    pq.add(c[i].end);
                }
            }
        }
        System.out.println(ans);
    }

}
