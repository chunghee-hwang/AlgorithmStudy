package dynamic_programming;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
/*
https://codeup.kr/problem.php?id=3703
 */
public class GetCandy {
    private static int[][] map;
    private static int[][] mem;
    private static int n, m;
    private static int dp(int y, int x) {
        if (mem[y][x] != 0)
            return mem[y][x];
        boolean yCheck = y + 1 < n;
        boolean xCheck = x + 1 < m;
        int down = -1;
        int right = -1;
        if (yCheck) {
            down = map[y][x]+dp(y + 1, x);
        }
        if (xCheck) {
            right = map[y][x]+dp(y, x + 1);
        }
        if (!yCheck && !xCheck)
        {
            return mem[y][x] = map[y][x];
        }
        return mem[y][x] = Math.max(down, right);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        map = new int[n][m];
        mem = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        dp(0, 0);
        System.out.println(mem[0][0]);
    }
}
