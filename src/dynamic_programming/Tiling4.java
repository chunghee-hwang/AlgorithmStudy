package dynamic_programming;

//https://www.acmicpc.net/problem/14852
//2×N 크기의 벽을 2×1, 1×2, 1×1 크기의 타일로 채우는 경우의 수를 구해보자.
// (1 ≤ N ≤ 1,000,000)
//경우의 수를 1,000,000,007로 나눈 나머지를 출력한다.
public class Tiling4 {

    //점화식 : D[n] = 3 * D[n-2] + 2 * D[n-1]
    // + (2*D[n-3] + 2*[n-4] *...*2*D[0])

    static int [][]d = new int[1000001][2];

    static int dp(int x){
        d[0][0] = 0;
        d[1][0] = 2;
        d[2][0] = 7;
        d[2][1] = 1;

        for(int i = 3; i <=x; i++){
            d[i][1] = (d[i-1][1] + d[i-3][0]) % 100000007;
            d[i][0] = (3*d[i-2][0] + 2*d[i-1][0] + 2*d[i][1]) % 100000007;
        }
        return d[x][0];
    }

    public static void main(String[] args) {
        int x = 4;
        System.out.println(dp(x));
    }

}
