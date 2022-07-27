import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;


public class Boj25381 {
    public static void main(String args[]) throws IOException {
        BufferedReader bf=new BufferedReader(new InputStreamReader(System.in));
        String get=bf.readLine();
        Deque<Integer> bCount=new ArrayDeque<Integer>();
        Deque<Integer> aCount=new ArrayDeque<Integer>();
        int ans=0;
        for(int i=0;i<get.length();i++){
            if(get.charAt(i)=='C'){
                if(bCount.size()>0&&bCount.getFirst()<i){//C보다 앞에 나온 b가 있을 경우
                    ans++;//C를 제거하며 ans카운트 증가
                    bCount.pollFirst();//가장 먼저 나온 B제거, (그리디)
                }
            }
            if(get.charAt(i)=='B'){
                bCount.addLast(i);//B큐에 인덱스 추가

            }
            if(get.charAt(i)=='A'){//A큐에 인덱스 추가
                aCount.addLast(i);
            }
        }
        //이렇게 되면 C를 빼고 남은 B인덱스만 B큐에 남게 된다.
        while(aCount.size()>0 && bCount.size()>0){
            if(aCount.getFirst()<bCount.getFirst()){
                ans++;
                bCount.pollFirst();
                aCount.pollFirst();
            }
            else{
                bCount.pollFirst();
            }
        }
        System.out.println(ans);
    }
}
