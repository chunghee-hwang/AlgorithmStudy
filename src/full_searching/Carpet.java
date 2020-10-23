package src.full_searching;

import java.util.Arrays;

// https://programmers.co.kr/learn/courses/30/lessons/42842
public class Carpet {
    private static void getWh(int []fullWh, int []redWh, int red){
        redWh[0] = red / redWh[1];
        fullWh[0] = redWh[0] + 2;
        fullWh[1] = redWh[1] + 2;
    }
    public static int[] solution(int brown, int red) {
        int []fullWh = {0,0};
        int []redWh = {red,1};
        int area = brown + red;
        while(redWh[1] != red && fullWh[0] >= fullWh[1]){
            if(red % redWh[1] == 0){
                getWh(fullWh,redWh,red);
                if(fullWh[0] * fullWh[1] == area)
                    break;
            }
            redWh[1]++;
        }
        if(fullWh[0]==0 && fullWh[1] == 0){
            fullWh[0] = 3; fullWh[1] = 3;
        }
        return fullWh;
    }
    public static void main(String[] args) {
        int brown = 50;
        int red = 50;
        System.out.println(Arrays.toString(solution(brown, red)));
    }
}
