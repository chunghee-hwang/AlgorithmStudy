package dynamic_programming;
//https://codeup.kr/problem.php?id=2640
import java.util.Scanner;

public class PowerOfN {
    static final long div = 1000000007;
    static long power(int n, int k){
        if(k == 0)
            return 1;
        long temp = power(n, k/2);
        long result = temp * temp % div;
        if(k%2 != 0)
            result = result * n % div;
        return result;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        System.out.println(power(n, k));
    }

    // 10 5 2 1
}
