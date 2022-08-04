import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ17135 {
    public static int X;
    public static int Y;
    public static int D;
    public static int[][] map;
    public static int[][] get;

    public static int[] order=new int[3];
    public static int ans=Integer.MIN_VALUE;

    public static int[] kill(){
        int x1=-1,y1=-1,distance1=Integer.MAX_VALUE;
        int x2=-1,y2=-1,distance2=Integer.MAX_VALUE;
        int x3=-1,y3=-1,distance3=Integer.MAX_VALUE;
        for(int j=0;j<X;j++){
            for(int i=0;i<Y;i++){
                if(map[i][j]==1){
                    if(Math.abs(order[0]-j)+Y-i<distance1){
                        x1=j;
                        y1=i;
                        distance1=Math.abs(order[0]-j)+Y-i;
                    }

                    if(Math.abs(order[1]-j)+Y-i<distance2){
                        x2=j;
                        y2=i;
                        distance2=Math.abs(order[1]-j)+Y-i;
                    }


                    if(Math.abs(order[2]-j)+Y-i<distance3){
                        x3=j;
                        y3=i;
                        distance3=Math.abs(order[2]-j)+Y-i;
                    }

                }
            }
        }
        //System.out.println(y1+" "+x1+" "+distance1+" "+y2+" "+x2+" "+distance2+" "+y3+" "+x3+" "+distance3);
        int ret[]=new int[6];

        if(distance1<=D){
            ret[0]=y1;
            ret[1]=x1;
        }
        else{
            ret[0]=-1;
            ret[1]=-1;
        }

        if(distance2<=D){
            ret[2]=y2;
            ret[3]=x2;
        }
        else{
            ret[2]=-1;
            ret[3]=-1;
        }

        if(distance3<=D){
            ret[4]=y3;
            ret[5]=x3;
        }
        else{
            ret[4]=-1;
            ret[5]=-1;
        }
        return ret;
    }
    public static void simulate(){


        int count=-1;
        int nowAns=0;
        while(count!=0){
/*
            for(int[] i : map){
                for(int j:i){
                    System.out.print(j+" ");
                }
                System.out.println();
            }
            System.out.println();
*/
            int nums[]=kill();
/*
            for(int i:nums){
                System.out.print(i+" ");
            }
            System.out.println();
*/
            if(nums[0]>-1){
                map[nums[0]][nums[1]]=10;
            }
            if(nums[2]>-1){
                map[nums[2]][nums[3]]=10;
            }
            if(nums[4]>-1){
                map[nums[4]][nums[5]]=10;
            }

            count=0;
            for(int i=0;i<Y;i++){
                for(int j=0;j<X;j++){
                    if(map[i][j]==10){
                        nowAns++;
                        map[i][j]=0;
                    }
                }
            }

            for(int i=Y-1;i>0;i--){
                for(int j=0;j<X;j++){
                    map[i][j]=map[i-1][j];
                    if(map[i][j]==1){
                        count++;
                    }
                }
            }
            for(int j=0;j<X;j++){
                map[0][j]=0;
            }
        }
        if(nowAns>ans){
            ans=nowAns;
        }
    }
    public static void mkOrd(int d){
        if(d==0){
            for(int i=0;i<X;i++){
                order[d]=i;
                mkOrd(d+1);
            }
        }
        else{
            if(d==3){
//                System.out.println(order[0]+" "+order[1]+" "+order[2]+" ");
                for(int i=0;i<Y;i++){
                    for(int j=0;j<X;j++){
                        map[i][j]=get[i][j];
                    }
                }
                simulate();
                return;
            }
            for(int i=order[d-1]+1;i<X;i++){
                order[d]=i;
                mkOrd(d+1);
            }
        }
    }
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());
        Y=Integer.parseInt(st.nextToken());
        X=Integer.parseInt(st.nextToken());
        D=Integer.parseInt(st.nextToken());
        map=new int[Y][X];
        get=new int[Y][X];

        for(int i=0;i<Y;i++){
            st=new StringTokenizer(br.readLine());
            for(int j=0;j<X;j++){
                get[i][j]=Integer.parseInt(st.nextToken());
            }
        }
        mkOrd(0);
        System.out.println(ans);
    }

}
