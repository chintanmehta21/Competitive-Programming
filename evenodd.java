//Q3 - Find the number of Even elements and number of Odd elements
import java.util.Scanner;

public class evenodd {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter size of array:");
        int n=sc.nextInt();
        int a[]=new int[n];
        for(int i=0;i<n;i++)
        {
            System.out.print("Enter Element:");
            a[i]=sc.nextInt();
        }
        int ce=0,co=0;
        for(int i=0;i<n;i++)
        {
            if((a[i])%2==0)   
            {
                ce++;
            }
            else
            {
                co++;
            }
        }
        System.out.println("No of Even elements in array:"+ce);
        System.out.println("No of Odd elements in array:"+co);
    }
}