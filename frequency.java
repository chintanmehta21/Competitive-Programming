//Q6 - Check the frequency of a character in a String
import java.util.Scanner;

public class frequency {
    public static void main(String[] args) {
        String s="this is java program";
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter Character:");
        char ch=sc.next().charAt(0);
        int f=0;
        for(int i = 0; i < s.length(); i++) {
            if(ch == s.charAt(i)) {
                f++;
            }
        }

        System.out.println("Frequency of " + ch + " = " + f);
    }
}