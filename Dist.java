//Q10 - Convert a Distance entered in inches to Feet
import java.util.Scanner;
class Distance
{
    float inches,feet;
    void accept()
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter distance in inches:");
        inches=sc.nextFloat();
        feet=inches/12;
    }
}
public class Dist {
    public static void main(String[] args) {
        Distance d1=new Distance();
        Distance d2=new Distance();
        d1.accept();
        d2.accept();
        float d3=d1.inches+d2.inches;
        System.out.println("Distance:"+d3+" inches");
        System.out.println("Distance:"+d3/12+" feet");
    }
}