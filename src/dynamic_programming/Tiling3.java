package dynamic_programming;

//https://www.acmicpc.net/problem/2133
//3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.
// (1 ≤ N ≤ 30)
public class Tiling3 {

    //점화식 : D[n] = 3 * D[n-2] + (2*D[n-4] + 2*[n-6] *...*2*D[0])

    static int []d = new int[1001];

    static int dp(int x){
        if(x == 0) return 1;
        if(x == 1) return 0;
        if(x == 2) return 3;
        if(d[x] != 0) return d[x];
        int result = 3 * dp(x-2);
        for(int i = 4; i <=x; i++){
            if(i%2 == 0)
                result += 2 * dp(x-i);
        }
        return d[x] = result;
    }

    public static void main(String[] args) {
        int x = 2;
        System.out.println(dp(x));
    }

}
