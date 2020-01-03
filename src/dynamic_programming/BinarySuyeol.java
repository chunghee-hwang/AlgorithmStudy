package dynamic_programming;

import java.util.Scanner;

// https://www.acmicpc.net/problem/1904
public class BinarySuyeol {

    /*
    n : 1
    1
    1가지

    n:2
    11
    00
    2가지

    n:3

    111
    001
    100
    3가지

    n:4
    0000
    0011
    1100
    1001
    1111
    5가지

     */

    private static int mem[] = new int[1000001];
    private static int dp(int n){
        if(n == 1)
            return 1;
        if(n == 2)
            return 2;
        if(mem[n-2] == 0)
            mem[n-2] = dp(n-2);
        if(mem[n-1] == 0)
            mem[n-1] = dp(n-1);
        return (mem[n-2] + mem[n-1]) % 15746;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(dp(n));
    }

}
