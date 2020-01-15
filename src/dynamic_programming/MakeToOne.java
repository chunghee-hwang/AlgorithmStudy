package dynamic_programming;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//https://www.acmicpc.net/problem/1463

public class MakeToOne {
    static int mem[] = new int[1000001];
    static int dp(int x) {
        if (x == 1) return 0;
        if (x >= 2 && x <= 3) return 1;
        if (mem[x] != 0) return mem[x];
        int div3 = x % 3;
        boolean div2 = ((x >> 1) << 1) == x;
        if (!div2 && div3 != 0)
            return mem[x] = dp(x - 1) + 1;
        else if (div3 == 0)
            return mem[x] = Math.min(dp(x / 3), dp(x - 1)) + 1;
        else //div2 == 0
            return mem[x] = Math.min(dp(x / 2), dp(x - 1)) + 1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println(dp(Integer.parseInt(br.readLine())));
    }
}
