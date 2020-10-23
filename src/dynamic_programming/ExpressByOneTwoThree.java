package src.dynamic_programming;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//https://www.acmicpc.net/problem/9095
public class ExpressByOneTwoThree {
    private static int[] mem = new int[12];
    private static int dp(int n) {
        if (mem[n] != 0) return mem[n];
        if (n == 1 || n == 2) return n;
        if (n == 3) return 4;
        return mem[n] = dp(n-1)+dp(n-2)+dp(n-3);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            System.out.println(dp(Integer.parseInt(br.readLine())));
        }
    }

}
