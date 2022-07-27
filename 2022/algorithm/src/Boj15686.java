import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Boj15686
{
    static class Pos{

        public int x;
        public int y;
        public Pos(int y,int x){
            this.x=x;
            this.y=y;
        }
    }
    static ArrayList<Pos> chicken=new ArrayList<Pos>();
    static ArrayList<Pos> house=new ArrayList<Pos>();
    static ArrayList<Integer> arr = new ArrayList<Integer>();
    static int n;
    static int m;
    static int ans=Integer.MAX_VALUE;
    public static void cal(){
        if(arr.size()==m){
            get();
            return;
        }
        if(arr.isEmpty()){
            for(int i=0;i<chicken.size();i++){
                arr.add(i);
                cal();
                arr.remove(arr.size()-1);
            }
        }
        else{
            for(int i=arr.get(arr.size()-1)+1 ;i<chicken.size();i++){
                arr.add(i);
                cal();
                arr.remove(arr.size()-1);
            }
        }

    }

    public static void get(){
        int temp=0;
        for(Pos p : house){
            int temp2=Integer.MAX_VALUE;
            for(int now : arr)
                if(temp2>(Math.abs(chicken.get(now).x-p.x)+Math.abs(chicken.get(now).y-p.y)))
                    temp2=Math.abs(chicken.get(now).x-p.x)+Math.abs(chicken.get(now).y-p.y);
            temp+=temp2;
        }
        if(ans>temp){
            ans=temp;
        }
        if(temp<ans){
            ans=temp;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(bf.readLine());
        n=Integer.parseInt(st.nextToken());
        m=Integer.parseInt(st.nextToken());

        for(int i=0;i<n;i++){
            st=new StringTokenizer(bf.readLine());
            for(int j=0;j<n;j++){
                int t=Integer.parseInt(st.nextToken());
                if(t==1){
                    house.add(new Pos(i,j));
                }
                if(t==2){
                    chicken.add(new Pos(i,j));
                }
            }
        }
        cal();
        System.out.println(ans);
    }
}
