package src.dynamic_programming;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
/*
https://codeup.kr/problem.php?id=3703
 */

public class GetCandy {
    private static int[][] map; //맵

    //mem[y][x]: (y,x)셀부터 마지막 셀까지의 경로중 사탕을 가장 많이 얻을 수 있는 경로의 사탕개수합
    private static int[][] mem;
    private static int n, m;
    private static int dp(int y, int x) {
        //이미 (y,x)셀부터 마지막 셀까지의 경로중 사탕을 가장 많이 얻을 수 있는 경로의 사탕개수합을 알고 있다면 반환
        if (mem[y][x] != 0) return mem[y][x];
        boolean yCheck = y + 1 < n;
        boolean xCheck = x + 1 < m;
        int down = -1;
        int right = -1;
        /*짧은 길로 가기 위해선 무조건 오른쪽이나 아래로만 가야함*/

        //바로 아래 셀 부터 마지막 셀 경로들의 가장 많이 모을 수 있는 사탕의 수
        if (yCheck) down = dp(y + 1, x);

        //바로 오른쪽 셀 부터 마지막 셀 경로들의 가장 많이 모을 수 있는 사탕의 수
        if (xCheck) right = dp(y, x + 1);

        //마지막 셀을 방문할 경우 그 셀의 사탕 수 반환
        if (!yCheck && !xCheck) return mem[y][x] = map[y][x];

        //현재 위치의 사탕수 + max(아래셀~마지막셀 까지의 최대 모을 수 있는 사탕, 오른쪽셀~마지막셀까지의 최대 모을 수 있는 사탕) 저장
        return mem[y][x] = map[y][x]+Math.max(down, right);
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
