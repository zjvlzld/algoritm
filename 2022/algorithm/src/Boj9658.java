import java.util.Scanner;

public class Boj9658 {
    public static void main(String args[]){
        int n= new Scanner(System.in).nextInt();
        if(n%7==1||n%7==3){
            System.out.println("CY");
        }
        else{
            System.out.println("SK");
        }
    }
}
