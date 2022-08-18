import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ17471 {
    public static int N;
    public static int[] human;
    public static List<List<Integer>> map=new ArrayList<>();
    public static int bfs(List<Integer> arr){
        int [] visit=new int[N+1];
        int sum=0;
        Deque<Integer> que=new ArrayDeque<>();
        for(int i:arr){
            visit[i]=1;
        }
        /*
        for(int i:visit){
            System.out.print(i+" ");
        }
        System.out.println();
        */
        visit[arr.get(0)]=0;
        sum+=human[arr.get(0)];
        que.addLast(arr.get(0));
        while(que.size()!=0){
            int now=que.pollFirst();
            for(int i:map.get(now)){
                if(visit[i]==1){
                    visit[i]=0;
                    sum+=human[i];
                    que.addLast(i);
                }
            }
        }
        /*
        for(int i:visit){
            System.out.print(i+" ");
        }
        System.out.println();
        */
        for(int i:arr){
            if(visit[i]!=0){
                return -1;
            }
        }



        return sum;
    }

    public static void main(String ...asdf) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        N=Integer.parseInt(br.readLine());
        human=new int[N+1];
        int ans=Integer.MAX_VALUE;
        StringTokenizer st=new StringTokenizer(br.readLine());
        map.add(new ArrayList<>());
        for(int i=1;i<N+1;i++){
            human[i]=Integer.parseInt(st.nextToken());
            map.add(new ArrayList<>());
        }
        for(int i=1;i<N+1;i++){
            st=new StringTokenizer(br.readLine());
            int m=Integer.parseInt(st.nextToken());
            for(int j=0;j<m;j++){
                map.get(i).add(Integer.parseInt(st.nextToken()));
            }
        }

        /*for(List<Integer> i:map){
            for(int j:i){
                System.out.print(j+" ");
            }
            System.out.println();
        }*/
        for(int i=1;i<Math.pow(2,N)-1;i++) {
            List<Integer> group1 = new ArrayList<Integer>();
            List<Integer> group2 = new ArrayList<Integer>();
            for (int j = 0; j < N; j++) {
                if ((i & 1 << j) > 0) {
                    group1.add(j + 1);
                } else group2.add(j + 1);
            }

/*            if(i==9) {
            for(int k:group1){
                System.out.print(k+" ");
            }
            System.out.println();
            for(int k:group2){
                System.out.print(k+" ");
            }
            System.out.println();
*/

            int g1 = bfs(group1);
            int g2 = bfs(group2);
            //System.out.println(g1 + " " + g2);
            if (g1 > 0 && g2 > 0) {
                ans = Math.min(ans, Math.abs(g1 - g2));
            }

        }
        if(ans==Integer.MAX_VALUE){
            System.out.println(-1);
        }
        else{
            System.out.println(ans);
        }
    }
}
