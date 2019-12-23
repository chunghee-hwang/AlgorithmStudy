package bfs_dfs;

import java.util.Scanner;
//https://codeup.kr/problem.php?id=2605
public class CandyPangDFS2 {
    private static final int SIZE = 7;
    private static int[][] candies = new int[SIZE][SIZE];
    private static boolean[][] visit = new boolean[SIZE][SIZE];
    private static int sameCnt = 0;

    private static void dfs(int x, int y, int color) {
        if (y < 0 || x < 0 || x >= SIZE || y >= SIZE || visit[y][x])
            return;

        if (candies[y][x] == color) {
            sameCnt++;
            visit[y][x] = true;
            dfs(x - 1, y, color);
            dfs(x + 1, y, color);
            dfs(x, y - 1, color);
            dfs(x, y + 1, color);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int y, x;
        int popCnt = 0;
        for (y = 0; y < SIZE; y++) for (x = 0; x < SIZE; x++) candies[y][x] = sc.nextInt();
        for (y = 0; y < SIZE; y++)
            for (x = 0; x < SIZE; x++)
                if (!visit[y][x]) {
                    sameCnt = 0;
                    dfs(x, y, candies[y][x]);
                    if (sameCnt >= 3) popCnt++;
                }
        System.out.println(popCnt);
    }
}
