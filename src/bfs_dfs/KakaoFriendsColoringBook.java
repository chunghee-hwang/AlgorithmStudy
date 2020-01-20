package bfs_dfs;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;

//https://programmers.co.kr/learn/courses/30/lessons/1829
public class KakaoFriendsColoringBook {
    private static class Pair {
        private int r, c;

        Pair(int r, int c) {
            this.r = r;
            this.c = c;
        }

        static Pair make(int r, int c) {
            return new Pair(r, c);
        }
    }

    public static int[] solution(int m, int n, int[][] picture) {
        Queue<Pair> q = new ArrayDeque<>();
        int areaCnt = 0;
        boolean[][] visit = new boolean[m][n];
        int mn = m * n;
        int maxArea = 0;
        for (int i = 0; i < mn; i++)
        {
            int row = i / n;
            int column = i % n;
            if (visit[row][column] || picture[row][column] == 0) continue;
            q.add(Pair.make(row, column));
            visit[row][column] = true;
            areaCnt++;
            int area = 0;
            while (!q.isEmpty()) {
                Pair pair = q.remove();
                area++;
                int r = pair.r;
                int c = pair.c;
                int color = picture[r][c];

                //left
                if (c - 1 >= 0 && !visit[r][c - 1] && picture[r][c - 1] == color) {
                    q.add(Pair.make(r, c - 1));
                    visit[r][c-1] = true;
                }

                //right
                if (c + 1 < n && !visit[r][c + 1] && picture[r][c + 1] == color) {
                    q.add(Pair.make(r, c + 1));
                    visit[r][c + 1] = true;
                }

                //top
                if (r - 1 >= 0 && !visit[r - 1][c] && picture[r - 1][c] == color) {
                    q.add(Pair.make(r - 1, c));
                    visit[r - 1][c] = true;
                }

                //bottom
                if (r + 1 < m && !visit[r + 1][c] && picture[r + 1][c] == color) {
                    q.add(Pair.make(r + 1, c));
                    visit[r + 1][c] = true;
                }
            }
            if(maxArea < area) maxArea = area;
        }


        return new int[]{areaCnt, maxArea};
    }

    public static void main(String[] args) {
        int[][] picture = {{1, 1, 1, 0}, {1, 1, 1, 0}, {0,0,0,1}, {0, 0, 0, 1}, {0, 0, 0, 1}, {0, 0, 0, 1}};
        System.out.print(Arrays.toString(solution(6, 4, picture)));
    }
}
