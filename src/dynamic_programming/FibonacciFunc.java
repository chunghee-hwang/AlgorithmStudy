package src.dynamic_programming;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//https://www.acmicpc.net/problem/1003
public class FibonacciFunc {
    private static int [][]mem = new int[41][2];
    private static int[] dp(int n){
        if(n == 0) return mem[n] = new int[]{1,0};
        if(n == 1) return mem[n] = new int[]{0,1};
        if(mem[n][0] !=0 && mem[n][1]!= 0) return mem[n];
        int[] prev1 = dp(n-1);
        int[] prev2 = dp(n-2);
        return mem[n] = new int[]{prev1[0]+prev2[0], prev1[1]+prev2[1]};
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int i = 0 ; i < T; i++){
            int[] counts = dp(Integer.parseInt(br.readLine()));
            System.out.println(counts[0]+" "+counts[1]);
        }
    }
}
