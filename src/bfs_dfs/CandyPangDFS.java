package bfs_dfs;

import java.util.Scanner;
import java.util.function.BiPredicate;
//https://codeup.kr/problem.php?id=2605
public class CandyPangDFS {
    private static final int SIZE = 7;
    private static int[][] candies = new int[SIZE][SIZE];
    private static boolean[][] visit = new boolean[SIZE][SIZE];

    private static int dfs(int x, int y) {
        int sameCnt = 1;

        if (visit[y][x]) return 0;
        visit[y][x] = true;
        int dx = x-1, dy = y;
        final BiPredicate<Integer, Integer> isSameColor = (a, b)-> !visit[b][a] && candies[y][x] == candies[b][a];
        //left
        if (dx >= 0 && isSameColor.test(dx, dy)) {
            sameCnt+=dfs(dx, dy);
        }
        //top
        dx = x; dy = y-1;
        if (dy >= 0 && isSameColor.test(dx,dy)) {
            sameCnt+=dfs(dx, dy);
        }
        //right
        dx = x+1; dy = y;
        if (dx < SIZE && isSameColor.test(dx,dy)) {
            sameCnt+=dfs(dx, dy);
        }
        //bot
        dx = x; dy = y+1;
        if (dy < SIZE && isSameColor.test(dx,dy)) {
            sameCnt+=dfs(dx, dy);
        }
        return sameCnt;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int y, x;
        int popCnt = 0;
        for (y = 0; y < SIZE; y++) for (x = 0; x < SIZE; x++) candies[y][x] = sc.nextInt();
        for (y = 0; y < SIZE; y++)
            for (x = 0; x < SIZE; x++)
                if(!visit[y][x] && dfs(x,y) >= 3) popCnt++;
        System.out.println(popCnt);
    }
}
