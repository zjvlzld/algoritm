import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ17406 {
    static int Y;
    static int X;
    static int C;
    static int[][] origin;
    static int[][] map;
    static int[][] order;
    static int order2[];
    static int used[];
    static int ans=Integer.MAX_VALUE;

    public static int getAns(){//최종 형태에서 배열 값 구하는 함수
        int ret=Integer.MAX_VALUE;
        for(int i=0;i<Y;i++){
            int temp=0;
            for(int j=0;j<X;j++){
                temp+=map[i][j];
            }
            if(temp<ret){
                ret=temp;
            }
        }
        return ret;
    }
    public static void mkOrder(int d){//순열 만드는 함수
        if(d==order2.length){//순열이 완성되면
            for(int i=0;i<Y;i++){
                for(int j=0;j<X;j++){
                    map[i][j]=origin[i][j];
                }
            }
            for(int i=0;i<d;i++){//순열대로
                //배열을 회전시킨다(order2가 순열)
                rotate(order[order2[i]][0]-order[order2[i]][2]-1,order[order2[i]][1]-order[order2[i]][2]-1,order[order2[i]][0]+order[order2[i]][2]-1,order[order2[i]][1]+order[order2[i]][2]-1);
            }
            int t=getAns();
            if(ans>t){
                ans=t;
            }
        }
        for(int i=0;i<C;i++){//순열 만들기
            if(used[i]==0){
                order2[d]=i;
                used[i]=1;
                mkOrder(d+1);
                used[i]=0;
            }
        }

    }
    public static void rotate(int sY,int sX,int eY,int eX){//회전시키기
        if(sX>eX){
            return;
        }
        int arr[]=new int[4*(eX-sX)];//순서대로 쫙 넣어줄 변수
        int p=0;
        //순서대로 쫙 넣어준 다음에
        for(int i=sX;i<eX;i++){
            arr[p++]=map[sY][i];
        }
        for(int i=sY;i<eY;i++){
            arr[p++]=map[i][eX];
        }
        for(int i=eX;i>sX;i--){
            arr[p++]=map[eY][i];
        }
        for(int i=eY;i>sY;i--){
            arr[p++]=map[i][sX];
        }
        //한칸씩 미뤄서 순서대로 쭉 뺴준다
        p=0;
        for(int i=sX+1;i<=eX;i++){
            map[sY][i]=arr[p++];
        }
        for(int i=sY+1;i<=eY;i++){
            map[i][eX]=arr[p++];
        }
        for(int i=eX-1;i>=sX;i--){
            map[eY][i]=arr[p++];
        }
        for(int i=eY-1;i>=sY;i--){
            map[i][sX]=arr[p++];
        }
        rotate(sY+1, sX+1, eY-1, eX-1);
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        Y=Integer.parseInt(st.nextToken());
        X=Integer.parseInt(st.nextToken());
        C=Integer.parseInt(st.nextToken());
        map=new int[Y][X];
        origin=new int[Y][X];

        for(int i=0;i<Y;i++){
            st=new StringTokenizer(br.readLine());
            for(int j=0;j<X;j++){
                origin[i][j]=Integer.parseInt(st.nextToken());
            }
        }
        order=new int[C][3];
        order2=new int[C];
        used=new int[C];
        for(int i=0;i<C;i++){
            st=new StringTokenizer(br.readLine());
            order[i][0]=Integer.parseInt(st.nextToken());
            order[i][1]=Integer.parseInt(st.nextToken());
            order[i][2]=Integer.parseInt(st.nextToken());
        }
        mkOrder(0);
        System.out.println(ans);
    }
}
