package src.simulation;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;
//https://www.acmicpc.net/problem/1021
public class RotatingQueue {
    private ArrayDeque<Integer> q = new ArrayDeque<>();
    private void shiftLeft(){
        q.add(q.poll());
    }
    private void shiftRight(){
        q.addFirst(q.pollLast());
    }
    // return = {left : -2|| right : 2|| do not move : 0, min distance}
    private int[] getBetterShiftDirection(int s){
        int[] directionAndDistance = {0,0};
        if(q.isEmpty()) {
            directionAndDistance[0] = -1;
            return directionAndDistance;
        }
        if(s == q.peek()){
            return directionAndDistance;
        }
        int leftShiftDistance =0, rightShiftDistance;
        for (Integer elem : q) {
            if(elem == s) break;
            leftShiftDistance++;
        }
        rightShiftDistance = q.size() - leftShiftDistance;
        if(leftShiftDistance < rightShiftDistance){
            directionAndDistance[0] = -2;
            directionAndDistance[1] = leftShiftDistance;
        }
        else{
            directionAndDistance[0] = 2;
            directionAndDistance[1] = rightShiftDistance;
        }
        return directionAndDistance;
    }
    private RotatingQueue(){
        StringTokenizer st;
        try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int a;
            int distanceSum = 0;
            int []seek = new int[m];
            int[] directionAndDistance;
            int direction, distance;
            st = new StringTokenizer(br.readLine());
            for(a = 1; a <= n; a++) q.add(a);
            for(a = 0; a < m; a++) seek[a] = Integer.parseInt(st.nextToken());
            for (int s : seek) {
                directionAndDistance = getBetterShiftDirection(s);
                direction = directionAndDistance[0];
                distance = directionAndDistance[1];
                distanceSum+=distance;
                switch (direction)
                {
                    case -2:
                        for(a= 0; a< distance; a++) shiftLeft();
                        q.poll();
                        break;
                    case 2:
                        for(a= 0; a< distance; a++) shiftRight();
                        q.poll();
                        break;
                    case 0:
                        q.poll();
                        break;
                }
            }
            System.out.println(distanceSum);
        }catch (IOException e){
            e.printStackTrace();
        }
    }
    public static void main(String[] args) {
        new RotatingQueue();
    }
}
