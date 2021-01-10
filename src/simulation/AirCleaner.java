import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
//https://www.acmicpc.net/problem/17144
public class AirCleaner {
    private int cleanerPosY1, cleanerPosY2;
    private int r, c, t;
    private int[][] dusts;
    private void collectRoomInfo() {
        StringTokenizer st;
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {
            st = new StringTokenizer(br.readLine());
            r = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());
            t = Integer.parseInt(st.nextToken());
            dusts = new int[r][c];
            int y, x;
            for (y = 0; y < r; y++) {
                st = new StringTokenizer(br.readLine());
                for (x = 0; x < c; x++) {
                    int dust = Integer.parseInt(st.nextToken());
                    dusts[y][x] = dust;
                    if (dust == -1) {
                        if (cleanerPosY1 == 0) cleanerPosY1 = y;
                        else cleanerPosY2 = y;
                        dusts[y][x] = 0;
                    }
                }
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void spreadDust() {
        int[][] buffer = new int[r][c];
        int y, x;
        int spreadDust;
        int b,a;

        for (y = 0; y < r; y++) {
            for (x = 0; x < c; x++) {
                int cnt = 0;
                spreadDust = dusts[y][x] / 5;
                if(spreadDust ==0)
                    continue;
                a = x; b = y-1;

                if (b >= 0 && (a != 0 || (b != cleanerPosY1 && b != cleanerPosY2))) {
                    buffer[b][a]+= spreadDust;
                    cnt++;
                }
                b = y+1;
                if(b < r && (a != 0 || (b != cleanerPosY1 && b != cleanerPosY2))){
                    buffer[b][a]+= spreadDust;
                    cnt++;
                }
                b = y; a = x-1;
                if(a >= 0 && (a != 0 || (b != cleanerPosY1 && b != cleanerPosY2))){
                    buffer[b][a]+= spreadDust;
                    cnt++;
                }
                a = x+1;
                if(a<c && (a != 0 || (b != cleanerPosY1 && b != cleanerPosY2))){
                    buffer[b][a]+=spreadDust;
                    cnt++;
                }
                dusts[y][x]-=spreadDust*cnt;
            }
        }

        for (y = 0; y < r; y++) {
            for (x = 0; x < c; x++) {
                dusts[y][x]+=buffer[y][x];
            }
        }

    }
    private void cleanDust(int dir) {
        int y = dir==-1?cleanerPosY1:cleanerPosY2;
        int x = 1;
        int buffer = 0;
        int temp;
        while(x < c){
            temp = dusts[y][x];
            dusts[y][x++] = buffer;
            buffer = temp;
        }
        x--;
        if(dir == -1) {
            y--;
            while (y >= 0) {
                temp = dusts[y][x];
                dusts[y--][x] = buffer;
                buffer = temp;
            }
            y++;
        }
        else{
            y++;
            while (y < r) {
                temp = dusts[y][x];
                dusts[y++][x] = buffer;
                buffer = temp;
            }
            y--;
        }

        x--;
        while(x >= 0){
            temp = dusts[y][x];
            dusts[y][x--] = buffer;
            buffer = temp;
        }
        x++;
        if(dir == -1){
            y++;
            while(y < cleanerPosY1){
                temp = dusts[y][x];
                dusts[y++][x] = buffer;
                buffer = temp;
            }
        }
        else{
            y--;
            while(y > cleanerPosY2){
                temp = dusts[y][x];
                dusts[y--][x] = buffer;
                buffer = temp;
            }
        }

    }

    private void simulateAirForSeconds() {
        for (int s = 0; s < t; s++) {
            spreadDust();
            cleanDust(-1);
            cleanDust(1);
        }
    }

    private void showDustSum(){
        int y,x, sum = 0;
        for (y = 0; y < r; y++) {
            for (x = 0; x < c; x++) {
                sum+=dusts[y][x];
            }
        }
        System.out.println(sum);
    }

    private AirCleaner() {
        collectRoomInfo();
        simulateAirForSeconds();
        showDustSum();
    }

    public static void main(String[] args) {
        new AirCleaner();
    }
}