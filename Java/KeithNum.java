/*
 * A Keith Number is an integer N with ‘d’ digits with the following property. It is a
Fibonacci like sequence (in which each term in the sequence is the sum of the ‘d’
previous terms) where first is formed, with the first ‘d’ terms being the decimal digits
of the number N, then N itself occurs as a term in the sequence. 
 */
import java.util.Scanner;
public class KeithNum
 {
    public static void main(String[] args) 
    {
        Scanner sc= new Scanner(System.in);
        System.out.print("Please enter a number: ");
        String in= sc.nextLine();
        if (in.length() > 1 && isKeithNumber(in))
            System.out.println(in + " is a Keith number!");
         else 
            System.out.println(in + " is NOT a Keith number!");
    }
    static boolean isKeithNumber(String in) 
    {
        int len = in.length();
        int s[] = new int[len];
        for (int i = 0; i < len; i++) 
            s[i] = Integer.valueOf(in.substring(i, i + 1));
        int next = 0;
        int number = Integer.valueOf(in);
        while (next < number) 
        {
            next = 0;
            for (int i = 0; i < len; i++) 
            {
                next += s[i];
                if (i < len - 1) 
                {
                    s[i] = s[i + 1];
                } else 
                {
                    s[i] = next; // add new value to the series
                }
            }
            if (next == number) 
            {
                return true;
            }
        }
        return false;
    }
}
/* OUTPUT
 * Please enter a number: 197
197 is a Keith number!

 */
