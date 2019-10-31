package dynamic_programming;

//https://www.acmicpc.net/problem/11727
//2×n 직사각형을 2×1과 2×2 타일로 채우는 방법의 수를
// 구하는 프로그램을 작성하시오.
//방법의 수를 10,007로 나눈 나머지를 출력한다.
// (1 ≤ n ≤ 1,000)
public class Tiling2 {

    //점화식 : D[n] = D[n-1] + 2 * D[n-2]

    static int []d = new int[1001];

    static int dp(int x){
        if(x == 1) return 1;
        if(x == 2) return 3;
        if(d[x] != 0) return d[x];
        return d[x] = (dp(x-1) + 2*dp(x-2)) % 10007;
    }

    public static void main(String[] args) {
        int x = 10;
        System.out.println(dp(x));
    }

}
