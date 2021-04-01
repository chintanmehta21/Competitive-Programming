//Q5 - Check if a particular String is present in an array of Strings or not
import java.util.Scanner;

public class searchstring {
    public static void main(String[] args) {
        String a[]={"ABC","XYZ","PQR","LMN"};
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter String which you want to search:");
        String k=sc.next();
        int i;
        for(i=0;i<a.length;i++)
        {
            if(a[i].equals(k))
            {
                System.out.println("String found at "+(i+1) );
                break;
            }
           
        }
        if(i==a.length)
        {
            System.out.println("String not found");
        }
    }
}