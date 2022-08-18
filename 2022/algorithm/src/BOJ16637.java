import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ16637 {
    static int n;
    static String get;
    static int ans=Integer.MIN_VALUE;
    public static void get(int now,int top) {
        if(now==n-1){
            if(get.charAt(now-1)=='+'){
                top+=(int)get.charAt(now)-(int)'0';
            }
            if(get.charAt(now-1)=='-'){
                top-=(int)get.charAt(now)-(int)'0';
            }
            if(get.charAt(now-1)=='*'){
                top*=(int)get.charAt(now)-(int)'0';
            }
            ans=Math.max(ans,top);
            return;
        }
        int n1=-1,n2=-1;
        if(get.charAt(now-1)=='+'){
            n1=(top+((int)get.charAt(now)-(int)'0'));
            if(get.charAt(now+1)=='+'){
                n2=top+(((int)get.charAt(now)-(int)'0')+((int)get.charAt(now+2)-(int)'0'));

            }
            if(get.charAt(now+1)=='-'){
                n2=top+(((int)get.charAt(now)-(int)'0')-((int)get.charAt(now+2)-(int)'0'));

            }
            if(get.charAt(now+1)=='*'){
                n2=top+(((int)get.charAt(now)-(int)'0')*((int)get.charAt(now+2)-(int)'0'));

            }
        }
        if(get.charAt(now-1)=='-'){
            n1=top-((int)get.charAt(now)-(int)'0');
            if(get.charAt(now+1)=='+'){
                n2=top-(((int)get.charAt(now)-(int)'0')+((int)get.charAt(now+2)-(int)'0'));

            }
            if(get.charAt(now+1)=='-'){
                n2=top-(((int)get.charAt(now)-(int)'0')-((int)get.charAt(now+2)-(int)'0'));
            }
            if(get.charAt(now+1)=='*'){
                n2=top-(((int)get.charAt(now)-(int)'0')*((int)get.charAt(now+2)-(int)'0'));

            }
        }
        if(get.charAt(now-1)=='*'){
            n1=(top*((int)get.charAt(now)-(int)'0'));

            if(get.charAt(now+1)=='+'){
                n2=top*(((int)get.charAt(now)-(int)'0')+((int)get.charAt(now+2)-(int)'0'));

            }
            if(get.charAt(now+1)=='-'){
                n2=top*(((int)get.charAt(now)-(int)'0')-((int)get.charAt(now+2)-(int)'0'));
            }
            if(get.charAt(now+1)=='*'){
                n2=top*(((int)get.charAt(now)-(int)'0')*((int)get.charAt(now+2)-(int)'0'));
            }

        }
        if(now==n-3){
            ans=Math.max(ans,n2);
            get(now+2,n1);

            return;
        }
        get(now+2,n1);
        get(now+4,n2);

    }

    public static void main(String ...asdfa) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        n=Integer.parseInt(br.readLine());
        get=br.readLine();
        if(n==1){
            System.out.println(get);
            return;
        }
        if(n==3){
            if(get.charAt(1)=='+') System.out.println((get.charAt(0)-(int)'0')+(get.charAt(2)-(int)'0'));
            if(get.charAt(1)=='-') System.out.println((get.charAt(0)-(int)'0')-(get.charAt(2)-(int)'0'));
            if(get.charAt(1)=='*') System.out.println((get.charAt(0)-(int)'0')*(get.charAt(2)-(int)'0'));
            return;
        }
        get(2,(int)get.charAt(0)-(int)'0');
        System.out.println(ans);
    }
}
