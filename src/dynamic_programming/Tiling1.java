package dynamic_programming;

//https://www.acmicpc.net/problem/11726
//2×n 크기의 직사각형을 1×2, 2×1
// 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
//방법의 수를 10,007로 나눈 나머지를 출력한다.
// (1 ≤ n ≤ 1,000)
public class Tiling1 {

    //점화식 : D[n] = D[n-1] + D[n-2]

    static int []d = new int[1001];

    static int dp(int x){
        if(x == 1) return 1;
        if(x == 2) return 2;
        if(d[x] != 0) return d[x];
        return d[x] = (dp(x-1) + dp(x-2)) % 10007;
    }

    public static void main(String[] args) {
        int x = 4;
        System.out.println(dp(x));
    }

}
