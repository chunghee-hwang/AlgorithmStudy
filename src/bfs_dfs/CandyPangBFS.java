package src.bfs_dfs;

import java.awt.*;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.function.BiPredicate;
//https://codeup.kr/problem.php?id=2605
public class CandyPangBFS {
    private static final int SIZE = 7;
    private static int[][] candies = new int[SIZE][SIZE];
    private static boolean[][] visit = new boolean[SIZE][SIZE];

    static Queue<Point> q = new LinkedList<>();

    private static int addQueueIfSameColor(Point current, Point... points) {
        int sameColorCnt = 0;
        final BiPredicate<Integer, Integer> isSameColor = (x, y) -> x >= 0 && x <= 6 && y >= 0 && y <= 6 &&
                candies[current.y][current.x] == candies[y][x];
        int x, y;
        for (Point point : points) {
            x = point.x;
            y = point.y;
            if (isSameColor.test(x, y) && !visit[y][x]) {
                q.add(point);
                sameColorCnt++;
            }
        }
        return sameColorCnt;
    }

    private static boolean bfs(int x, int y) {
        q.add(new Point(x, y));
        int sameColorCnt = 1;
        while (!q.isEmpty()) {
            Point current = q.remove();
            x = current.x;
            y = current.y;
            if (visit[y][x]) continue;

            Point top = new Point(x, y - 1);
            Point down = new Point(x, y + 1);
            Point left = new Point(x - 1, y);
            Point right = new Point(x + 1, y);
            sameColorCnt += addQueueIfSameColor(current, top, down, left, right);
            visit[y][x] = true;
        }
        return sameColorCnt >= 3;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int y, x;
        int popCnt = 0;
        for (y = 0; y < SIZE; y++) for (x = 0; x < SIZE; x++) candies[y][x] = sc.nextInt();
        for (y = 0; y < SIZE; y++)
            for (x = 0; x < SIZE; x++) {
                if (visit[y][x]) continue;
                if (bfs(x, y)) popCnt++;
            }
        System.out.println(popCnt);
    }
}
