package src.math;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//https://www.acmicpc.net/problem/1002
public class Turret {
    private static class Position {
        private int[] joguhyeon;
        private int[] packseonghwan;

        private Position(int[] j, int[] p) {
            joguhyeon = j;
            packseonghwan = p;
        }

        static Position make(int[] j, int[] p) {
            return new Position(j, p);
        }

        // 두 원의 위치관계에 따라서 접점이 달라짐 https://mathbang.net/101
        private int getRyujaemyeongCoordinateCnt() {
            int x1, x2, y1, y2, r1, r2;
            int rDiff, rSum;
            double d;
            x1 = joguhyeon[0];
            x2 = packseonghwan[0];
            y1 = joguhyeon[1];
            y2 = packseonghwan[1];
            r1 = joguhyeon[2];
            r2 = packseonghwan[2];
            d = Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2));
            rDiff = Math.abs(r1 - r2);
            rSum = r1 + r2;
            if (d == 0 && r1 == r2) return -1; //원의 중심이 같고 반지름까지 같은 경우
            else if (rDiff < d && d < rSum) return 2; // 두 점에서 만날 경우
            else if (rSum == d || rDiff == d) return 1; // 한 점에서 만날 경우
            else if (rSum < d || d < rDiff || (d == 0 && r1 != r2)) return 0; // 만나지 않을 경우
            return 0;
        }
    }

    public static void main(String[] args) {
        StringTokenizer st;
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {
            int T = Integer.parseInt(br.readLine());
            int a;
            for (int t = 0; t < T; t++) {
                st = new StringTokenizer(br.readLine());
                int[] j = new int[3];
                int[] p = new int[3];
                for (a = 0; a < 3; a++) j[a] = Integer.parseInt(st.nextToken());
                for (a = 0; a < 3; a++) p[a] = Integer.parseInt(st.nextToken());
                System.out.println(Position.make(j, p).getRyujaemyeongCoordinateCnt());
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
