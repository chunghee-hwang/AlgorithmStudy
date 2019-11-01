package dynamic_programming;

//  https://programmers.co.kr/learn/courses/30/lessons/43104
public class Tiling5 {

    //점화식 : D[n] = D[n-1] + D[n-2]
    private long tiling(int n, long[] mem){
        if(n == 1) return 4;
        if(n == 2) return 6;
        if(mem[n] != 0) return mem[n];
        return mem[n] = tiling(n-1, mem) + tiling(n-2, mem);
    }

    public long solution(int N)
    {
        long []mem = new long[81];
        return tiling(N, mem);
    }

    public static void main(String[] args) {
        System.out.println(new Tiling5().solution(5));
    }
}
