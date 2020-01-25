package dynamic_programming;
//https://programmers.co.kr/learn/courses/30/lessons/12900
public class TwoByNTiling {
    private static int[] mem;
    private static int dp(int n){
        if(mem[n] != 0) return mem[n];
        if(n == 1 || n == 2)return n;
        return mem[n] = (dp(n-1) + dp(n-2))%1000000007;
    }
    public static int solution(int n) {
        mem = new int[n+1];
        return dp(n);
    }
    public static void main(String[] args) {
        int n = 4;
        solution(4);
    }
}
