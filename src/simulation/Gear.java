package simulation;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//https://www.acmicpc.net/problem/14891
public class Gear {
    private char[][] gears;
    private int[] topPoleIdx = new int[5];
    private boolean[] visit = new boolean[5];
    private int getLeftPoleIdx(int topPoleIdx){
        return topPoleIdx-2>=0? topPoleIdx-2:topPoleIdx+6;
    }
    private int getRightPoleIdx(int topPoleIdx){
        return (topPoleIdx+2)%8;
    }
    private void rotateGear(int gearIdx, int direction){
        if(visit[gearIdx])return;
        int curTopPoleIdx = topPoleIdx[gearIdx];
        int curLeftPoleIdx = getLeftPoleIdx(curTopPoleIdx);
        int curRightPoleIdx = getRightPoleIdx(curTopPoleIdx);
        curTopPoleIdx-=direction;
        if(curTopPoleIdx < 0) curTopPoleIdx = 7;
        else if(curTopPoleIdx > 7) curTopPoleIdx = 0;
        topPoleIdx[gearIdx] = curTopPoleIdx;
        visit[gearIdx] = true;
        if(gearIdx > 1){
            int leftGearIdx = gearIdx-1;
            int leftGearTopPoleIdx = topPoleIdx[leftGearIdx];
            int leftGearRightPoleIdx = getRightPoleIdx(leftGearTopPoleIdx);
            if(gears[leftGearIdx][leftGearRightPoleIdx] != gears[gearIdx][curLeftPoleIdx]) {
                rotateGear(leftGearIdx, -direction);
            }
        }
        if(gearIdx < 4){
            int rightGearIdx = gearIdx+1;
            int rightGearTopPoleIdx = topPoleIdx[rightGearIdx];
            int rightGearLeftPoleIdx = getLeftPoleIdx(rightGearTopPoleIdx);
            if(gears[rightGearIdx][rightGearLeftPoleIdx] != gears[gearIdx][curRightPoleIdx]){
                rotateGear(rightGearIdx, -direction);
            }
        }
    }

    private void printScoreSum(){
        int scoreSum = 0;
        for(int idx = 1; idx <=4; idx++){
            if(gears[idx][topPoleIdx[idx]] == '1')
                scoreSum+= Math.pow(2, idx-1);
        }
        System.out.println(scoreSum);
    }

    private Gear() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        gears = new char[5][8];
        gears[1] = br.readLine().toCharArray();
        gears[2] = br.readLine().toCharArray();
        gears[3] = br.readLine().toCharArray();
        gears[4] = br.readLine().toCharArray();
        int n = Integer.parseInt(br.readLine());
        for(int k = 0; k < n; k++){
            st = new StringTokenizer(br.readLine());
            int gearIdx = Integer.parseInt(st.nextToken());
            int rotateDirection = Integer.parseInt(st.nextToken());
            rotateGear(gearIdx, rotateDirection);
            visit = new boolean[5];
        }
        printScoreSum();
    }

    public static void main(String[] args) throws IOException {
        new Gear();
    }
}
