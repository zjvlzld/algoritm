import java.io.*;
import java.util.*;
import java.util.Deque;

public class Boj25395 {

    static class info implements Comparable{
        public int index;
        public int pos;
        public int fuel;

        @Override
        public int compareTo(Object o) {
            info temp=(info)o;
            return pos-temp.pos;
        }
    }

    public static void main(String args[]) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());
        info[] arr = new info[N];
        st = new StringTokenizer(bf.readLine());

        for (int i = 0; i < N; i++) {
            arr[i] = new info();
            arr[i].pos = Integer.parseInt(st.nextToken());
            arr[i].index = i + 1;
        }
        st = new StringTokenizer(bf.readLine());
        for (int i = 0; i < N; i++) {
            arr[i].fuel = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);
        int start = 0;
        for (int i = 0; i < N; i++) {
            if (arr[i].index == S) {
                start = i;
            }
        }
        int[] visit = new int[N+1];
        Deque<Integer> que = new ArrayDeque<>();
        que.addLast(start);
        visit[arr[start].index]=1;
        while(que.size()!=0){
            int now=que.pollFirst();
            for(int i=now;i>=0;i--){
                if(arr[i].pos<arr[now].pos-arr[now].fuel){
                    break;
                }
                if(visit[arr[i].index]==0){
                    que.addLast(i);
                    visit[arr[i].index]=1;
                }
            }
            for(int i=now;i<N;i++){
                if(arr[i].pos>arr[now].pos+arr[now].fuel){
                    break;
                }
                if(visit[arr[i].index]==0){
                    que.addLast(i);
                    visit[arr[i].index]=1;
                }
            }
        }
        StringBuilder ans=new StringBuilder();
        for(int i=1;i<N+1;i++){
            if(visit[i]==1){
                ans.append(i).append(" ");
            }
        }
        System.out.println(ans);
    }
}
