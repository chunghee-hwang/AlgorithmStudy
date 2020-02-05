package simulation;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Snake {
    private int n;
    private int[][] map;
    private int[] controls;
    private final int apple = 3;
    private final int body = 2;
    private ArrayDeque<int[]> snake = new ArrayDeque<>();
    private void makeMap(int n) {
        map = new int[n][n];
        map[0][0] = body;
        snake.add(new int[]{0,0});
    }

    private void putApple(int y, int x) {
        map[y][x] = apple;
    }

    // direction> -1 : left, +1: right
    private void setControl(int seconds, int control) {
        controls[seconds] = control;
    }

    private void loadMap() {
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {
            int a;
            StringTokenizer st;
            n = Integer.parseInt(br.readLine());
            int k = Integer.parseInt(br.readLine());
            makeMap(n);
            for (a = 0; a < k; a++) {
                st = new StringTokenizer(br.readLine());
                putApple(Integer.parseInt(st.nextToken()) - 1, Integer.parseInt(st.nextToken()) - 1);
            }
            int l = Integer.parseInt(br.readLine());
            controls = new int[10001];
            for (a = 0; a < l; a++) {
                st = new StringTokenizer(br.readLine());
                setControl(Integer.parseInt(st.nextToken()), st.nextToken().equals("D") ? 1 : -1);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private int getDirection(int dirsIdx, int seconds) {
        dirsIdx += controls[seconds];
        if (dirsIdx < 0) dirsIdx = 3;
        else if (dirsIdx > 3) dirsIdx = 0;
        return dirsIdx;
    }

    private boolean isBorder(int y, int x) {
        return y < 0 || x < 0 || y >= n || x >= n;
    }

    private boolean checkApple(int nextY, int nextX) {
        return map[nextY][nextX] == apple;
    }

    private void moveSnake(int nextY, int nextX) {
        if (isBorder(nextY, nextX)) return;
        snake.add(new int[]{nextY, nextX});
        int[] tailPos;
        if(!checkApple(nextY, nextX)){
            tailPos = snake.remove();
            map[tailPos[0]][tailPos[1]] = 0;
        }
        map[nextY][nextX] = body;
    }

    private boolean checkCollide(int nextY, int nextX) {
        if(isBorder(nextY,nextX))return true;
        return map[nextY][nextX] == body;
    }

    private void simulateSnake() {
        int y = 0, x = 0; //head pos
        int nextY, nextX;
        //left, up, right, down
        final int[][] dirs = {{0, -1}, {-1, 0}, {0, 1}, {1, 0}};
        int dirsIdx = 2;
        int[] dir;
        int seconds = 0;
        do{
            dirsIdx = getDirection(dirsIdx, seconds);
            dir = dirs[dirsIdx];
            nextY = y + dir[0];
            nextX = x + dir[1];
            if(checkCollide(nextY, nextX)){
                seconds++; break;
            }
            else {
                moveSnake(nextY, nextX);
            }
            seconds++;
            y = nextY;
            x = nextX;
        }
        while (!isBorder(y, x));
        System.out.print(seconds);
    }

    public static void main(String[] args){
        Snake snake = new Snake();
        snake.loadMap();
        snake.simulateSnake();
    }
}

